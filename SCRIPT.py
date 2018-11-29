import psycopg2
import Model

table_columns = {"categorianoticia":  ("id", "nome", "descricao"),
                 "noticia":           ("id", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "influenciaid"),
                 "Influenciaexterna": ("id", "nome"),
                 "palavraschave":     ("nome, idioma"),
                 "local":             ("sigla", "nome", "complemento"),
                 "fonteconfiavel":    ("nome", "descricao", "noticiaid"),
                 "ocupacao":          ("id", "emprego", "descricao"),
                 "pessoa":            ("id", "nome", "idade", "ocupacaoid"),
                 "categoriamidia":    ("id", "nome", "descricao"),
                 "midia":             ("id", "nome", "descricao", "categoriaid"),

                 "midia_noticia":            ("noticiaid", "midiaid"),
                 "palavraschave_noticia":    ("noticiaid", "palavraschaveid"),
                 "local_noticia":            ("noticiaid", "localid"),
                 "categorianoticia_noticia": ("noticiaid", "categorianoticia_noticia"),
                 "autor_noticia":            ("noticiaid", "autorid"),
                 "vitima_noticia":           ("noticiaid", "vitimaid")}

def CreateTables(conn):
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaNoticia (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL,
        Descricao VARCHAR(150) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS InfluenciaExterna (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Noticia (
        Id SERIAL PRIMARY KEY,
        Manchete VARCHAR(100) NOT NULL,
        Descricao VARCHAR(500),
        Consequencia VARCHAR(300),
        Popularidade INTEGER,
        Data DATE,
        Piada BOOLEAN
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
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL,
        Descricao VARCHAR(200)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Ocupacao (
        Id SERIAL PRIMARY KEY,
        Emprego VARCHAR(40) NOT NULL,
        Descricao VARCHAR(100)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Idade INTEGER,
        OcupacaoId INTEGER REFERENCES Ocupacao (Id)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaMidia (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(30) NOT NULL,
        Descricao VARCHAR(60) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Descricao VARCHAR(250),
        CategoriaId INTEGER REFERENCES CategoriaMidia (Id)
        );""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Influencia_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        InfluenciaId INTEGER REFERENCES InfluenciaExterna (Id),
        PRIMARY KEY (NoticiaId, InfluenciaId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        MidiaId INTEGER REFERENCES Midia (Id),
        PRIMARY KEY (NoticiaId, MidiaId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS FonteConfiavel_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id),
        FonteId INTEGER REFERENCES FonteConfiavel (Id),
        PRIMARY KEY (NoticiaId, FonteId)
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
    try:
        string_args = list(map(lambda a: str(a), args))
        cursor = conn.cursor()
        print ("ayy lmao")
        sql = """INSERT INTO """ + TableName + "(" + (", ".join(table_columns[TableName])) + ")" + " VALUES(" + (", ".join(string_args)) + """);"""
        print (sql)
        cursor.execute(sql)
    except Exception as e:
        print ("Problem inserting values into " + TableName)
    finally:
        cursor.close()



def main():
    try:
        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)
        print ("antesainda")
        CreateTables(conn)
        print ("aqui")
        Insert("CategoriaNoticia", conn, 0, "'Violência'",
        "'Agressão física e/ou moral a própria pessoa ou a terceiros relacionados.'")
        print ("passou")

        conn.commit()

    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
