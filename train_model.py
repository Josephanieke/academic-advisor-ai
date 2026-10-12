"""Train and save the Academic Advisor model as a deployable .pkl file."""

from __future__ import annotations

import pickle
from pathlib import Path

from advisor_model import AcademicAdvisorModel


# Illustrative, synthetic training cases.  No real student data is used.
TRAINING_DATA = [
    {"gpa": 1.20, "failed_courses": 4, "attendance": 45, "hours_per_week": 4, "level": 200, "priority": "High"},
    {"gpa": 1.55, "failed_courses": 3, "attendance": 62, "hours_per_week": 6, "level": 300, "priority": "High"},
    {"gpa": 1.80, "failed_courses": 2, "attendance": 70, "hours_per_week": 8, "level": 100, "priority": "High"},
    {"gpa": 2.10, "failed_courses": 2, "attendance": 68, "hours_per_week": 7, "level": 200, "priority": "High"},
    {"gpa": 2.35, "failed_courses": 1, "attendance": 72, "hours_per_week": 9, "level": 300, "priority": "Medium"},
    {"gpa": 2.50, "failed_courses": 1, "attendance": 76, "hours_per_week": 12, "level": 400, "priority": "Medium"},
    {"gpa": 2.72, "failed_courses": 0, "attendance": 74, "hours_per_week": 10, "level": 200, "priority": "Medium"},
    {"gpa": 2.90, "failed_courses": 1, "attendance": 82, "hours_per_week": 14, "level": 100, "priority": "Medium"},
    {"gpa": 3.20, "failed_courses": 0, "attendance": 80, "hours_per_week": 14, "level": 300, "priority": "Low"},
    {"gpa": 3.45, "failed_courses": 0, "attendance": 85, "hours_per_week": 16, "level": 400, "priority": "Low"},
    {"gpa": 3.70, "failed_courses": 0, "attendance": 90, "hours_per_week": 20, "level": 200, "priority": "Low"},
    {"gpa": 4.30, "failed_courses": 0, "attendance": 94, "hours_per_week": 24, "level": 500, "priority": "Low"},
]


def build_model(output_path: Path | None = None) -> Path:
    model = AcademicAdvisorModel(k=5).fit(TRAINING_DATA)
    destination = output_path or Path(__file__).parent / "models" / "academic_advisor_model.pkl"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as model_file:
        pickle.dump(model, model_file)
    return destination


if __name__ == "__main__":
    saved_to = build_model()
    print(f"Model saved to {saved_to}")
