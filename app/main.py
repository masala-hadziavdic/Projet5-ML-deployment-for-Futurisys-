# app/main.py
from fastapi import FastAPI
import joblib
import pandas as pd
from app.employee_models import EmployeeData
import os

app = FastAPI(title="ML Model API")

# --- Charger le modèle seulement si le fichier existe ---
model_path = "app/model/model.pkl"
if os.getenv("CI") == "true" or not os.path.exists(model_path):
    model = None
    print("⚠️ Modèle non chargé (CI ou fichier manquant)")
else:
    try:
        model = joblib.load(model_path)
        print(f"✅ Modèle chargé depuis {model_path}")
    except Exception as e:
        model = None
        print(f"❌ Erreur lors du chargement du modèle: {e}")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: EmployeeData):
    if model is None:
        return {"error": "Model not loaded"}

    try:
        # Convertir input en dictionnaire
        input_dict = data.model_dump()
        df = pd.DataFrame([input_dict])

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








