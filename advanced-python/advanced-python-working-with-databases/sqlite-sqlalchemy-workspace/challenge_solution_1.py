import sqlite3

# Connect to SQLite database 'users.db'
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Create 'Users' table if it doesn't exist
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Users (Id INTEGER PRIMARY KEY AUTOINCREMENT, FirstName TEXT, LastName TEXT, Email TEXT)''')

# List of users to add to the 'Users' table
users_to_add = [
    (None, 'Or', 'Hasson', 'hassonor@gmail.com'),
    (None, 'John', 'Doe', 'john.doe@example.com'),
    (None, 'Jane', 'Smith', 'jane.smith@example.com'),
    (None, 'Alice', 'Johnson', 'alice.johnson@example.com'),
    (None, 'Bob', 'Brown', 'bob.brown@gmail.com')
]

# Insert users into 'Users' table
cursor.executemany('INSERT INTO Users VALUES (?,?,?,?)', users_to_add)

# Fetch and print all records from 'Users' table
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

# Commit changes and close the connection
connection.commit()
connection.close()
