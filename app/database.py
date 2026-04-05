from dotenv import load_dotenv
import os
import psycopg2
from contextlib import contextmanager

# Charger le fichier .env
load_dotenv()

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
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
