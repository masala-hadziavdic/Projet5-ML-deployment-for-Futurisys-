from database import get_connection

def get_employee_by_data(employee_data: dict):
    """
    Recherche un employé existant dans la table employees
    """
    with get_connection() as conn:
        cur = conn.cursor()

        query = """
        SELECT * FROM employees
        WHERE age = %s
        AND revenu_mensuel = %s
        AND departement = %s
        AND poste = %s;
        """

        cur.execute(query, (
            employee_data.get("age"),
            employee_data.get("revenu_mensuel"),
            employee_data.get("departement"),
            employee_data.get("poste")
        ))

        employee = cur.fetchone()
        cur.close()
        return employee


def save_prediction_request(age, salary, department):
    """
    Enregistre une requête (input modèle)
    """
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO prediction_requests (age, salary, department)
        VALUES (%s, %s, %s)
        RETURNING id;
        """, (age, salary, department))

        request_id = cur.fetchone()[0]
        cur.close()
        return request_id


def save_prediction_result(request_id, prediction, probability):
    """
    Enregistre le résultat du modèle
    """
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO prediction_results (request_id, prediction, probability)
        VALUES (%s, %s, %s)
        RETURNING id;
        """, (request_id, prediction, probability))

        result_id = cur.fetchone()[0]
        cur.close()
        return result_id
