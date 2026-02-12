from fastapi import FastAPI
import joblib
import pandas as pd
from app.employee_models import EmployeeData
import os

app = FastAPI(title="ML Model API")

# --- Charger le pipeline complet (préprocessing + modèle)
pipeline_path = "app/model/pipeline.pkl"
pipeline = None

if not os.path.exists(pipeline_path):
    print("⚠️ Pipeline non trouvé, API fonctionnera avec un mock")
else:
    try:
        pipeline = joblib.load(pipeline_path)
        print(f"✅ Pipeline chargé depuis {pipeline_path}")
    except Exception as e:
        pipeline = None
        print(f"❌ Erreur lors du chargement du pipeline: {e}")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: EmployeeData):
    # Mode fallback si pipeline absent
    if pipeline is None:
        return {
            "prediction": "Non",
            "probability_quit": 0.3,
            "probability_stay": 0.7
        }

    try:
        input_dict = data.model_dump()
        df = pd.DataFrame([input_dict])

        prediction = pipeline.predict(df)[0]
        proba = pipeline.predict_proba(df)[0]

        return {
            "prediction": "Oui" if prediction == 1 else "Non",
            "probability_quit": float(proba[1]),
            "probability_stay": float(proba[0])
        }

    except Exception as e:
        return {"error": str(e)}
