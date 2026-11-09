"""Avgrenset måling: uv run --project backend python <denne-filen>.

Hver kjøring skrives til en egen, tidsstemplet fil. Originalmålingen
benchmark-results.json fra 2026-11-08 overskrives aldri (K9, SCRUM-58).
"""

import json
import math
import platform
import statistics
import subprocess
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from zoneinfo import ZoneInfo

from vaktmatch.config import DEFAULT_DATA_DIR
from vaktmatch.data import DatasetRepository
from vaktmatch.data.schema import Absence
from vaktmatch.rules.engine import evaluate

ROOT = Path(__file__).resolve().parents[3]
WARMUPS, RUNS = 2, 12


def git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "ukjent"


def fingerprint(directory: Path) -> str:
    digest = sha256()
    for path in sorted(directory.glob("*.json")):
        digest.update(path.name.encode() + b"\0" + path.read_bytes())
    return digest.hexdigest()


started = datetime.now(ZoneInfo("Europe/Oslo"))
repository = DatasetRepository(DEFAULT_DATA_DIR)
datasets = []
for info in repository.list_datasets():
    dataset = repository.get_dataset(info.id)
    # Samme fraværsoppsett som backendtestene: A/X i flyttefamilien, ellers A01/X.
    absence = Absence(employee_id="A" if info.family_id == "flytting" else "A01", shift_id="X")
    measurements = []
    for limit in (0, 1):
        probe = evaluate(dataset, [absence], "X", limit, ["P1"])  # første oppvarming
        if probe["search_status"] != "fullfort":
            measurements.append({"search_limit": limit, "skipped": probe["message"]})
            continue
        for _ in range(WARMUPS - 1):
            evaluate(dataset, [absence], "X", limit, ["P1"])
        samples = []
        for _ in range(RUNS):
            value = evaluate(dataset, [absence], "X", limit, ["P1"])
            assert value["search_status"] == "fullfort"
            samples.append(value["duration_ms"])
        measurements.append(
            {
                "search_limit": limit,
                "warmups": WARMUPS,
                "runs": len(samples),
                "combinations_examined": value["combinations_examined"],
                "median_ms": round(statistics.median(samples), 3),
                "p95_nearest_rank_ms": sorted(samples)[math.ceil(len(samples) * 0.95) - 1],
                "errors": 0,
                "aborted": 0,
                "samples_ms": samples,
            }
        )
    datasets.append(
        {
            "dataset_id": info.id,
            "version": info.version,
            "absence": absence.model_dump(),
            "employees": len(dataset.employees),
            "shifts": len(dataset.shifts),
            "measurements": measurements,
        }
    )

report = {
    "started_at": started.isoformat(timespec="seconds"),
    "commit": git("rev-parse", "HEAD"),
    "backend_worktree_dirty": bool(git("status", "--porcelain", "--", "backend")),
    "datasets_sha256": fingerprint(DEFAULT_DATA_DIR),
    "machine": f"{platform.system()} {platform.machine()}",
    "python": platform.python_version(),
    "scope": (
        "Motorens beregningstid; ekskluderer HTTP, filinnlasting, grensesnitt og modell. "
        "Ingen tids- eller skaleringsgaranti."
    ),
    "datasets": datasets,
}
out = Path(__file__).with_name(f"benchmark-results-{started:%Y%m%d-%H%M%S}.json")
if out.exists():
    raise SystemExit(f"{out.name} finnes allerede; ingen måling overskrives.")
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Skrev {out.name}")
for item in datasets:
    for m in item["measurements"]:
        if "skipped" in m:
            print(f"  {item['dataset_id']:<20} grense {m['search_limit']}: hoppet over")
        else:
            print(
                f"  {item['dataset_id']:<20} grense {m['search_limit']}: "
                f"median {m['median_ms']} ms, p95 {m['p95_nearest_rank_ms']} ms, "
                f"{m['combinations_examined']} kombinasjoner"
            )
