

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

    cursor.execute("""CREATE TABLE IF NOT EXISTS PalavrasChave (
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

    cursor.execute("""CREATE TABLE IF NOT EXISTS Ocupacao (
        Id INTEGER PRIMARY KEY,
        Emprego VARCHAR(40) NOT NULL,
        Descricao VARCHAR(100)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Idade INTEGER,
        OcupacaoId INTEGER REFERENCES Ocupacao (Id)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaMidia (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL,
        Descricao VARCHAR(60) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Descricao VARCHAR(250),
        CategoriaId INTEGER REFERENCES CategoriaMidia (Id)
        );""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        MidiaId INTEGER REFERENCES Midia (Id),
        PRIMARY KEY (NoticiaId, MidiaId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PalavrasChave_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        PalavrasChaveId VARCHAR(30) REFERENCES PalavrasChave (Nome),
        PRIMARY KEY (NoticiaId, PalavrasChaveId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Local_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        LocalId CHAR(2) REFERENCES Local (Sigla),
        PRIMARY KEY (NoticiaId, LocalId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaNoticia_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        CategoriaId INTEGER REFERENCES CategoriaNoticia (Id),
        PRIMARY KEY (NoticiaId, CategoriaId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Autor_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        AutorId INTEGER REFERENCES Pessoa (Id),
        PRIMARY KEY (NoticiaId, AutorId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Vitima_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        VitimaId INTEGER REFERENCES Pessoa (Id),
        PRIMARY KEY (NoticiaId, VitimaId)
        );""")

    cursor.close()


def Insert(TableName, conn, *args):
    string_args = list(map(lambda a: str(a), args))
    cursor = conn.cursor()
    sql = """INSERT INTO """ + TableName + " VALUES(" + (", ".join(string_args)) + """);"""
    cursor.execute(sql)

    cursor.close()
