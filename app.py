"""Flask deployment for the CSC 303 Academic Advisor System."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Dict

from flask import Flask, render_template, request

MODEL_PATH = Path(__file__).parent / "models" / "academic_advisor_model.pkl"


def load_model():
    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


app = Flask(__name__)
model = load_model()


def parse_student(form) -> Dict[str, float]:
    """Validate browser form input before it reaches the advisory model."""
    student = {
        "gpa": float(form["gpa"]),
        "failed_courses": int(form["failed_courses"]),
        "attendance": float(form["attendance"]),
        "hours_per_week": float(form["hours_per_week"]),
        "level": int(form["level"]),
    }
    if not 0 <= student["gpa"] <= 5:
        raise ValueError("CGPA must be between 0.00 and 5.00.")
    if not 0 <= student["failed_courses"] <= 6:
        raise ValueError("Failed/carry-over courses must be between 0 and 6.")
    if not 0 <= student["attendance"] <= 100:
        raise ValueError("Attendance must be between 0 and 100%.")
    if not 0 <= student["hours_per_week"] <= 40:
        raise ValueError("Study hours must be between 0 and 40 per week.")
    if student["level"] not in {100, 200, 300, 400, 500}:
        raise ValueError("Choose a valid level.")
    return student


@app.route("/", methods=["GET", "POST"])
def index():
    advice = error = None
    submitted = request.form.to_dict()
    if request.method == "POST":
        try:
            advice = model.advise(parse_student(request.form))
        except (KeyError, TypeError, ValueError) as exc:
            error = str(exc)
    return render_template("index.html", advice=advice, error=error, submitted=submitted)


if __name__ == "__main__":
    app.run(debug=True)
