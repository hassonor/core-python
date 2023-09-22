import os

from database import connect, add_project

if __name__ == "__main__":
    db = connect(os.getenv("DB_NAME"))

    # Check if connection was successful
    if db:
        cursor = db.cursor()

        # Example data
        tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
        add_project(cursor, "Clean house", "Clean house by room", tasks)
        db.commit()

        cursor.execute("SELECT * FROM projects")
        project_records = cursor.fetchall()
        print(project_records)

        cursor.execute("SELECT * FROM tasks")
        tasks_records = cursor.fetchall()
        print(tasks_records)

        db.close()
