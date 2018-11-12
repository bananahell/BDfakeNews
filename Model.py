

def CreateTables(conn):
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaNoticia (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL,
        Descricao VARCHAR(150) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS InfluenciaExterna (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Noticia (
        Id INTEGER PRIMARY KEY,
        Manchete VARCHAR(100) NOT NULL,
        Descricao VARCHAR(500),
        Consequencia VARCHAR(300),
        Popularidade INTEGER,
        Data DATE,
        Piada BOOLEAN,
        InfluenciaId INTEGER REFERENCES InfluenciaExterna (Id)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PalavraChave (
        Nome VARCHAR(30) PRIMARY KEY,
        Idioma VARCHAR(15) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Local (
        Sigla CHAR(2) PRIMARY KEY,
        Nome VARCHAR(10) NOT NULL,
        Complemento VARCHAR(50)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS FonteConfiavel (
        Nome VARCHAR(30) PRIMARY KEY,
        Descricao VARCHAR(200) NOT NULL,
        NoticiaId INTEGER REFERENCES Noticia (Id)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Idade INTEGER
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Ocupacao (
        Id INTEGER PRIMARY KEY,
        Emprego VARCHAR(40) NOT NULL,
        Descricao VARCHAR(100)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaMidia (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL,
        Descricao VARCHAR(60) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Descricao VARCHAR(250)
        );""")

    cursor.close()


def Insert(TableName, conn, *args):
    string_args = list(map(lambda a: str(a), args))
    cursor = conn.cursor()
    sql = """INSERT INTO """ + TableName + " VALUES(" + (", ".join(string_args)) + """);"""
    cursor.execute(sql)

    cursor.close()
