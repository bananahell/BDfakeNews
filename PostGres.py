import psycopg2

try:
    connect_str = "dbname='Locadora' user='Du' host='localhost' " + \
                  "password='admin123'"

    conn = psycopg2.connect(connect_str)

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Categoria (
        Id INTEGER PRIMARY KEY,
        NomeCategoria VARCHAR(40) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Filme (
        Id INTEGER PRIMARY KEY,
        Titulo VARCHAR(40) NOT NULL,
        CategoriaId INTEGER REFERENCES Categoria (Id)
        );""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Fita (
        Numero INTEGER PRIMARY KEY,
        FilmeId INTEGER REFERENCES Filme (Id)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Cliente (
        NumeroAssociado INTEGER PRIMARY KEY,
        Nome VARCHAR(40) NOT NULL,
        Telefone VARCHAR(20) NOT NULL,
        Endereco VARCHAR(20) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Ator (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(40) NOT NULL,
        DataNascimento DATE NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Emprestimo (
        NumeroFita INTEGER  REFERENCES Fita (Numero),
        NACliente INTEGER  REFERENCES Cliente (NumeroAssociado),
        DataEmprestado DATE NOT NULL,
        DataDevolucao DATE NOT NULL,
        PRIMARY KEY(NumeroFita, NACliente)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS AtorFilmes (
        FilmeId INTEGER  REFERENCES Filme (Id),
        AtorId INTEGER  REFERENCES Ator (Id),
        PRIMARY KEY(FilmeId, AtorId)
        );""")

    # cursor.execute("""INSERT INTO Categoria VALUES(
    #     01, 'Action'
    #     );""")

    # cursor.execute("""INSERT INTO Categoria VALUES(
    #     02, 'Drama'
    #     );""")

    # cursor.execute("""INSERT INTO Filme VALUES(
    #     01, 'Vingadores Guerra Infinita', 01
    #     );""")

    # cursor.execute("""INSERT INTO Filme VALUES(
    #     02, 'Thor Ragnarok', 01
    #     );""")

    # cursor.execute("""INSERT INTO Filme VALUES(
    #     03, 'Titanic', 02
    #     );""")

    # cursor.execute("""INSERT INTO Filme VALUES(
    #     04, 'Creed', 01
    #     );""")


    # cursor.execute("""INSERT INTO Fita VALUES(
    #     00, 01
    #     );""")

    # cursor.execute("""INSERT INTO Fita VALUES(
    #     01, 02
    #     );""")

    # cursor.execute("""INSERT INTO Fita VALUES(
    #     02, 03
    #     );""")

    # cursor.execute("""INSERT INTO Fita VALUES(
    #     03, 04
    #     );""")

    # cursor.execute("""INSERT INTO Cliente VALUES(
    #     01, 'Eduardo', 00000000, 'Aguas Claras'
    #     );""")

    # cursor.execute("""INSERT INTO Ator VALUES(
    #     01, 'Robert Downey Jr.', '1965-04-04'
    #     );""")

    # cursor.execute("""INSERT INTO Ator VALUES(
    #     02, 'Chris Evans', '1981-06-13'
    #     );""")

    # cursor.execute("""INSERT INTO Ator VALUES(
    #     03, 'Chris Hemsworth', '1983-08-11'
    #     );""")

    # cursor.execute("""INSERT INTO Emprestimo VALUES(
    #     0, 1, '2018-10-17', '2018-10-27'
    #     );""")

    # cursor.execute("""INSERT INTO AtorFilmes VALUES(
    #     1, 1
    #     );""")

    # cursor.execute("""INSERT INTO AtorFilmes VALUES(
    #     1, 2
    #     );""")

    # cursor.execute("""INSERT INTO AtorFilmes VALUES(
    #     1, 3
    #     );""")

    # cursor.execute("""INSERT INTO AtorFilmes VALUES(
    #     2, 3
    #     );""")

    # run a SELECT statement - no data in there, but we can try it

    cursor.execute("""SELECT * from Filme""")
    for table in cursor.fetchall():
        print(table)

    cursor.execute("""SELECT * from Fita""")
    for table in cursor.fetchall():
        print(table)

    cursor.execute("""SELECT * from Ator""")
    for table in cursor.fetchall():
        print(table)

    conn.commit()
    cursor.close()

except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
finally:
    if conn is not None:
        conn.close()
