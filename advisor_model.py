"""Lightweight, explainable AI model used by the Academic Advisor app.

The model combines a small k-nearest-neighbours classifier with transparent
academic rules.  It deliberately has no heavy training dependency, so the
same model can be trained in Google Colab and deployed with Flask.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Any, Dict, Iterable, List, Tuple


FEATURES = ("gpa", "failed_courses", "attendance", "hours_per_week", "level")


@dataclass
class AcademicAdvisorModel:
    """An explainable k-NN classifier for academic-support priority."""

    k: int = 5
    training_data: List[Dict[str, float]] | None = None

    def fit(self, records: Iterable[Dict[str, float]]) -> "AcademicAdvisorModel":
        self.training_data = [dict(record) for record in records]
        if not self.training_data:
            raise ValueError("Training data cannot be empty.")
        return self

    @staticmethod
    def _normalise(student: Dict[str, float]) -> Tuple[float, float, float, float, float]:
        """Scale mixed academic inputs to comparable 0-1 ranges."""
        return (
            float(student["gpa"]) / 5.0,
            float(student["failed_courses"]) / 6.0,
            float(student["attendance"]) / 100.0,
            float(student["hours_per_week"]) / 40.0,
            float(student["level"]) / 500.0,
        )

    def _nearest(self, student: Dict[str, float]) -> List[Dict[str, float]]:
        if not self.training_data:
            raise ValueError("Model has not been trained.")
        target = self._normalise(student)

        def distance(record: Dict[str, float]) -> float:
            values = self._normalise(record)
            return sqrt(sum((a - b) ** 2 for a, b in zip(target, values)))

        return sorted(self.training_data, key=distance)[: min(self.k, len(self.training_data))]

    def predict_priority(self, student: Dict[str, float]) -> Tuple[str, float]:
        """Return support priority and the neighbour-agreement percentage."""
        neighbours = self._nearest(student)
        labels = [str(record["priority"]) for record in neighbours]
        priority = max(set(labels), key=labels.count)
        confidence = round((labels.count(priority) / len(labels)) * 100, 1)
        return priority, confidence

    def advise(self, student: Dict[str, float]) -> Dict[str, Any]:
        """Combine machine-learning classification and pedagogical rules."""
        priority, confidence = self.predict_priority(student)
        actions: List[str] = []
        reasons: List[str] = []
        gpa = float(student["gpa"])
        failed = int(student["failed_courses"])
        attendance = float(student["attendance"])
        hours = float(student["hours_per_week"])

        if gpa < 2.0:
            actions.append("Book an academic-advising meeting this week.")
            reasons.append("Your CGPA is below 2.00 and needs immediate recovery planning.")
        elif gpa < 3.0:
            actions.append("Meet your course adviser before course registration closes.")
            reasons.append("A structured improvement plan can help raise your CGPA.")
        else:
            actions.append("Maintain your study routine and choose courses that support your career goal.")
            reasons.append("Your current CGPA shows a stable academic foundation.")

        if failed >= 2:
            actions.append("Prioritise carry-over courses and use the departmental tutorial sessions.")
            reasons.append(f"You reported {failed} failed/carry-over course(s).")
        if attendance < 75:
            actions.append("Raise class attendance to at least 75% and speak with lecturers early.")
            reasons.append("Attendance is below the recommended 75% threshold.")
        if hours < 10:
            actions.append("Create a weekly timetable with at least 10 focused study hours.")
            reasons.append("Your independent-study time is currently limited.")

        study_plan = ""
        if priority == "High":
            study_plan = "Use a recovery plan: daily revision blocks, weekly adviser check-ins, and peer tutoring."
        elif priority == "Medium":
            study_plan = "Use a growth plan: protect two revision sessions per course every week and track quizzes."
        else:
            study_plan = "Use an enrichment plan: sustain your routine and add a portfolio, internship, or research goal."

        return {
            "priority": priority,
            "confidence": confidence,
            "actions": actions,
            "reasons": reasons,
            "study_plan": study_plan,
        }
