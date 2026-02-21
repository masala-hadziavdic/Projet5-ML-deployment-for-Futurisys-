"""
API de prédiction d'attrition des employés - Futurisys
Prêt pour Hugging Face Spaces
"""

from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import os
from pydantic import BaseModel
from typing import Optional

# ================================
# Définir les modèles Pydantic
# ================================

class EmployeeData(BaseModel):
    age: int
    annee_experience_totale: int
    annees_dans_l_entreprise: int
    annees_dans_le_poste_actuel: int
    annees_depuis_la_derniere_promotion: int
    augementation_salaire_precedente: float
    departement: str
    distance_domicile_travail: int
    domaine_etude: str
    frequence_deplacement: str
    genre: str
    heure_supplementaires: str
    nb_formations_suivies: int
    niveau_education: int
    niveau_hierarchique_poste: int
    nombre_experiences_precedentes: int
    nombre_participation_pee: int
    note_evaluation_actuelle: int
    note_evaluation_precedente: int
    revenu_mensuel: float
    satisfaction_employee_environnement: int
    satisfaction_employee_equilibre_pro_perso: int
    satisfaction_employee_equipe: int
    satisfaction_employee_nature_travail: int
    statut_marital: str

class PredictionResult(BaseModel):
    prediction: str
    probability_quit: float
    probability_stay: float
    confidence_level: str

class ErrorResponse(BaseModel):
    error: str
    message: str
    details: Optional[dict] = None

# ================================
# Initialiser FastAPI
# ================================

app = FastAPI(title="ML Employee Attrition API")

# ================================
# Charger le pipeline complet
# ================================

pipeline_path = os.path.join(os.path.dirname(__file__), "model", "pipeline.pkl")
pipeline = None

if not os.path.exists(pipeline_path):
    print(f"⚠️ Pipeline non trouvé: {pipeline_path}. L'API utilisera un mock.")
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

@app.post("/predict", response_model=PredictionResult)
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
        # Compatible Pydantic v1/v2
        if hasattr(data, "model_dump"):
            df = pd.DataFrame([data.model_dump()])
        else:
            df = pd.DataFrame([data.dict()])

        # Prédiction
        prediction = pipeline.predict(df)[0]

        # Probabilité
        if hasattr(pipeline, "predict_proba"):
            proba = pipeline.predict_proba(df)[0]
        else:
            # approximation si pas de predict_proba
            proba = [1 - prediction, prediction]

        # Niveau de confiance
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
        raise HTTPException(
            status_code=400,
            detail={"error": "PredictionError", "message": str(e), "input_data": data.dict()}
        )