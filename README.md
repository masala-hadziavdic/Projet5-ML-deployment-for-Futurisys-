# 💻 ML Futurisys – Attrition Prediction API

🔗 Liens du projet

🌐 Hugging Face Space : https://huggingface.co/spaces/amely188/ml-futurisys

💻 GitHub Repository : https://github.com/masala-hadziavdic/Projet5-ML-deployment-for-Futurisys-

Table des matières

À propos du projet

Architecture

Schéma UML

Stack technique

Installation locale

Initialisation PostgreSQL

Lancement de l’API

Exemple d’utilisation

Tests & qualité

Traçabilité des prédictions

CI/CD & Déploiement

Auteur

---

📖 À propos du projet

L’API Futurisys ML est une solution de classification permettant de prédire l’attrition des employés (probabilité qu’un employé quitte l’entreprise).

Le modèle utilisé est un XGBoost pré-entraîné, exposé via une API FastAPI.

📊 Performances du modèle
Métrique	Valeur
Accuracy	0.7483
F1-Score	0.4308
Précision	0.3373
Rappel	0.5957
TN	192
FP	55
FN	19
TP	28
🎯 Objectifs du projet

Exposer un modèle ML via une API REST

Enregistrer toutes les prédictions en base PostgreSQL

Assurer la traçabilité complète

Mettre en place un pipeline CI/CD

Déployer automatiquement sur Hugging Face Spaces

🏗️ Architecture
Client
   ↓
FastAPI (app/main.py)
   ↓
prediction_service.py
   ↓
database.py
   ↓
PostgreSQL
📂 Rôle des fichiers principaux
Fichier	Description
app/main.py	Point d’entrée FastAPI
prediction_service.py	Logique métier
database.py	Connexion et gestion PostgreSQL
model.pkl	Modèle XGBoost
test_prediction_service.py	Tests unitaires
🗄️ Schéma UML de la Base de Données

Diagramme UML (à placer dans assets/uml_database.png) :

![UML Database](assets/uml_database.png)
⚙️ Stack technique & versions
Technologie	Version
Python	3.12
FastAPI	0.104+
XGBoost	3.0.4
Pandas	2.3+
NumPy	2.3+
PostgreSQL	13+
Psycopg2	2.9+
SQLAlchemy	2.0+
Pytest	7.4+
GitHub Actions	CI/CD
Hugging Face Spaces	Déploiement
💾 Installation locale
# Cloner le repository
git clone https://github.com/masala-hadziavdic/Projet5-ML-deployment-for-Futurisys-.git
cd Projet5-ML-deployment-for-Futurisys-

# Créer environnement virtuel
python -m venv venv

# Activation Windows
venv\Scripts\activate

# Activation Linux/macOS
source venv/bin/activate

# Installer dépendances
pip install --upgrade pip
pip install -r requirements.txt
🐘 Initialisation PostgreSQL

Créer une base :

CREATE DATABASE futurisys;

Configurer les variables d’environnement :

DB_HOST=localhost
DB_PORT=5432
DB_NAME=futurisys
DB_USER=postgres
DB_PASSWORD=your_password
🚀 Lancement de l’API
uvicorn app.main:app --reload

Documentation Swagger disponible à :

http://127.0.0.1:8000/docs
📬 Exemple d’utilisation
POST /predict
{
  "prediction": "Non",
  "probability_quit": 0.0962093397974968,
  "probability_stay": 0.9037906527519226
}


🧪 Tests & qualité

Lancer les tests :

pytest

Les tests vérifient :

Chargement du modèle

Validation du schéma d’entrée

Insertion en base

Récupération des prédictions

📊 Traçabilité des prédictions

Chaque prédiction est stockée en base PostgreSQL :

Inputs utilisateur

Score de probabilité

Classe prédite

Timestamp

Cela garantit :

Auditabilité

Historique complet

Analyse future des performances

🔁 CI/CD & Déploiement

Pipeline GitHub Actions :

Exécution des tests

Vérification du chargement FastAPI

Déploiement automatique vers Hugging Face Space

Déploiement automatique vers :

👉 https://huggingface.co/spaces/amely188/ml-futurisys

👩‍💻 Auteur

Support et contact
Auteur : masala-hadziavdic (amela188@hotmail.com)
Projet : Formation Data Scientist Machine Learning - OpenClassrooms
Repository : GitHub
Démo live : Hugging Face Spaces
Projet réalisé dans le cadre du déploiement d’une solution Machine Learning avec CI/CD et infrastructure PostgreSQL.