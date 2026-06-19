# Weekly Session Plan
**Module:** From Data to Deployment: Python, APIs & ML [SUM]
**Year/Specialization:** BSc (Hons) Computing with AI — Year 2
**Lecturer:** Mr. Subash Sharma
**Groups:** AI5, AI6, AI7, AI8
**Total Contact Time:** 6 hours (2 Tutorials × 1hr + 2 Workshops × 2hr)

## Pipeline Covered This Week
Dataset → Preprocessing (Pandas) → Decision Tree Model → Save model.pkl → FastAPI (/predict) → Frontend (HTML form) → Docker → Docker Compose → Nginx → AWS EC2

## Dataset
**Titanic — Kaggle Competition** (https://www.kaggle.com/competitions/titanic)
Target: `Survived` (0/1, binary classification)

| Feature | Type | Notes |
|---------|------|-------|
| Pclass | Categorical (ordinal) | 1, 2, 3 |
| Sex | Categorical | male/female → encode |
| Age | Numerical | has missing values → impute |
| SibSp | Numerical | siblings/spouses aboard |
| Parch | Numerical | parents/children aboard |
| Fare | Numerical | ticket fare |
| Embarked | Categorical | C/Q/S → encode, has missing values |

Dropped/unused: `PassengerId`, `Name`, `Ticket`, `Cabin` (high cardinality / mostly missing).

## Frontend Requirement
A single HTML page with:
- Input fields for each feature above (dropdowns for Pclass/Sex/Embarked, number inputs for Age/SibSp/Parch/Fare)
- A **Predict** button that sends the form data to the FastAPI `/predict` endpoint (POST, JSON)
- Displays the returned prediction (Survived / Did Not Survive) on the page without reloading

This frontend is served either as a static file via FastAPI itself (simplest) or as a separate Nginx-served static page that calls the API — covered in Workshop 2.

## Week Learning Outcomes
By the end of this week, students will be able to:
1. Load and preprocess a tabular dataset using Pandas.
2. Train and evaluate a Decision Tree classifier/regressor using scikit-learn.
3. Serialize a trained model using pickle.
4. Build a FastAPI service exposing a `/predict` endpoint that loads the model and returns predictions.
5. Build a simple HTML frontend that collects passenger details and displays the prediction returned by the API.
6. Containerize the API + frontend with Docker, orchestrate with Docker Compose, and front it with Nginx.
7. Deploy the containerized service to an AWS EC2 instance.

---

## TUTORIAL 1 — Monday, 09:00–10:00 (1 hour) | AI6
### Topic: Data Pipeline Thinking & Preprocessing Concepts

| Time | Activity | Mode |
|------|----------|------|
| 0–10 min | Recap: ML lifecycle overview — where does today's work sit in the full pipeline (show the diagram) | Lecture |
| 10–25 min | Dataset selection criteria: structure, target variable, class balance, missing values | Lecture + discussion |
| 25–45 min | Walkthrough: Pandas preprocessing on the **Titanic dataset** — `read_csv`, handling missing `Age`/`Embarked`, encoding `Sex`/`Embarked`/`Pclass`, dropping `Name`/`Ticket`/`Cabin`/`PassengerId`, train-test split | Live coding demo |
| 45–55 min | Intro to Decision Trees: how splits work, entropy/Gini, overfitting risk | Lecture (conceptual, visual) |
| 55–60 min | Q&A + preview of Wednesday's workshop task | Discussion |

**Resources:** Slide deck, sample dataset (e.g., Titanic/Iris-style CSV), Jupyter/Colab notebook (read-only demo).

---

## TUTORIAL 2 — Tuesday, 09:00–10:00 (1 hour) | AI8
### Topic: From Model to API to Deployment — Concepts

| Time | Activity | Mode |
|------|----------|------|
| 0–10 min | Recap Tutorial 1; confirm everyone has dataset + preprocessing steps ready | Discussion |
| 10–20 min | Model persistence: why and how — `pickle.dump()` / `pickle.load()` | Lecture |
| 20–35 min | What is an API? REST basics, why FastAPI (speed, type hints, auto docs) | Lecture + live demo (`/predict` skeleton) |
| 35–45 min | Connecting a frontend to an API: basic HTML form + `fetch()`/JS to call `/predict` and show the result | Lecture + live demo |
| 45–55 min | Deployment concepts: what is Docker (image vs container), why Docker Compose (multi-service orchestration), Nginx as reverse proxy, EC2 as the host | Lecture (diagram-driven) |
| 55–60 min | Walk through full architecture diagram end-to-end; clarify workshop deliverables | Discussion |

**Resources:** Architecture diagram (Dataset → ... → EC2), FastAPI skeleton code, Docker/Nginx diagrams.

---

## WORKSHOP 1 — Wednesday (2 hours) | AI6: 09:00–11:00 (Lab 12) | AI5: 12:00–14:00 (Lab 11)
### Topic: Hands-on — Preprocessing, Model Training, Serialization

| Time | Activity |
|------|----------|
| 0–15 min | Setup check: Python env, install `pandas`, `scikit-learn` |
| 15–60 min | **Task 1:** Load Titanic dataset, drop `PassengerId`/`Name`/`Ticket`/`Cabin`, impute missing `Age` (median) and `Embarked` (mode), encode `Sex`/`Embarked`, split into train/test |
| 60–100 min | **Task 2:** Train a `DecisionTreeClassifier` on `Survived`, evaluate with accuracy/confusion matrix, tune `max_depth` |
| 100–115 min | **Task 3:** Save trained model as `model.pkl` using pickle |
| 115–120 min | Wrap-up: checklist confirmation, submit `model.pkl` + notebook |

**Deliverable:** Working `model.pkl` + preprocessing/training notebook.

**Facilitators:** Sushant Hona (AI6, Lab 12), Suvan Thapa Magar (AI5, Lab 11)

---

## WORKSHOP 2 — Thursday (2 hours) | AI7: 09:00–11:00 (Lab 08) | AI8: 12:00–14:00 (Lab 07)
### Topic: Hands-on — API, Containerization, Deployment

| Time | Activity |
|------|----------|
| 0–10 min | Setup check: Docker installed, FastAPI/uvicorn installed |
| 10–40 min | **Task 1:** Build FastAPI app — load `model.pkl`, define `/predict` POST endpoint accepting Pclass/Sex/Age/SibSp/Parch/Fare/Embarked, test with `/docs` (Swagger UI) |
| 40–65 min | **Task 2:** Build the frontend HTML page — form with dropdowns (Pclass, Sex, Embarked) + number inputs (Age, SibSp, Parch, Fare) + Predict button; use `fetch()` to call `/predict` and display result; serve via FastAPI's `StaticFiles`/`Jinja2Templates` |
| 65–90 min | **Task 3:** Write `Dockerfile`, build image, run container, verify the frontend + `/predict` work end-to-end inside the container |
| 90–105 min | **Task 4:** Write `docker-compose.yml` (API+frontend service + Nginx service), configure Nginx as reverse proxy |
| 105–115 min | **Task 5 (guided demo/where time allows):** Provision/access AWS EC2 instance, copy project, run `docker compose up`, test public endpoint and frontend in browser |
| 115–120 min | Wrap-up: deployment checklist, submission instructions |

**Deliverable:** Dockerized FastAPI service (with working frontend page) running behind Nginx, deployed (or demonstrated) on EC2.

**Facilitators:** Ronisha Shrestha (AI7, Lab 08), Sonik Das Mulmi (AI8, Lab 07)

---

## Assessment / Checkpoint Ideas
- Exit ticket after Workshop 1: submit `model.pkl` with accuracy score.
- Exit ticket after Workshop 2: submit a screenshot of `/predict` returning a prediction (local or EC2).

## Notes for Lecturer
- Workshop 2 is now very tight (API + frontend + Docker + Compose + Nginx + EC2 in 120 min). Consider pre-providing a frontend HTML/JS boilerplate so students adapt rather than write it from scratch, freeing time for the deployment steps.
- Given the 6-hour total, EC2 deployment in Workshop 2 may need to be a guided/shared demo rather than every student independently provisioning an instance, due to time and AWS account/cost constraints — consider a pre-provisioned shared instance or instructor walkthrough with student-side practice on Docker Compose only.
- Pre-share the Titanic dataset (train.csv) before Tutorial 1 so Workshop 1 isn't lost to download/setup time.
