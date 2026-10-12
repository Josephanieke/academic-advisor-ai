"""Automated checks for model behaviour and the Flask web interface."""

import unittest

from app import app, model


class AdvisorSystemTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_high_risk_student_gets_high_priority(self):
        result = model.advise(
            {"gpa": 1.4, "failed_courses": 3, "attendance": 55, "hours_per_week": 5, "level": 200}
        )
        self.assertEqual(result["priority"], "High")
        self.assertTrue(result["actions"])

    def test_web_form_returns_advice(self):
        response = self.client.post(
            "/",
            data={"gpa": "3.5", "failed_courses": "0", "attendance": "90", "hours_per_week": "18", "level": "300"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recommended priority", response.data)

    def test_web_form_validates_gpa(self):
        response = self.client.post(
            "/",
            data={"gpa": "7", "failed_courses": "0", "attendance": "90", "hours_per_week": "18", "level": "300"},
        )
        self.assertIn(b"CGPA must be between", response.data)


if __name__ == "__main__":
    unittest.main()
