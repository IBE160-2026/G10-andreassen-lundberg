# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6,<7", "playwright==1.58.0"]
# ///
"""Kontroll av UX-dokumenter og offlineprototype, ikke av VaktMatch-regelmotoren.

Kjør fra repoets rot: uv run <sti-til-denne-filen> [--browser <chromium.exe>]
Nettleser kan installeres med: uv run --with playwright==1.58.0 playwright install chromium
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote

import yaml
from playwright.sync_api import expect, sync_playwright

WORKSPACE = Path(__file__).resolve().parent.parent
RESULTS: list[dict] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    RESULTS.append({"check": name, "passed": bool(condition), "detail": detail})


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    assert len(parts) == 3, f"Mangler YAML-frontmatter: {path.name}"
    return yaml.safe_load(parts[1]), text


def token_value(tokens: dict, name: str):
    value = tokens
    for key in name.split("."):
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def luminance(color: str) -> float:
    channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(foreground: str, background: str) -> float:
    a, b = sorted((luminance(foreground), luminance(background)))
    return (b + 0.05) / (a + 0.05)


def table_components(text: str, section: str) -> set[str]:
    body = text.split(f"## {section}", 1)[1].split("\n## ", 1)[0]
    rows = [line.split("|")[1].strip().strip("*`") for line in body.splitlines() if line.startswith("|")]
    return {row for row in rows[2:] if row and not row.startswith("-")}


def document_checks() -> None:
    design, design_text = frontmatter(WORKSPACE / "DESIGN.md")
    experience, experience_text = frontmatter(WORKSPACE / "EXPERIENCE.md")
    check("Begge UX-kontraktene ferdigstilt", design.get("status") == experience.get("status") == "final")
    for name, text in (("DESIGN", design_text), ("EXPERIENCE", experience_text)):
        refs = re.findall(r"\{((?:colors|typography|rounded|spacing|components)\.[\w.-]+)\}", text)
        missing = sorted({ref for ref in refs if token_value(design, ref) is None})
        check(f"{name}: tokenreferanser", not missing, f"{len(refs)} referanser; mangler: {missing}")
    colors = design.get("colors", {})
    check("Fargetokens har konkrete hexverdier", bool(colors) and all(re.fullmatch(r"#[0-9a-fA-F]{6}", c) for c in colors.values()))
    color_pairs = [("ink", "surface", 4.5), ("ink", "background", 4.5), ("ink-secondary", "surface", 4.5), ("ink-secondary", "background", 4.5), ("on-primary", "primary", 4.5), ("positive", "positive-soft", 4.5), ("caution", "caution-soft", 4.5), ("negative", "negative-soft", 4.5), ("focus", "surface", 3), ("focus", "background", 3), ("border", "surface", 3)]
    for foreground, background, minimum in color_pairs:
        ratio = contrast(colors[foreground], colors[background])
        check(f"Kontrast {foreground}/{background}", ratio >= minimum, f"{ratio:.2f}:1; minimum {minimum}:1")
    visual = table_components(design_text, "Components")
    behavior = table_components(experience_text, "Component Patterns")
    check("Samme komponentsett i begge kontrakter", visual == behavior, f"Kun design: {sorted(visual - behavior)}; kun oppførsel: {sorted(behavior - visual)}")
    for path in [WORKSPACE / "DESIGN.md", WORKSPACE / "EXPERIENCE.md", WORKSPACE / "implementation-handoff.md", WORKSPACE / ".working/source-reconciliation-2026-11-08.md"]:
        text = path.read_text(encoding="utf-8")
        broken = []
        for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-z]+://|mailto:|#", href):
                continue
            target = unquote(href.split("#", 1)[0].strip("<>"))
            if not (path.parent / target).exists():
                broken.append(href)
        check(f"Lokale lenker i {path.relative_to(WORKSPACE).as_posix()}", not broken, str(broken))
    for source in design.get("sources", []) + experience.get("sources", []):
        check(f"Kilde {source}", (WORKSPACE / source).exists())
    expected = ["Foundation", "Information Architecture", "Voice and Tone", "Component Patterns", "State Patterns", "Interaction Primitives", "Accessibility Floor", "Key Flows", "Responsive & Platform"]
    check("Obligatoriske EXPERIENCE-seksjoner", all(f"## {heading}" in experience_text for heading in expected))
    order = ["Brand & Style", "Colors", "Typography", "Layout & Spacing", "Elevation & Depth", "Shapes", "Components", "Do's and Don'ts"]
    headings = re.findall(r"^## (.+)$", design_text, re.M)
    check("DESIGN-seksjoner i kanonisk rekkefølge", headings == order, str(headings))
    for path in sorted((WORKSPACE / "mockups").glob("key-*.html")):
        text = path.read_text(encoding="utf-8")
        check(f"Statisk skjermreferanse {path.name}: uten script", "<script" not in text.lower())


def interaction_checks(page, prototype: str) -> None:
    def open_settings():
        settings = page.get_by_test_id("search-settings")
        if not settings.get_attribute("open") and not settings.evaluate("el => el.open"):
            settings.locator("summary").click()

    def search_again():
        open_settings()
        page.get_by_test_id("search-again").click()
        page.get_by_test_id("ranked-candidates").wait_for()

    def ranked_ids():
        return page.get_by_test_id("ranked-candidates").locator("article").evaluate_all("els => els.map(el => el.dataset.testid)")

    page.goto(f"{prototype}?screen=absence")
    check("Søk krever eksplisitt fraværssimulering", page.get_by_test_id("search").is_disabled())
    page.get_by_test_id("person").select_option("")
    page.get_by_test_id("simulate").click()
    check("Manglende ansatt gir synlig norsk feil", "Velg" in page.locator("#form-error").inner_text() and page.get_by_test_id("search").is_disabled())
    check("Ugyldig ansattfelt er maskinlesbart", page.get_by_test_id("person").get_attribute("aria-invalid") == "true")
    page.get_by_test_id("person").select_option("A01")
    for invalid in ("0", "1.5"):
        page.get_by_test_id("days").fill(invalid)
        page.get_by_test_id("simulate").click()
        check(f"Ugyldig dagtall {invalid} simuleres ikke", page.get_by_test_id("search").is_disabled() and bool(page.locator("#form-error").inner_text()))
    page.get_by_test_id("days").fill("1")
    check("Overlappende påbegynt nattvakt vises beskyttet", page.locator("#target-past").is_disabled())
    page.get_by_test_id("simulate").click()
    page.get_by_test_id("search").click()
    page.get_by_test_id("ranked-candidates").wait_for()
    ids = ranked_ids()
    check("P1 plasserer A02 foran A03", ids.index("candidate-A02") < ids.index("candidate-A03"), str(ids))
    open_settings()
    page.get_by_test_id("criterion-p2").check()
    page.get_by_test_id("criterion-p1").uncheck()
    ids = ranked_ids()
    check("P2 plasserer A03 foran A02", ids.index("candidate-A03") < ids.index("candidate-A02"), str(ids))
    page.get_by_test_id("criterion-p2").click()
    check("Siste aktive sorteringskriterium kan ikke fjernes", page.get_by_test_id("criterion-p2").is_checked())
    page.get_by_test_id("inspect-A05").click()
    check("Regelavvik kan undersøkes, men ikke velges", page.get_by_test_id("candidate-details").is_visible() and page.get_by_test_id("choose").count() == 0)
    page.get_by_test_id("back-results").click()
    check("Tilbake fra detalj returnerer fokus til undersøkt kort", page.evaluate("document.activeElement?.dataset.testid") == "inspect-A05")
    page.get_by_test_id("inspect-A02").click()
    page.get_by_test_id("choose").click()
    page.get_by_test_id("start-offer").click()
    page.get_by_test_id("accept-A02").click()
    check("Simulert aksept er synlig for valgt forslag", "Alle berørte" in page.get_by_test_id("offer-summary").inner_text())
    page.get_by_test_id("explain").click()
    check("KI-reserve bevarer valgt alternativ og svar", page.get_by_test_id("ai-fallback").is_visible() and "Alle berørte" in page.get_by_test_id("offer-summary").inner_text())
    page.get_by_test_id("back-results").click()
    page.get_by_test_id("inspect-A03").click()
    page.get_by_test_id("choose").click()
    page.get_by_test_id("back-results").click()
    page.get_by_test_id("inspect-A02").click()
    page.get_by_test_id("choose").click()
    check("A → B → A bevarer simulerte svar for A", "Alle berørte" in page.get_by_test_id("offer-summary").inner_text())
    page.get_by_test_id("data-open").click()
    check("Datasettbytte forhåndsvises før innlasting", page.get_by_test_id("data-confirm").is_visible() and "d1" in page.locator("main").inner_text() and "d2" in page.locator("main").inner_text())
    page.get_by_test_id("data-confirm").click()
    check("Nye data krever nytt eksplisitt søk", page.get_by_test_id("ranked-candidates").count() == 0)
    search_again()
    page.get_by_test_id("inspect-A02").click()
    check("Aksept fra d1 arves ikke av d2", page.get_by_test_id("offer-panel").count() == 0 and page.get_by_test_id("choose").is_visible())
    page.get_by_test_id("data-open").click()
    history = page.get_by_test_id("session-history").inner_text()
    check("Tidligere valg og svar finnes med gammel dataversjon", "d1" in history and "A02" in history and "akseptert" in history)
    page.goto(f"{prototype}?screen=results")
    page.locator(".prototype-tools summary").click()
    page.get_by_test_id("force-empty").click()
    check("Tomt søk har avgrenset konklusjon", "Ingen kontrollerte alternativer funnet innenfor valgt søkeomfang" in page.locator("main").inner_text())
    page.locator(".prototype-tools summary").click()
    page.get_by_test_id("force-search-error").click()
    check("Søkefeil kan prøves igjen", "Søket kunne ikke fullføres" in page.locator("main").inner_text() and page.get_by_role("button", name="Prøv søket igjen", exact=True).is_visible())
    page.locator(".prototype-tools summary").click()
    page.get_by_test_id("force-load-error").click()
    check("Feilet dataoppdatering beholder siste gyldige grunnlag", "Siste gyldige grunnlag d1 er beholdt" in page.locator("main").inner_text())
    page.goto(f"{prototype}?screen=details")
    page.get_by_test_id("choose").click()
    page.get_by_test_id("start-offer").click()
    page.get_by_test_id("accept-B").click()
    check("Én av to aksepter er ikke full aksept ved flytting", "Alle berørte" not in page.get_by_test_id("offer-summary").inner_text())
    page.get_by_test_id("accept-C").click()
    check("Flytteforslag krever aksept fra begge berørte", "Alle berørte" in page.get_by_test_id("offer-summary").inner_text())
    page.goto(f"{prototype}?screen=absence")
    page.get_by_test_id("simulate").click()
    page.get_by_test_id("days").fill("2")
    check("Endret utkast krever ny eksplisitt simulering", page.get_by_test_id("search").is_disabled())
    page.get_by_role("button", name="Ukesoversikt", exact=True).click()
    check("Endret utkast fjerner ikke aktivt simulert fravær", "Udekket" in page.get_by_test_id("week-grid").inner_text())
    page.goto(f"{prototype}?screen=absence")
    reached = False
    for _ in range(30):
        page.keyboard.press("Tab")
        if page.evaluate("document.activeElement?.dataset.testid") == "simulate":
            reached = True
            break
    check("Fraværshandlingen nås med Tab uten musebruk", reached)
    if reached:
        page.keyboard.press("Enter")
        check("Tastatursimulering flytter fokus til søk", page.evaluate("document.activeElement?.dataset.testid") == "search")
        page.keyboard.press("Enter")
        page.get_by_test_id("ranked-candidates").wait_for()
        check("Hovedflyten kan åpne resultater med tastatur", page.get_by_test_id("ranked-candidates").is_visible())
    page.goto(f"{prototype}?screen=results")
    open_settings()
    page.get_by_test_id("search-limit").select_option("0")
    check("Endret søkeomfang starter ikke skjult søk", page.get_by_test_id("ranked-candidates").count() == 0)
    search_again()
    check("Grense 0 skjuler flytteeksempler", page.get_by_test_id("inspect-M01").count() == 0)
    page.goto(f"{prototype}?screen=absence")
    page.get_by_test_id("start-shift").select_option("t")
    page.get_by_test_id("simulate").click()
    page.get_by_test_id("search").click()
    check("Andre målskift bruker ikke morgenvaktens konstruerte resultater", "utenfor prototypeeksemplet" in page.locator("main").inner_text() and page.get_by_test_id("ranked-candidates").count() == 0)
    page.goto(f"{prototype}?screen=absence")
    page.get_by_test_id("start-shift").select_option("f")
    check("Låst målskift kan få registrert fravær", not page.locator("#target-f").is_disabled())
    page.get_by_test_id("simulate").click()
    check("Fravær på låst målskift kan simuleres eksplisitt", page.get_by_test_id("search").is_enabled())
    page.get_by_role("button", name="Ukesoversikt", exact=True).click()
    check("Lås skjuler ikke udekket behov i ukesoversikten", "Udekket" in page.get_by_test_id("week-grid").locator(".week-day").last.inner_text())


def export_mock(page, screen: str) -> None:
    filenames = {"week": "key-ukeplan.html", "absence": "key-fravaer.html", "results": "key-alternativer.html", "details": "key-detaljer.html"}
    html = page.evaluate("""() => {
      const root = document.documentElement.cloneNode(true);
      root.querySelectorAll('script, .prototype-tools').forEach(el => el.remove());
      root.querySelectorAll('*').forEach(el => [...el.attributes].forEach(attr => { if (attr.name.startsWith('on')) el.removeAttribute(attr.name); }));
      root.querySelectorAll('button').forEach(el => el.type = 'button');
      const caption = document.createElement('aside');
      caption.setAttribute('style', 'padding:12px 24px;background:#fff3d6;color:#79520c;text-align:center;font:14px/1.5 system-ui');
      caption.innerHTML = 'Statisk skjermreferanse · konstruert UX-eksempel. <a href="prototype.html" style="color:inherit">Åpne den klikkbare prototypen</a>.';
      root.querySelector('body').prepend(caption);
      return '<!DOCTYPE html>\\n<!-- Skjermreferanse til DESIGN.md og EXPERIENCE.md; data er illustrative. -->\\n' + root.outerHTML;
    }""")
    (WORKSPACE / "mockups" / filenames[screen]).write_text(html + "\n", encoding="utf-8")


def render_checks(browser_path: str | None, export: bool = False, axe_path: str | None = None) -> None:
    with sync_playwright() as p:
        args = {"headless": True}
        if browser_path:
            args["executable_path"] = browser_path
        browser = p.chromium.launch(**args)
        errors: list[str] = []
        network: list[str] = []
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, reduced_motion="reduce")
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda request: network.append(request.url) if request.url.startswith(("http:", "https:")) else None)
        prototype = (WORKSPACE / "mockups/prototype.html").as_uri()
        for width in (1440, 768, 360):
            page.set_viewport_size({"width": width, "height": 900})
            for screen in ("week", "absence", "results", "details"):
                page.goto(f"{prototype}?screen={screen}")
                page.wait_for_function("document.querySelector('main') && document.querySelector('main').innerText.length > 50")
                overflow = page.evaluate("document.documentElement.scrollWidth > innerWidth + 1")
                check(f"{screen}: {width}px uten vannrett rulling", not overflow)
                if export and width == 1440:
                    export_mock(page, screen)
                if axe_path and width in (1440, 360):
                    page.add_script_tag(path=axe_path)
                    violations = page.evaluate("async () => (await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa']}})).violations.map(v => ({id:v.id, impact:v.impact, elements:v.nodes.map(n => n.target)}))")
                    check(f"axe {screen} {width}px", not violations, json.dumps(violations, ensure_ascii=False))
                if width in (1440, 360) and screen in ("results", "details"):
                    page.screenshot(path=str(WORKSPACE / f".working/{screen}-{width}.png"), full_page=True)
        page.set_viewport_size({"width": 1440, "height": 1000})
        page.goto(f"{prototype}?screen=results")
        page.evaluate("document.documentElement.style.fontSize = '200%'")
        check("Alternativer flyter om ved 200% tekststørrelse", not page.evaluate("document.documentElement.scrollWidth > innerWidth + 1"))
        try:
            interaction_checks(page, prototype)
        except Exception as error:
            check("Interaksjonskontroll fullført", False, f"{type(error).__name__}: {error}")
        check("Ingen JavaScript-feil ved skjermnavigasjon", not errors, str(errors))
        check("Prototypen sender ingen nettverksforespørsler", not network, str(network))
        browser.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", help="Valgfri eksisterende Chromium-binær")
    parser.add_argument("--documents-only", action="store_true")
    parser.add_argument("--export-mocks", action="store_true")
    parser.add_argument("--axe", help="Valgfri lokal axe.min.js")
    args = parser.parse_args()
    try:
        if not args.documents_only:
            render_checks(args.browser, args.export_mocks, args.axe)
        document_checks()
    except Exception as error:
        check("Kontrollkjøring fullført", False, f"{type(error).__name__}: {error}")
    report = {"date": "2026-11-08", "scope": "UX-dokumenter og illustrativ offlineprototype; ikke app eller regelmotor", "checks": RESULTS}
    (WORKSPACE / ".working/verification-results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failed = [result for result in RESULTS if not result["passed"]]
    print(json.dumps({"passed": len(RESULTS) - len(failed), "failed": failed}, ensure_ascii=False))
    raise SystemExit(bool(failed))


if __name__ == "__main__":
    main()
