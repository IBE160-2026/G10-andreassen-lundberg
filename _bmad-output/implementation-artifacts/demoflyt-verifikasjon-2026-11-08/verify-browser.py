# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright==1.58.0", "tzdata"]
# ///
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from zoneinfo import ZoneInfo
import argparse
import json
import re
import subprocess
from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser(description="Faktisk lokal VaktMatch-demo med Playwright; ingen modellkall.")
parser.add_argument("--url", default="http://localhost:5173")
parser.add_argument("--browser", help="Valgfri Chromium-binær; ellers brukes Playwrights installerte nettleser")
parser.add_argument("--axe", help="Valgfri lokal axe.min.js; uten denne kjøres ikke axe-kontroller")
parser.add_argument("--out", help="Rapportfil; standard er en ny, tidsstemplet browser-results-*.json")
args = parser.parse_args()
OUT = Path(__file__).parent
ROOT = Path(__file__).resolve().parents[3]
STARTED = datetime.now(ZoneInfo("Europe/Oslo"))
REPORT = Path(args.out) if args.out else OUT / f"browser-results-{STARTED:%Y%m%d-%H%M%S}.json"


def git(*command):
    try:
        return subprocess.run(["git", *command], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "ukjent"


def provenance(page):
    # K11: knytt rårapporten til kildegrunnlag og faktisk kjørende backend.
    digest = sha256()
    for path in sorted((ROOT / "backend" / "data" / "datasets").glob("*.json")):
        digest.update(path.name.encode() + b"\0" + path.read_bytes())
    base = args.url.rstrip("/")
    try:
        health = page.request.get(base + "/api/health").json()
    except Exception as error:
        health = {"error": f"{type(error).__name__}: {error}"}
    try:
        served = sorted(f"{d['id']}@{d['version']}" for d in page.request.get(base + "/api/datasets").json())
    except Exception as error:
        served = [f"{type(error).__name__}: {error}"]
    return {
        "started_at": STARTED.isoformat(timespec="seconds"),
        "finished_at": datetime.now(ZoneInfo("Europe/Oslo")).isoformat(timespec="seconds"),
        "commit": git("rev-parse", "HEAD"),
        "app_worktree_dirty": bool(git("status", "--porcelain", "--", "backend", "frontend")),
        "datasets_sha256": digest.hexdigest(),
        "backend_health": health,
        "served_datasets": served,
        "axe_version": page.evaluate("() => window.axe?.version ?? null") if axe else None,
    }
checks = []
page_errors = []
external_requests = []
axe = Path(args.axe) if args.axe else None


def check(name, condition, details=""):
    checks.append({"check": name, "passed": bool(condition), "details": details})


with sync_playwright() as p:
    launch = {"headless": True}
    if args.browser:
        launch["executable_path"] = args.browser
    browser = p.chromium.launch(**launch)
    page = browser.new_page(viewport={"width": 1440, "height": 1000}, reduced_motion="reduce")
    page.on("pageerror", lambda error: page_errors.append(str(error)))
    page.on("request", lambda request: external_requests.append(request.url) if request.url.startswith("http") and not re.match(r"https?://(127\.0\.0\.1|localhost)(:|/)", request.url) else None)

    def button(name):
        return page.get_by_role("button", name=name, exact=True)

    def boot(width=1440):
        page.set_viewport_size({"width": width, "height": 1000})
        page.goto(args.url)
        button("Registrer fravær").wait_for()

    def measure(screen, width):
        check(f"{screen}: {width}px uten vannrett rulling", not page.evaluate("document.documentElement.scrollWidth > innerWidth + 1"))
        if axe:
            page.add_script_tag(path=str(axe))
            findings = page.evaluate("async () => (await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}})).violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>n.target)}))")
            check(f"axe: {screen} {width}px", not findings, findings)

    def simulate():
        button("Registrer fravær").click()
        page.get_by_role("radio").first.wait_for()
        with page.expect_response(lambda response: "/api/absences/simulate" in response.url) as info:
            button("Simuler fravær").click()
        check("Fraværssimulering gir gyldig API-respons", info.value.status == 200)
        page.get_by_label("Søkegrense", exact=True).wait_for()

    def search(limit="0"):
        page.get_by_label("Søkegrense", exact=True).select_option(limit)
        with page.expect_response(lambda response: "/api/evaluate" in response.url) as info:
            button("Finn alternativer").click()
        result = info.value.json()
        expect(button("Finn alternativer")).to_be_enabled()
        page.locator("#result-title").wait_for()
        return result

    def inspect(person, kind="Direkte erstatter"):
        page.get_by_role("button", name=re.compile(f"^Undersøk {person}, {kind},")).first.click()
        expect(page.get_by_role("heading", name="Undersøk alternativ", exact=True)).to_be_visible()

    def full_acceptance():
        return "Full simulert aksept" in "\n".join(page.locator(".work > section.panel > p").all_text_contents())

    def swap(identifier):
        button("Datagrunnlag").click()
        page.get_by_label("Nytt datasett", exact=True).select_option(identifier)
        with page.expect_response(lambda response: "/api/datasets/compare" in response.url):
            button("Forhåndsvis endringer").click()
        with page.expect_response(lambda response: "/api/state" in response.url):
            button("Last inn oppdaterte vaktdata").click()
        expect(page.get_by_role("heading", name="Ukesoversikt", exact=True)).to_be_visible()

    try:
        boot()
        measure("ukesoversikt", 1440)
        simulate()
        result = search()
        direct = [a for a in result["alternatives"] if a["rank"] is not None]
        check("S1: beregnede direkte forslag A02/A03 i P1-rekkefølge", [a["candidate_id"] for a in direct] == ["A02", "A03"])
        check("S1: API sender eksakte timetall", [(a["p1"]) for a in direct] == ["32", "40"])
        measure("alternativer", 1440)
        page.screenshot(path=str(REPORT.with_name(f"live-alternatives-desktop-{STARTED:%Y%m%d-%H%M%S}.png")), full_page=True)
        p2 = page.get_by_role("checkbox", name=re.compile("^P2"))
        p1 = page.get_by_role("checkbox", name=re.compile("^P1"))
        with page.expect_response(lambda response: "/api/evaluate" in response.url):
            p2.check()
        expect(button("Finn alternativer")).to_be_enabled()
        with page.expect_response(lambda response: "/api/evaluate" in response.url) as second:
            p1.uncheck()
        expect(button("Finn alternativer")).to_be_enabled()
        check("P2 kommer fra backend og setter A03 først", [a["candidate_id"] for a in second.value.json()["alternatives"] if a["rank"] is not None] == ["A03", "A02"])
        p2.click()
        check("Siste kriterium beholdes", p2.is_checked())
        inspect("A03")
        measure("detaljer", 1440)
        with page.expect_response(lambda response: "/api/explain" in response.url):
            button("Forklar forskjellen").click()
        expect(button("Velg alternativ")).to_be_enabled()
        check("Nøkkelfri forklaringsreserve er synlig", "KI-forklaring er ikke tilgjengelig" in page.locator("main").inner_text())
        button("Velg alternativ").click()
        button("Simuler tilbud").click()
        button("Simuler aksept for A03").click()
        check("Direkte aksept er separat øktstatus", full_acceptance())
        measure("valg", 1440)
        button("Undersøk et annet alternativ").click()
        inspect("A02"); button("Velg alternativ").click()
        button("Undersøk et annet alternativ").click()
        inspect("A03"); button("Velg alternativ").click()
        check("A → B → A bevarer As svar", full_acceptance())
        swap("komplettert")
        button("3 Valg").click()
        page.get_by_text(re.compile("^Tidligere valg")).click()
        check("Datasettbytte bevarer gammelt valg som historikk", "hovedscenario" in page.locator("main").inner_text() and "aksept" in page.locator("main").inner_text())
        check("Gammel aksept er ikke gjeldende valg på nye data", "Ingen gjeldende valg" in page.locator("main").inner_text())
        swap("hovedscenario")
        button("2 Alternativer").click()
        search("0")
        inspect("A03"); button("Velg alternativ").click()
        check("Retur til tidligere datasett vekker ikke gammel aksept", not full_acceptance() and "Aksept ikke simulert" in "\n".join(page.locator(".work > section.panel > p").all_text_contents()))
        button("Datagrunnlag").click()
        measure("datagrunnlag", 1440)
        swap("en-flytting")
        simulate()
        none = search("0")
        check("UJ-2: ingen direkte kontrollerte løsninger", not any(a["selectable"] for a in none["alternatives"]))
        chain = search("1")
        solution = next(a for a in chain["alternatives"] if a["selectable"])
        check("UJ-2: begge berørte beregnes i én flytting", solution["candidate_id"] == "B" and set(solution["affected_employee_ids"]) == {"B", "C"})
        inspect("B", "Én flytting")
        button("Velg alternativ").click(); button("Simuler tilbud").click()
        button("Simuler aksept for B").click()
        check("Én av to aksepter gir ikke full aksept", not full_acceptance())
        button("Simuler aksept for C").click()
        check("To av to aksepter gir full simulert aksept", full_acceptance())
        button("Undersøk et annet alternativ").click()
        search("0")
        button("3 Valg").click()
        check("Utelatt flytteforslag blir ikke gyldig valg ved ny grense0", "Ingen gjeldende valg" in page.locator("main").inner_text() or not button("Simuler aksept for B").is_enabled())
        boot(360)
        measure("ukesoversikt", 360)
        button("Registrer fravær").click()
        page.get_by_role("radio").first.wait_for()
        measure("fravær", 360)
        page.get_by_label("Ansatt", exact=True).select_option("")
        button("Simuler fravær").click()
        check("Ugyldig skjema har koblet feltfeil", page.get_by_label("Ansatt", exact=True).get_attribute("aria-invalid") == "true")
        page.get_by_label("Ansatt", exact=True).select_option("A01")
        page.get_by_role("radio").first.wait_for()
        button("Simuler fravær").click()
        result = search("0")
        measure("alternativer", 360)
        page.screenshot(path=str(REPORT.with_name(f"live-alternatives-mobile-{STARTED:%Y%m%d-%H%M%S}.png")), full_page=True)
        inspect("A02")
        measure("detaljer", 360)
        button("Velg alternativ").click()
        measure("valg", 360)
        button("Datagrunnlag").click()
        measure("datagrunnlag", 360)
        page.set_viewport_size({"width": 1440, "height": 1000})
        button("2 Alternativer").click()
        page.evaluate("document.documentElement.style.fontSize='200%'")
        check("200% tekst flyter om", not page.evaluate("document.documentElement.scrollWidth > innerWidth + 1"))
        boot()
        reached = False
        for _ in range(35):
            page.keyboard.press("Tab")
            if page.evaluate("document.activeElement?.textContent.trim()") == "Registrer fravær":
                reached = True
                break
        check("Tastatur kan nå fraværsinngangen", reached)
        if reached:
            page.keyboard.press("Enter")
            expect(page.get_by_role("heading", name="Registrer fravær", exact=True)).to_be_visible()
            page.get_by_role("radio").first.wait_for()
            reached = False
            for _ in range(25):
                page.keyboard.press("Tab")
                if page.evaluate("document.activeElement?.textContent.trim()") == "Simuler fravær":
                    reached = True
                    break
            check("Tastatur kan nå simulering uten felle", reached)
            if reached:
                page.keyboard.press("Enter")
                expect(page.get_by_role("heading", name="Sammenlign alternativer", exact=True)).to_be_visible()
        page.route("**/api/datasets", lambda route: route.abort())
        page.goto(args.url)
        expect(page.get_by_role("alert")).to_contain_text("Backend er utilgjengelig")
        check("Simulert nettverksfeil mot backend gir norsk feil uten falske resultater", "Backend er utilgjengelig" in page.get_by_role("alert").inner_text() and page.locator("article.card").count() == 0)
        page.unroute("**/api/datasets")
        button("Prøv igjen").click()
        button("Registrer fravær").wait_for()
        check("Gjenforsøk etter backendfeil laster virkelig grunnlag", button("Registrer fravær").is_visible())
        button("Registrer fravær").click()
        page.get_by_role("radio").first.wait_for()
        attempts = []
        def fail_first_simulation(route):
            attempts.append(1)
            route.abort() if len(attempts) == 1 else route.continue_()
        page.route("**/api/absences/simulate", fail_first_simulation)
        button("Simuler fravær").click()
        expect(page.get_by_role("alert")).to_be_visible()
        with page.expect_response(lambda response: "/api/absences/simulate" in response.url):
            button("Prøv igjen").click()
        expect(page.get_by_role("heading", name="Sammenlign alternativer", exact=True)).to_be_visible()
        check("Gjenforsøk av simulering utfører faktisk ny handling", len(attempts) == 2)
        page.unroute("**/api/absences/simulate")
        page.clock.install()
        held_requests = []
        page.route("**/api/evaluate", lambda route: held_requests.append(route))
        button("Finn alternativer").click()
        expect(button("Finn alternativer")).to_be_disabled()
        page.clock.run_for(60001)
        expect(page.get_by_role("alert")).to_be_visible()
        check("Hengende forespørsel avsluttes med norsk feil og åpne handlinger", button("Finn alternativer").is_enabled() and "AbortError" not in page.get_by_role("alert").inner_text(), page.get_by_role("alert").inner_text())
        for held in held_requests:
            try:
                held.abort()
            except Exception:
                pass  # Klienten kan allerede ha avbrutt nettleserforespørselen.
        page.unroute("**/api/evaluate")
        with page.expect_response(lambda response: "/api/evaluate" in response.url):
            button("Prøv igjen").click()
        expect(page.locator("#result-title")).to_be_visible()
        check("Gjenforsøk etter tidsavbrudd gir nytt faktisk resultat", page.locator("article.card:visible").count() > 0)
    except Exception as error:
        check("Samlet nettleserflyt fullført", False, f"{type(error).__name__}: {error}")
        page.screenshot(path=str(REPORT.with_name(f"live-failure-{STARTED:%Y%m%d-%H%M%S}.png")), full_page=True)
    finally:
        check("Ingen JavaScript-feil i appen", not page_errors, page_errors)
        check("Ingen eksterne modell-/leverandørkall", not external_requests, external_requests)
        report = {"scope": "Faktisk lokal app, ikke HTML-prototypen", "url": args.url, "browser": browser.version, "axe_enabled": bool(axe), "provenance": provenance(page), "checks": checks, "passed": sum(x["passed"] for x in checks), "failed": [x for x in checks if not x["passed"]]}
        REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"report": str(REPORT), "passed": report["passed"], "failed": report["failed"]}, ensure_ascii=True))
        browser.close()

raise SystemExit(bool(report["failed"]))
