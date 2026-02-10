from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Exemple minimal de payload valide pour EmployeeData
sample_employee_data = {
    "satisfaction_employee_environnement": 4,
    "satisfaction_employee_nature_travail": 4,
    "satisfaction_employee_equipe": 3,
    "satisfaction_employee_equilibre_pro_perso": 4,
    "note_evaluation_precedente": 4,
    "note_evaluation_actuelle": 4,
    "niveau_hierarchique_poste": 3,
    "heure_supplementaires": "Non",
    "augementation_salaire_precedente": 0.18,
    "age": 35,
    "genre": "Homme",
    "revenu_mensuel": 4500,
    "statut_marital": "Marié(e)",
    "departement": "Consulting",
    "nombre_experiences_precedentes": 3,
    "annee_experience_totale": 12,
    "annees_dans_l_entreprise": 5,
    "annees_dans_le_poste_actuel": 3,
    "annees_depuis_la_derniere_promotion": 2,
    "nombre_participation_pee": 2,
    "nb_formations_suivies": 4,
    "distance_domicile_travail": 8,
    "niveau_education": 5,
    "domaine_etude": "Marketing",
    "frequence_deplacement": "Rare"
}

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}

def test_predict_endpoint():
    response = client.post("/predict", json=sample_employee_data)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    # Vérifie que la prédiction renvoie soit "Oui" soit "Non"
    assert data["prediction"][0] in ["Oui", "Non"]
