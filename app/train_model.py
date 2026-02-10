# app/train_model.py
import os
import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

# ---- Créer dossier model ----
os.makedirs("app/model", exist_ok=True)

# ---- Charger données ----
df_rh = pd.read_csv("extrait_sirh.csv")
df_sondage = pd.read_csv("extrait_sondage.csv")
df_eval = pd.read_csv("extrait_eval.csv")

# ---- Correction colonne evaluation ----
df_eval['eval_number'] = df_eval['eval_number'].apply(
    lambda x: int(x.split('_')[1])
)

# ---- Merge correct ----
df_joint = pd.merge(
    df_rh,
    df_sondage,
    left_on='id_employee',
    right_on='code_sondage',
    how='inner'
)

df_joint = pd.merge(
    df_joint,
    df_eval,
    right_on='eval_number',
    left_on='code_sondage',
    how='inner'
)

# ---- Nettoyer cible ----
df_joint['a_quitte_l_entreprise'] = (
    df_joint['a_quitte_l_entreprise']
    .str.lower()
    .str.strip()
)

df_joint = df_joint[
    df_joint['a_quitte_l_entreprise'].isin(['oui', 'non'])
]

# ---- Cible binaire ----
df_joint['target'] = df_joint['a_quitte_l_entreprise'].map({
    'oui': 1,
    'non': 0
})

# ---- Features ----
features = [
    'age',
    'genre',
    'revenu_mensuel',
    'statut_marital',
    'departement',
    'nombre_experiences_precedentes',
    'annees_dans_l_entreprise',
    'nombre_participation_pee',
    'nb_formations_suivies',
    'distance_domicile_travail',
    'niveau_education',
    'domaine_etude',
    'frequence_deplacement',
    'annees_depuis_la_derniere_promotion',
    'satisfaction_employee_environnement',
    'note_evaluation_precedente',
    'satisfaction_employee_nature_travail',
    'satisfaction_employee_equipe',
    'satisfaction_employee_equilibre_pro_perso',
    'note_evaluation_actuelle',
    'augementation_salaire_precedente'
]

X = df_joint[features]
y = df_joint['target']

# ---- Encoder catégories ----
X = pd.get_dummies(X)

# ---- Split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ---- Modèle ----
model = XGBClassifier(
    n_estimators=200,
    random_state=42,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

# ---- Sauvegarde ----
model_path = "app/model/model.pkl"
joblib.dump(model, model_path)

print(f"✅ Modèle sauvegardé : {model_path}")

