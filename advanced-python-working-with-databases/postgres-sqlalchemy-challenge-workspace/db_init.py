from models import Base
from database import engine

# This will create the tables based on the models.
Base.metadata.create_all(engine)
