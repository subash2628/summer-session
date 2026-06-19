import pickle
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Titanic Survival Predictor")

app.mount("/static", StaticFiles(directory="static"), name="static")


class Passenger(BaseModel):
    Pclass: int       # 1, 2, or 3
    Sex: int          # 0 = male, 1 = female
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: int     # 0 = C, 1 = Q, 2 = S


@app.post("/predict")
def predict(passenger: Passenger):
    features = [[
        passenger.Pclass,
        passenger.Sex,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.Fare,
        passenger.Embarked,
    ]]
    prediction = model.predict(features)[0]
    return {"survived": bool(prediction)}
