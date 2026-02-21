# 💻 ML Futurisys – Attrition Prediction API

![Python](https://img.shields.io/badge/Python-3.12.7-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Local-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-3.0.4-orange)
![Pytest](https://img.shields.io/badge/Tests-Pytest%207.4.4-green)
[![Test and Deploy API](https://github.com/masala-hadziavdic/Projet5-ML-deployment-for-Futurisys-/actions/workflows/deploy.yml/badge.svg)](https://github.com/masala-hadziavdic/Projet5-ML-deployment-for-Futurisys-/actions/workflows/deploy.yml)

---

## 🔗 Liens du projet

- 🌐 **Hugging Face Space** : https://huggingface.co/spaces/amely188/ml-futurisys  
- 💻 **GitHub Repository** : https://github.com/masala-hadziavdic/Projet5-ML-deployment-for-Futurisys

---

## 📌 Table des matières

- [À propos du projet](#-à-propos-du-projet)  
- [Architecture](#-architecture)  
- [Schéma de base de données (UML)](#-schéma-uml-de-la-base-de-données)  
- [Stack technique & versions](#-stack-technique--versions)  
- [Installation locale](#-installation-locale)  
- [Initialisation base PostgreSQL](#-initialisation-base-postgresql)  
- [Lancement de l’API](#-lancement-de-lapi)  
- [Exemples d’utilisation](#-exemples-dutilisation)  
- [Tests & qualité](#-tests--qualité)  
- [Traçabilité des prédictions](#-traçabilité-des-prédictions)  
- [Déploiement et CI/CD](#-déploiement-et-cicd)  
- [Auteur](#-auteur)

---

# 📖 À propos du projet

L’API Futurisys ML est une solution de classification automatisée conçue pour analyser et anticiper l’attrition au sein d’une entreprise. Elle s’appuie sur un modèle XGBoost pré-entraîné afin d’estimer la probabilité qu’un employé décide de quitter l’organisation.

| Métrique       | Valeur | Description |
|----------------|--------|------------|
| Accuracy       | 0.7483 | Précision globale sur les données de test |
| F1-Score       | 0.4308 | Équilibre précision / rappel |
| Précision      | 0.3373 | Taux de vrais positifs parmi les prédictions positives |
| Rappel         | 0.5957 | Taux de détection des vrais cas d’attrition |
| True Negatives (TN) | 192 | Nombre de vrais négatifs |
| False Positives (FP) | 55 | Nombre de faux positifs |
| False Negatives (FN) | 19 | Nombre de faux négatifs |
| True Positives (TP) | 28 | Nombre de vrais positifs |


Toutes les interactions avec le modèle passent obligatoirement par PostgreSQL pour :

- ✅ Enregistrement des **inputs**  
- ✅ Enregistrement des **outputs**  
- ✅ Historique complet des prédictions  
- ✅ Audit et traçabilité

---

# 🏗️ Architecture

Client / API  
↓  
`prediction_service.py`  
↓  
`database.py`  
↓  
PostgreSQL  

| Fichier | Rôle |
|----------|------|
| `database.py` | Connexion et gestion DB |
| `prediction_service.py` | Logique métier (insert & retrieve) |
| `test_prediction_service.py` | Tests unitaires Pytest |

---

# 🗄️ Schéma UML de la Base de Données

**Exemple diagramme UML exportable Draw.io / PNG** :

![UML Database](assets/uml_database.png)  
*(Remplace `assets/uml_database.png` par le chemin réel de ton image exportée depuis Draw.io)*

---

# ⚙️ Stack technique & versions

| Technologie | Version |
|------------|---------|
| Python | 3.12.7 (Anaconda) |
| FastAPI | 0.104+ |
| XGBoost | 3.0.4 |
| Pandas | 2.3.3 |
| NumPy | 2.3.4 |
| PostgreSQL | 13+ |
| Psycopg2-binary | 2.9.11 |
| Pytest | 7.4.4 |
| SQLAlchemy | 2.0+ |

---

# 💾 Installation locale

```bash
# Cloner le repo
git clone https://github.com/masala-hadziavdic/Projet5-ML-deployment-for-Futurisys.git
cd Projet5-ML-deployment-for-Futurisys

# Créer environnement Python
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Installer dépendances
pip install --upgrade pip
pip install -r requirements.txt
