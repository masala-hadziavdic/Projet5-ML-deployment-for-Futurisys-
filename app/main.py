from fastapi import FastAPI
import joblib
import pandas as pd
from app.employee_models import EmployeeData

app = FastAPI(title="ML Model API")

# Charger le modèle
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

        # Prédiction
        prediction = model.predict(df)[0]  # récupère 0 ou 1
        proba = model.predict_proba(df)[0]  # [prob_stay, prob_quit] si classifier binaire

        # Transformer en sortie lisible
        result = {
            "prediction": "Oui" if prediction == 1 else "Non",  # 1 = quitte, 0 = reste
            "probability_quit": float(proba[1]),  # probabilité de quitter
            "probability_stay": float(proba[0])   # probabilité de rester
        }

        return result

    except Exception as e:
        return {"error": str(e)}






