from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


# Define User model
class User(Base):
    __tablename__ = 'Users'
    Id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)


# Create an SQLite database engine in memory
engine = create_engine('sqlite:///users.db')

# Create 'Users' table within the database
Base.metadata.create_all(engine)

# Start a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add users to the 'Users' table
users = [
    User(FirstName='Or', LastName='Hasson', Email='hassonor@gmail.com'),
    User(FirstName='John', LastName='Doe', Email='john.doe@example.com'),
    User(FirstName='Jane', LastName='Smith', Email='jane.smith@example.com'),
    User(FirstName='Alice', LastName='Johnson', Email='alice.johnson@example.com'),
    User(FirstName='Bob', LastName='Brown', Email='bob.brown@gmail.com')
]
session.add_all(users)

# Commit changes
session.commit()

# Fetch and print all records from 'Users' table
for user in session.query(User).all():
    print(user.Id, user.FirstName, user.LastName, user.Email)

# Close the session
session.close()
