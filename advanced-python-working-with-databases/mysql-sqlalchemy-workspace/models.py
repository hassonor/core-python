# Importing necessary data types and functions from SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import registry, relationship

# Initializing a mapper registry for declarative base
mapper_registry = registry()

# Generating a base class from the mapper registry for our ORM models
Base = mapper_registry.generate_base()


# Model for 'projects' table
class Project(Base):
    __tablename__ = 'projects'

    # Defining columns for the 'projects' table
    project_id = Column(Integer, primary_key=True)  # Primary Key
    title = Column(String(length=50))
    description = Column(String(length=75))

    # String representation of the Project model
    def __repr__(self):
        return f"<Project(title='{self.title}', description='{self.description}')>"


# Model for 'tasks' table
class Task(Base):
    __tablename__ = 'tasks'

    # Defining columns for the 'tasks' table
    task_id = Column(Integer, primary_key=True)  # Primary Key
    project_id = Column(Integer, ForeignKey('projects.project_id'))  # Foreign Key linking to the 'projects' table
    description = Column(String(length=75))

    # Setting up a relationship between Task and Project models
    project = relationship("Project")

    # String representation of the Task model
    def __repr__(self):
        return f"<Task(description='{self.description}')>"


# Model for 'sales' table
class Sale(Base):
    __tablename__ = 'sales'

    # Defining columns for the 'sales' table
    order_num = Column(Integer, primary_key=True)  # Primary Key
    order_type = Column(String(length=255))
    cust_name = Column(String(length=255))
    prod_category = Column(String(length=255))
    prod_number = Column(String, nullable=False)
    prod_name = Column(String(length=255))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Integer)

    # String representation of the Sale model
    def __repr__(self):
        return (f"<Sale(order_num={self.order_num}, order_type={self.order_type}, "
                f"cust_name={self.cust_name}, prod_category={self.prod_category},"
                f" prod_number={self.prod_number}, prod_name={self.prod_name}, "
                f"quantity={self.quantity}, price={self.price}, discount={self.discount}, "
                f"order_total={self.order_total})>")
