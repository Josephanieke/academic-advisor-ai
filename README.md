# Academic Advisor AI — CSC 303

An explainable academic-advising web application. It combines software-engineering practices (separation of concerns, validation, automated tests, Git configuration, and documentation) with AI techniques (k-nearest-neighbours classification plus a transparent rule engine).

## What it does

The app receives a student's CGPA, failed/carry-over courses, attendance, study hours, and level. It classifies the student into **High**, **Medium**, or **Low** academic-support priority, then explains the recommendation and gives an action plan.

> The training data is synthetic for demonstration. This project is a decision-support prototype; department advisers retain the final decision.

## Project structure

```
app.py                         # Flask web application / deployment entry point
advisor_model.py                # Explainable k-NN and rule-based AI logic
train_model.py                  # Builds models/academic_advisor_model.pkl
models/academic_advisor_model.pkl # Serialized, deployable model
templates/index.html            # Web user interface
static/style.css                # Responsive styling
tests/test_advisor.py           # Automated tests
Academic_Advisor_Colab.ipynb    # Colab-ready training notebook
```

## Run locally in VS Code

1. Open this folder in VS Code. Accept the recommended Python, Pylance, Jupyter, and Black extensions.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate       # macOS/Linux
   # .venv\Scripts\activate        # Windows PowerShell
   ```

3. Install the framework, generate the model, test, and start the web app:

   ```bash
   pip install -r requirements.txt
   python train_model.py
   python -m unittest discover -s tests -v
   flask --app app run --debug
   ```

4. Visit `http://127.0.0.1:5000` in a browser.

## Google Colab workflow

1. Upload `Academic_Advisor_Colab.ipynb` to [Google Colab](https://colab.research.google.com/).
2. Run every cell. The final cell downloads `academic_advisor_model.pkl`.
3. Place that downloaded file in `models/` and run the Flask app. This demonstrates the model was built in Colab and deployed locally.

## Git and GitHub checklist

Git is installed when `git --version` shows a version number. From this project folder:

```bash
git init
git add .
git commit -m "Build academic advisor AI web application"
```

Create an empty repository on GitHub, then connect and publish it:

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/academic-advisor-ai.git
git push -u origin main
```

If GitHub CLI is installed and authenticated, the alternative is:

```bash
gh repo create academic-advisor-ai --public --source=. --remote=origin --push
```

## Evidence for assessment

- **Standard engineering:** modular code, form validation, test cases, `.gitignore`, dependency file, VS Code configuration, and documentation.
- **AI techniques:** feature normalisation, k-NN classification, a serialized `.pkl` model, and explainable recommendation rules.
- **Deployment:** Flask serves the model-driven web application.
