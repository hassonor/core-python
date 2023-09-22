import sqlite3

# [1] Establish Database Connection
# ---------------------------
connection = sqlite3.connect('movies.db')

# [2] Create a Cursor for Database Operations
# ---------------------------
cursor = connection.cursor()

# [3] Database Initialization
# ---------------------------
# 3.1 Create the 'Movies' table (if it doesn't already exist)
# Note: This section is currently commented out and should be activated if table creation is needed.
# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')

# 3.2 Insert sample records into the 'Movies' table
# Note: This section is currently commented out. Uncomment to insert the sample record.
# cursor.execute('''INSERT INTO Movies VALUES('Titanic', 'James Cameron', 1997)''')

# [4] Data Operations
# ---------------------------
# 4.1 Define a sample dataset of famous films for insertion
# famous_films = [
#     ('Pulp Fiction', 'Quentin Tarantino', 1994),
#     ('Back to the Future', 'Robert Zemeckis', 1985),
#     ('Moonrise Kingdom', 'Wes Anderson', 2012)
# ]

# 4.2 Insert multiple records into the 'Movies' table
# cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famous_films)

# 4.3 Fetch all records from the 'Movies' table
# cursor.execute("SELECT * FROM Movies")
# print(cursor.fetchall())

# 4.4 Fetch movies by a specific release year
# release_year = (1985,)
# cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
# print(cursor.fetchall())

# [5] Finalize Operations
# ---------------------------
# 5.1 Commit the database changes
connection.commit()

# 5.2 Close the database connection
connection.close()
