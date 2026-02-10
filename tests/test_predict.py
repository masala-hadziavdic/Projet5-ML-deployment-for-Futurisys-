from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Payload exemple valide correspondant exactement aux champs de EmployeeData
sample_employee_data = {
    "age": 35,
    "genre": "Homme",
    "revenu_mensuel": 4500.0,
    "statut_marital": "Marié(e)",
    "departement": "Consulting",
    "nombre_experiences_precedentes": 3,
    "annees_dans_l_entreprise": 5,
    "nombre_participation_pee": 2,
    "nb_formations_suivies": 4,
    "distance_domicile_travail": 8,
    "niveau_education": 5,
    "domaine_etude": "Marketing",
    "frequence_deplacement": "Rare",
    "annees_depuis_la_derniere_promotion": 2,
    "satisfaction_employee_environnement": 4,
    "note_evaluation_precedente": 4,
    "satisfaction_employee_nature_travail": 4,
    "satisfaction_employee_equipe": 3,
    "satisfaction_employee_equilibre_pro_perso": 4,
    "note_evaluation_actuelle": 4,
    "augementation_salaire_precedente": 0.18
}

def test_home():
    """Test de l’endpoint racine '/'"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_predict_endpoint():
    """Test de l’endpoint POST '/predict'"""
    response = client.post("/predict", json=sample_employee_data)
    assert response.status_code == 200

    data = response.json()
    assert "prediction" in data
    assert "probability_quit" in data
    assert "probability_stay" in data

    # Vérifie que la prédiction renvoie "Oui" ou "Non"
    assert data["prediction"] in ["Oui", "Non"]

    # Vérifie que les probabilités sont entre 0 et 1
    assert 0.0 <= data["probability_quit"] <= 1.0
    assert 0.0 <= data["probability_stay"] <= 1.0
