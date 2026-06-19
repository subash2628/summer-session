import pickle
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, field_validator
from typing import Literal

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Titanic Survival Predictor")

app.mount("/static", StaticFiles(directory="static"), name="static")


class Passenger(BaseModel):
    Pclass:   Literal[1, 2, 3]          # first, second, third
    Sex:      Literal[0, 1]             # 0 = male, 1 = female
    Age:      float                     # 0.42 – 80 (dataset range)
    SibSp:    int                       # 0 – 8
    Parch:    int                       # 0 – 6
    Fare:     float                     # 0 – 512.33
    Embarked: Literal[0, 1, 2]         # 0 = C, 1 = Q, 2 = S

    @field_validator("Age")
    @classmethod
    def age_in_range(cls, v):
        if not (0.42 <= v <= 80):
            raise ValueError("Age must be between 0.42 and 80")
        return v

    @field_validator("SibSp")
    @classmethod
    def sibsp_in_range(cls, v):
        if not (0 <= v <= 8):
            raise ValueError("SibSp must be between 0 and 8")
        return v

    @field_validator("Parch")
    @classmethod
    def parch_in_range(cls, v):
        if not (0 <= v <= 6):
            raise ValueError("Parch must be between 0 and 6")
        return v

    @field_validator("Fare")
    @classmethod
    def fare_in_range(cls, v):
        if not (0 <= v <= 512.33):
            raise ValueError("Fare must be between 0 and 512.33")
        return v


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
