from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=75))

    def __repr__(self):
        return f"<Project(title='{self.title}', description='{self.description}')>"


class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=75))

    project = relationship("Project")

    def __repr__(self):
        return f"<Task(description='{self.description}')>"
