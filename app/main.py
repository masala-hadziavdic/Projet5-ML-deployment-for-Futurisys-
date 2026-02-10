from fastapi import FastAPI
import joblib
import pandas as pd
from app.employee_models import EmployeeData
import os

app = FastAPI(title="ML Model API")

# Charger le modèle
if os.getenv("CI") == "true":
    model = None
else:
    model = joblib.load("app/model/model.pkl")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: EmployeeData):
    try:
        # Convertir input en dictionnaire
        input_dict = data.model_dump()
        df = pd.DataFrame([input_dict])

        # Vérifier que le modèle existe
        if model is None:
            return {"error": "Model not loaded"}

        # Prédiction
        prediction = model.predict(df)[0]
        proba = model.predict_proba(df)[0]

        result = {
            "prediction": "Oui" if prediction == 1 else "Non",
            "probability_quit": float(proba[1]),
            "probability_stay": float(proba[0])
        }

        return result

    except Exception as e:
        return {"error": str(e)}







