from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from config import DATABASE_URL
from models import Base, Project, Task

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)


def add_project_with_tasks(_session, title, description, task_descriptions):
    project = Project(title=title, description=description)
    _session.add(project)
    _session.flush()

    tasks = [Task(project_id=project.project_id, description=task_desc) for task_desc in task_descriptions]
    _session.bulk_save_objects(tasks)
    _session.commit()


def print_tasks_for_project(_session, project_title):
    project = _session.execute(select(Project).where(Project.title == project_title)).scalar()

    tasks = _session.execute(select(Task).where(Task.project_id == project.project_id)).all()
    for task in tasks:
        print(task)


if __name__ == '__main__':
    with Session(engine) as session:
        # Uncomment below lines to add data
        # add_project_with_tasks(session, 'Organize closet', 'Organize closet by color and style', [
        #     'Decide what clothes to donate',
        #     'Organize summer clothes',
        #     'Organize winter clothes'
        # ])

        print_tasks_for_project(session, 'Organize closet')
