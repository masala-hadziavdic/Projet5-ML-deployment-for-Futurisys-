import psycopg2
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        dbname="ml_database",
        user="postgres",
        password="0000",
        host="localhost",
        port="5434"
    )
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Database error:", e)
        raise e
    finally:
        conn.close()

