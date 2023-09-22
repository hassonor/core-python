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
        return mysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=db_name
        )
    except mysql.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def add_project(_cursor, project_title, project_description, _tasks):
    """Add a new project and associated tasks to the database.

    Args:
        _cursor (Cursor): Database cursor.
        project_title (str): Title of the project.
        project_description (str): Description of the project.
        _tasks (list): List of task descriptions.
    """
    project_data = (project_title, project_description)
    _cursor.execute('''INSERT INTO projects(title,description) VALUES (%s, %s)''', project_data)

    tasks_data = [(_cursor.lastrowid, task) for task in _tasks]
    _cursor.executemany('''INSERT INTO tasks(project_id, description) VALUES(%s,%s)''', tasks_data)
