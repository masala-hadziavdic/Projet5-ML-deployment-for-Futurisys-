"""
Model pour validation des données
API de prédiction d'attrition des employés - Futurisys
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict
from datetime import datetime
from enum import Enum

# ================================
# ENUMS
# ================================

class HeuresSupplementaires(str, Enum):
    OUI = "Oui"
    NON = "Non"

class Genre(str, Enum):
    HOMME = "Homme"
    FEMME = "Femme"

class StatutMarital(str, Enum):
    CELIBATAIRE = "Célibataire"
    MARIE = "Marié(e)"
    DIVORCE = "Divorcé(e)"

class Departement(str, Enum):
    COMMERCIAL = "Commercial"
    CONSULTING = "Consulting"
    RH = "Ressources Humaines"

class DomaineEtude(str, Enum):
    INFRA_CLOUD = "Infra & Cloud"
    AUTRE = "Autre"
    TRANSFORMATION = "Transformation Digitale"
    MARKETING = "Marketing"
    ENTREPRENEURIAT = "Entrepreneuriat"
    RH = "Ressources Humaines"

class FrequenceDeplacement(str, Enum):
    FREQUENT = "Voyage_Fréquent"
    RARE = "Voyage_Rare"
    AUCUN = "Aucun"

# ================================
# INPUT MODEL
# ================================

class EmployeeData(BaseModel):
    """Données d'entrée pour la prédiction"""

    satisfaction_employee_environnement: int = Field(..., ge=1, le=4)
    satisfaction_employee_nature_travail: int = Field(..., ge=1, le=4)
    satisfaction_employee_equipe: int = Field(..., ge=1, le=4)
    satisfaction_employee_equilibre_pro_perso: int = Field(..., ge=1, le=4)

    note_evaluation_precedente: int = Field(..., ge=1, le=4)
    note_evaluation_actuelle: int = Field(..., ge=1, le=4)

    niveau_hierarchique_poste: int = Field(..., ge=1, le=5)

    heure_supplementaires: HeuresSupplementaires

    augementation_salaire_precedente: float = Field(..., ge=0.0, le=1.0)

    age: int = Field(..., ge=18, le=65)
    genre: Genre
    revenu_mensuel: int = Field(..., ge=1000, le=50000)
    statut_marital: StatutMarital

    departement: Departement

    nombre_experiences_precedentes: int = Field(..., ge=0, le=20)
    annee_experience_totale: int = Field(..., ge=0, le=40)
    annees_dans_l_entreprise: int = Field(..., ge=0, le=30)
    annees_dans_le_poste_actuel: int = Field(..., ge=0, le=20)
    annees_depuis_la_derniere_promotion: int = Field(..., ge=0, le=15)

    nombre_participation_pee: int = Field(..., ge=0, le=3)
    nb_formations_suivies: int = Field(..., ge=0, le=6)

    distance_domicile_travail: int = Field(..., ge=0, le=100)

    niveau_education: int = Field(..., ge=1, le=5)
    domaine_etude: DomaineEtude

    frequence_deplacement: FrequenceDeplacement

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
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
                "frequence_deplacement": "Voyage_Rare"
            }
        }
    )

# ================================
# OUTPUT MODEL
# ================================

class PredictionResult(BaseModel):
    prediction: str
    probability_quit: float
    probability_stay: float
    confidence_level: str
    timestamp: datetime = Field(default_factory=datetime.now)

# ================================
# ERROR RESPONSE
# ================================

class ErrorResponse(BaseModel):
    error: str
    message: str
    details: Optional[Dict] = None
    timestamp: datetime = Field(default_factory=datetime.now)