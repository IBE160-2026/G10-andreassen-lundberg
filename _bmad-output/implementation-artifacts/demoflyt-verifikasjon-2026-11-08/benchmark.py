"""Avgrenset måling: uv run --project backend python <denne-filen>."""

import json
import math
import platform
import statistics
from pathlib import Path

from vaktmatch.config import DEFAULT_DATA_DIR
from vaktmatch.data import DatasetRepository
from vaktmatch.data.schema import Absence
from vaktmatch.rules.engine import evaluate

dataset = DatasetRepository(DEFAULT_DATA_DIR).get_dataset("hovedscenario")
results = []
for limit in (0, 1):
    for _ in range(2):
        evaluate(dataset, [Absence(employee_id="A01", shift_id="X")], "X", limit, ["P1"])
    samples = []
    for _ in range(12):
        value = evaluate(dataset, [Absence(employee_id="A01", shift_id="X")], "X", limit, ["P1"])
        assert value["search_status"] == "fullfort"
        samples.append(value["duration_ms"])
    results.append({
        "search_limit": limit, "warmups": 2, "runs": len(samples),
        "combinations_examined": value["combinations_examined"],
        "median_ms": round(statistics.median(samples), 3),
        "p95_nearest_rank_ms": sorted(samples)[math.ceil(len(samples) * .95) - 1],
        "errors": 0, "aborted": 0, "samples_ms": samples,
    })
report = {
    "date": "2026-11-08", "dataset_id": dataset.dataset.id,
    "version": dataset.dataset.version, "employees": len(dataset.employees),
    "shifts": len(dataset.shifts), "machine": f"{platform.system()} {platform.machine()}",
    "python": platform.python_version(),
    "scope": "Motorens beregningstid; ekskluderer HTTP, filinnlasting, grensesnitt og modell. Ingen tids- eller skaleringsgaranti.",
    "measurements": results,
}
Path(__file__).with_name("benchmark-results.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=True))
