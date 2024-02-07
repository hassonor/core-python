# Importing necessary modules from sqlalchemy
import sqlalchemy

# Create a new SQLite engine to interact with a database named movies.db
# The echo=True flag will enable logging, allowing you to see SQL queries executed by SQLAlchemy.
engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

# Create metadata object which provides a collection of Table objects and their associated schema constructs
metadata = sqlalchemy.MetaData()

# Define a new table structure for the 'Movies' table within the metadata
# This does not create the table in the database, but provides an SQLAlchemy representation of it.
movies_table = sqlalchemy.Table("Movies", metadata,
                                sqlalchemy.Column("title", sqlalchemy.Text),  # Title column as text
                                sqlalchemy.Column("director", sqlalchemy.Text),  # Director column as text
                                sqlalchemy.Column("year", sqlalchemy.Integer))  # Year column as integer

# Create tables in the database according to the definitions in the metadata.
# This will only create tables that don't already exist.
metadata.create_all(engine)

# Using the engine, establish a connection and execute a query to fetch all records from the 'Movies' table
with engine.connect() as conn:
    # Execute a select query on the movies_table and print each row.
    for row in conn.execute(sqlalchemy.select(movies_table)):
        print(row)
