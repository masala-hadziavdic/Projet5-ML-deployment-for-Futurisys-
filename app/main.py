from fastapi import FastAPI
import joblib
import pandas as pd
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
    try:
        columns = [
            "age",
            "genre",
            "revenu_mensuel",
            "statut_marital",
            "departement",
            "nombre_experiences_precedentes",
            "annees_dans_l_entreprise",
            "nombre_participation_pee",
            "nb_formations_suivies",
            "distance_domicile_travail",
            "niveau_education",
            "domaine_etude",
            "frequence_deplacement",
            "annees_depuis_la_derniere_promotion",
            "satisfaction_employee_environnement",
            "note_evaluation_precedente",
            "satisfaction_employee_nature_travail",
            "satisfaction_employee_equipe",
            "satisfaction_employee_equilibre_pro_perso",
            "note_evaluation_actuelle",
            "augementation_salaire_precedente"
        ]

        features = pd.DataFrame([data.features], columns=columns)

        prediction = model.predict(features)

        return {"prediction": prediction.tolist()}

    except Exception as e:
        return {"error": str(e)}




