from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from typing import List

app = FastAPI(title="ML Model API")

model = joblib.load("app/model/model.pkl")


class PredictionInput(BaseModel):
    features: List[float]


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: PredictionInput):
    features = np.array([data.features])
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}
