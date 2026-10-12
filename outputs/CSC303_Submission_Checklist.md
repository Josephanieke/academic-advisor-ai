# CSC 303 Submission Checklist

## Project title

**Academic Advisor AI: An Explainable Student Decision-Support System**

## Demonstration flow

1. Open the project in VS Code and show the recommended Python extensions.
2. In the terminal, run `git log --oneline` after making the first commit.
3. Open `Academic_Advisor_Colab.ipynb` in Google Colab and run the cells that create `academic_advisor_model.pkl`.
4. Place the model in `models/academic_advisor_model.pkl` (already included in this project).
5. Run the Flask app and open `http://127.0.0.1:5000`.
6. Enter a sample profile such as CGPA `1.40`, failed courses `3`, attendance `55`, study hours `5`, and level `200`.
7. Explain that the AI classifies support priority with k-nearest neighbours, then applies transparent rules to explain the recommendation.
8. Run the automated test command and show that all tests pass.

## Commands to show

```bash
source .venv/bin/activate
python -m unittest discover -s tests -v
flask --app app run --debug
```

## Requirement coverage

| Assignment requirement | Evidence in this submission |
| --- | --- |
| Git | Local repository initialized; `.gitignore` and version-ready source files included. |
| GitHub | `README.md` contains the remote publishing commands; publish under your own GitHub account. |
| Repository | The project folder is a Git repository on the `main` branch. |
| Python-optimised VS Code | `.vscode/extensions.json` recommends Python, Pylance, Jupyter, and Black; `launch.json` debugs Flask. |
| Google Colab model | `Academic_Advisor_Colab.ipynb` trains and downloads the `.pkl` model. |
| `.pkl` deployment | `models/academic_advisor_model.pkl` is loaded by `app.py` and served through Flask. |
| Web-app testing | `tests/test_advisor.py` tests model advice, valid form submission, and invalid input. |

## Important note for the presentation

The project uses **synthetic sample records**, not real student records. It is an explainable decision-support prototype: the model assists an academic adviser and does not make final academic decisions.
