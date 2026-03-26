# Schéma UML / BDD

```mermaid
erDiagram

    employees {
        int employee_id PK
        int satisfaction_employee_environnement
        int satisfaction_employee_nature_travail
        int satisfaction_employee_equipe
        int satisfaction_employee_equilibre_pro_perso
        int note_evaluation_precedente
        int note_evaluation_actuelle
        int niveau_hierarchique_poste
        varchar heure_supplementaires
        decimal augmentation_salaire_precedente
        int age
        varchar genre
        int revenu_mensuel
        varchar statut_marital
        varchar departement
        varchar poste
        int nombre_experiences_precedentes
        int annee_experience_totale
        int annees_dans_l_entreprise
        int annees_dans_le_poste_actuel
        int annees_depuis_la_derniere_promotion
        int annes_sous_responsable_actuel
        int nombre_participation_pee
        int nb_formations_suivies
        int distance_domicile_travail
        int niveau_education
        varchar domaine_etude
        varchar frequence_deplacement
        varchar a_quitte_l_entreprise
        timestamp created_at
    }

    employee_professional_info {
        int id PK
        int employee_id FK
    }

    employee_performance {
        int id PK
        int employee_id FK
    }

    employee_satisfaction {
        int id PK
        int employee_id FK
    }

    employee_work_conditions {
        int id PK
        int employee_id FK
    }

    prediction_sessions {
        uuid session_id PK
    }

    prediction_requests {
        int id PK
        uuid session_id FK
        int employee_id FK
        int age
        int revenu_mensuel
        timestamp created_at
    }

    prediction_results {
        int id PK
        int request_id FK
        int model_id FK
        int prediction
        decimal probability
        timestamp created_at
    }

    model_metadata {
        int model_id PK
    }

    api_audit_logs {
        bigint log_id PK
        uuid session_id FK
    }

    employees ||--|| employee_professional_info : has
    employees ||--|| employee_performance : has
    employees ||--|| employee_satisfaction : has
    employees ||--|| employee_work_conditions : has
    employees ||--o{ prediction_requests : referenced_by
    prediction_sessions ||--o{ prediction_requests : contains
    prediction_requests ||--|| prediction_results : generates
    model_metadata ||--o{ prediction_results : used_by
    prediction_sessions ||--o{ api_audit_logs : logs