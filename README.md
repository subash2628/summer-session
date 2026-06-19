# From Data to Deployment: Python, APIs & ML

**Module:** From Data to Deployment: Python, APIs & ML  
**Programme:** BSc (Hons) Computing with AI — Year 2  
**College:** Islington College  
**Lecturer:** Mr. Subash Sharma  
**Groups:** AI5, AI6, AI7, AI8

---

## Overview

This repository contains all teaching materials for a one-week intensive module. Students build a complete end-to-end machine learning pipeline — from raw data to a live, containerised web service — in four sessions across the week.

```
Titanic dataset  →  Pandas preprocessing  →  Decision Tree model  →  model.pkl
      →  FastAPI (/predict)  →  HTML frontend  →  Docker  →  Docker Compose  →  Nginx  →  AWS EC2
```

---

## Repository Structure

```
summer_session/
├── data/
│   └── PUT_TRAIN_CSV_HERE.txt     # download train.csv from Kaggle and place here
├── notebooks/
│   └── workshop1_preprocessing_model.ipynb   # Workshop 1 — Tasks 1–3
├── api/
│   ├── main.py                    # FastAPI app with /predict endpoint
│   ├── model.pkl                  # trained Decision Tree (max_depth=3, ~80% accuracy)
│   ├── requirements.txt
│   └── static/
│       └── index.html             # HTML form + fetch() frontend
├── nginx/
│   └── nginx.conf                 # reverse proxy config
├── Dockerfile                     # builds the API container
└── docker-compose.yml             # api (nishan9848/summer-project) + nginx (nishan9848/nginx-summer)
```

---

## Dataset

**Titanic — Kaggle Competition:** https://www.kaggle.com/competitions/titanic/data

Download `train.csv` and place it in the `data/` folder before running the notebook.

| Feature | Type | Notes |
|---------|------|-------|
| Pclass | Categorical (ordinal) | 1, 2, 3 |
| Sex | Categorical | male / female → encoded as 0 / 1 |
| Age | Numerical | missing values → imputed with median |
| SibSp | Numerical | siblings/spouses aboard |
| Parch | Numerical | parents/children aboard |
| Fare | Numerical | ticket fare |
| Embarked | Categorical | C / Q / S → encoded as 0 / 1 / 2, missing → mode |

Target: `Survived` (0 = Did Not Survive, 1 = Survived)

---

## Week Schedule

| Session | Day | Duration | Groups | Topic |
|---------|-----|----------|--------|-------|
| Tutorial 1 | Monday 09:00 | 1 hr | AI6 | Data Pipeline Thinking & Preprocessing Concepts |
| Tutorial 2 | Tuesday 09:00 | 1 hr | AI8 | From Model to API to Deployment — Concepts |
| Workshop 1 | Wednesday | 2 hrs | AI6 (Lab 12), AI5 (Lab 11) | Preprocessing, Model Training, Serialization |
| Workshop 2 | Thursday | 2 hrs | AI7 (Lab 08), AI8 (Lab 07) | API, Containerization, Deployment |

---

## Learning Outcomes

By the end of this week, students will be able to:

1. Load and preprocess a tabular dataset using Pandas.
2. Train and evaluate a Decision Tree classifier using scikit-learn.
3. Serialize a trained model using `pickle`.
4. Build a FastAPI service exposing a `/predict` endpoint.
5. Build a simple HTML frontend that collects input and displays the prediction.
6. Containerize the service with Docker and orchestrate it with Docker Compose and Nginx.
7. Deploy the containerised service to an AWS EC2 instance.

---

## Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Jupyter (for the notebook)

### Workshop 1 — Train the model

```bash
# Install dependencies
pip install pandas scikit-learn jupyter

# Place train.csv in data/, then open the notebook
jupyter notebook notebooks/workshop1_preprocessing_model.ipynb
```

Run all cells. This produces `api/model.pkl`.

### Workshop 2 — Run the API locally

```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

- Frontend: http://localhost:8000/static/index.html
- Swagger UI (auto-docs): http://localhost:8000/docs

Sample POST request:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"Pclass":3,"Sex":0,"Age":22,"SibSp":1,"Parch":0,"Fare":7.25,"Embarked":2}'
```

Expected response: `{"survived": false}`

### Workshop 2 — Run with Docker Compose (API + Nginx)

Both services use pre-built Docker Hub images — no local build required.

```bash
docker compose up
```

- Frontend via Nginx: http://localhost
- `/predict` via Nginx: http://localhost/predict

| Service | Image |
|---------|-------|
| API (FastAPI) | `nishan9848/summer-project:latest` |
| Nginx | `nishan9848/nginx-summer:latest` |

---

## API Reference

### `POST /predict`

**Request body (JSON):**

| Field | Type | Description |
|-------|------|-------------|
| Pclass | int | Passenger class: 1, 2, or 3 |
| Sex | int | 0 = male, 1 = female |
| Age | float | Passenger age |
| SibSp | int | Siblings/spouses aboard |
| Parch | int | Parents/children aboard |
| Fare | float | Ticket fare |
| Embarked | int | Port: 0 = Cherbourg, 1 = Queenstown, 2 = Southampton |

**Response:**

```json
{ "survived": true }
```

---

## Architecture

```
Browser
  │
  ▼
Nginx (port 80)
  ├── GET  /          → serves index.html (proxied from FastAPI /static)
  └── POST /predict   → proxied to FastAPI :8000/predict
                              │
                              ▼
                        model.pkl (Decision Tree)
                              │
                              ▼
                      {"survived": true/false}
```

---

## Deployment to AWS EC2

1. Launch an EC2 instance (Amazon Linux 2 or Ubuntu), open ports 22 and 80.
2. Install Docker and Docker Compose on the instance.
3. Copy the project:
   ```bash
   scp -r . ec2-user@<your-ec2-ip>:~/summer_session
   ```
4. SSH in and start the services:
   ```bash
   ssh ubuntu@<your-ec2-ip>
   cd summer_session
   docker compose up -d
   ```
5. Visit `http://<your-ec2-ip>` in a browser.

---

## Assessment Checkpoints

| Checkpoint | Deliverable |
|------------|-------------|
| After Workshop 1 | `model.pkl` + notebook with accuracy score printed |
| After Workshop 2 | Screenshot of `/predict` returning a prediction (local or EC2 URL) |

---

## Facilitators

| Session | Group | Room | Facilitator |
|---------|-------|------|-------------|
| Workshop 1 | AI6 | Lab 12 | Sushant Hona |
| Workshop 1 | AI5 | Lab 11 | Suvan Thapa Magar |
| Workshop 2 | AI7 | Lab 08 | Ronisha Shrestha |
| Workshop 2 | AI8 | Lab 07 | Sonik Das Mulmi |
