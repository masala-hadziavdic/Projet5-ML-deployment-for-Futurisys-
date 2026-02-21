"""
API de prédiction d'attrition des employés - Futurisys
"""

from fastapi import FastAPI
import joblib
import pandas as pd
import os
from app.employee_models import EmployeeData, PredictionResult, ErrorResponse

app = FastAPI(title="ML Employee Attrition API")

# ================================
# Charger le pipeline complet (préprocessing + modèle)
# ================================
pipeline_path = os.path.join(os.path.dirname(__file__), "model", "pipeline.pkl")
pipeline = None

if not os.path.exists(pipeline_path):
    print(f"⚠️ Pipeline non trouvé à l'emplacement: {pipeline_path}")
    print("API fonctionnera avec un mock")
else:
    try:
        pipeline = joblib.load(pipeline_path)
        print(f"✅ Pipeline chargé depuis {pipeline_path}")
    except Exception as e:
        pipeline = None
        print(f"❌ Erreur lors du chargement du pipeline: {e}")

# ================================
# Endpoints
# ================================

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict", response_model=PredictionResult, responses={400: {"model": ErrorResponse}})
def predict(data: EmployeeData):
    """Prédit le risque d'attrition pour un employé"""
    if pipeline is None:
        # Mock si le pipeline n'est pas disponible
        return PredictionResult(
            prediction="Non",
            probability_quit=0.3,
            probability_stay=0.7,
            confidence_level="Medium"
        )

    try:
        # Convertir l'objet Pydantic en DataFrame
        df = pd.DataFrame([data.model_dump()])

        # Prédiction
        prediction = pipeline.predict(df)[0]
        proba = pipeline.predict_proba(df)[0]

        # Calcul du niveau de confiance
        confidence_level = (
            "High" if proba[1] > 0.7 else "Medium" if proba[1] > 0.3 else "Low"
        )

        return PredictionResult(
            prediction="Oui" if prediction == 1 else "Non",
            probability_quit=float(proba[1]),
            probability_stay=float(proba[0]),
            confidence_level=confidence_level
        )

    except Exception as e:
        # Gestion des erreurs
        return ErrorResponse(
            error="PredictionError",
            message=str(e),
            details={"input_data": data.model_dump()}
        )