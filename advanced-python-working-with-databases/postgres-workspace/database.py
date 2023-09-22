import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def connect(db_name):
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=db_name,
            port=os.getenv("DB_PORT")
        )
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None
