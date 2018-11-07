import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host
                     user="Du",       # username
                     passwd="admin123",     # password
                     db="pythonspot")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS examples")

Filme = """CREATE TABLE Filme(Id INT PRIMARY KEY,
Titulo  VARCHAR(40) NOT NULL
Categoria  VARCHAR(40))"""

Fita = """CREATE TABLE Filme(Id INT PRIMARY KEY,
Titulo  VARCHAR(40) NOT NULL
Categoria  VARCHAR(40))"""


cur.execute("CREATE TABLE ")

# Select data from table using SQL query.
cur.execute("SELECT * FROM examples")

# print the first and second columns
for row in cur.fetchall():
    print(row[0], " ", row[1])
