import os
import mysql.connector as mysql
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def connect(db_name):
    """Connect to a MySQL database using environment variables for configuration.

    Args:
        db_name (str): The name of the database to connect to.

    Returns:
        connection: A mysql.connector connection object if successful, None otherwise.
    """
    try:
        # Create a connection using environment variables for host, user, and password
        return mysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=db_name
        )
    except mysql.Error as e:  # Make sure to specify mysql.Error
        print(f"Error connecting to database: {e}")
        return None


# Test the connection and fetch data from the 'projects' table
if __name__ == "__main__":
    db = connect(os.getenv("DB_NAME"))

    # Check if connection was successful
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM projects")
        project_records = cursor.fetchall()
        print(project_records)
        db.close()
