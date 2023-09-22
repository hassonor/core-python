from sqlalchemy import Column, String, Integer, ForeignKey, Float
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


class Sale(Base):
    __tablename__ = 'sales'
    order_num = Column(Integer, primary_key=True)
    order_type = Column(String(length=255))
    cust_name = Column(String(length=255))
    prod_category = Column(String(length=255))
    prod_number = Column(String, nullable=False)
    prod_name = Column(String(length=255))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Integer)

    def __repr__(self):
        return (f"<Sale(order_num={self.order_num}, order_type={self.order_type}, "
                f"cust_name={self.cust_name}, prod_category={self.prod_category},"
                f" prod_number={self.prod_number}, prod_name={self.prod_name}, "
                f"quantity={self.quantity}, price={self.price}, discount={self.discount}, "
                f"order_total={self.order_total})>")
