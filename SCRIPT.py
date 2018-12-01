import psycopg2
import Model

def CreateTables(conn):
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaNoticia (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Descricao VARCHAR(200) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS InfluenciaExterna (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Noticia (
        Id SERIAL PRIMARY KEY,
        Manchete VARCHAR(200) NOT NULL,
        Descricao VARCHAR(700),
        Consequencia VARCHAR(400),
        Popularidade INTEGER,
        Data DATE,
        Piada BOOLEAN
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Idioma (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(60) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PalavrasChave (
        Nome VARCHAR(50) PRIMARY KEY,
        Idioma INTEGER REFERENCES Idioma (Id)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Local (
        Sigla CHAR(2) PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Complemento VARCHAR(50)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS FonteConfiavel (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Descricao VARCHAR(300)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Ocupacao (
        Id SERIAL PRIMARY KEY,
        Emprego VARCHAR(60) NOT NULL,
        Descricao VARCHAR(200)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(70) NOT NULL,
        Idade INTEGER,
        OcupacaoId INTEGER REFERENCES Ocupacao (Id)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaMidia (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Descricao VARCHAR(80) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia (
        Id SERIAL PRIMARY KEY,
        Nome VARCHAR(70) NOT NULL,
        Descricao VARCHAR(300),
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
        PalavrasChaveId VARCHAR(50) REFERENCES PalavrasChave (Nome),
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


def Insert(TableName, connect_str, *args):
    try:
        conn = psycopg2.connect(connect_str)
        string_args = list(map(lambda a: str(a), args))
        cursor = conn.cursor()
        sql = """INSERT INTO """ + TableName + "(" + (", ".join(Model.table_columns[TableName])) + ")" + " VALUES(" + (", ".join(string_args)) + """);"""

        cursor.execute(sql)
        conn.commit()

    except Exception as e:
        print("Problem ocurred during insert")
        print(e)
    finally:
        cursor.close()
        conn.close()



def main():
    try:
        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)
        CreateTables(conn)
        conn.commit()

        Insert("categorianoticia", connect_str, 0, "'Violência'", "'Agressão física e/ou moral a própria pessoa ou a terceiros relacionados.'")
        Insert("categorianoticia", connect_str, 1, "'Política'", "'Escândalo de teor político.'")
        Insert("categorianoticia", connect_str, 2, "'Corrupção'", "'Roubo ou desvio de verba pública.'")
        Insert("categorianoticia", connect_str, 3, "'Escândalo'", "'Notícia pejorativa.'")

        Insert("noticia", connect_str, 0, "'Corrupção'", "'Acusado de desviar verba publica.'", "'perde confiança do povo'", 80, "'2018-10-12'", "false");
        Insert("noticia", connect_str, 1, "'Crime'", "'Acusado de agredir outro político.'", "'odiado pela câmara'", 80, "'2018-10-12'", "false");
        Insert("noticia", connect_str, 2, "'Abuso'", "'Acusado de xingar outro político.'", "'adorado pelas revistas de fofoca'", 80, "'2018-10-12'", "false");
        Insert("noticia", connect_str, 3, "'Crime contra animais'", "'Acusado de comparar a Dilma a um animal.'", "'adorado pelas massas.'", 100, "'2018-10-12'", "false");
        Insert("noticia", connect_str, 4, "'Assassinato'", "'Acusado de matar o senador.'", "'Sanidade é posta em dúvida.'", 80, "'2018-10-12'", "false");
        Insert("noticia", connect_str, 5, "'Escravidão'", "'Acusado de importar escravos chineses.'", "'Advogados vão ao museu olhar a Carta Aurea.'", 80, "'2018-10-12'", "false");

        Insert("influenciaexterna", connect_str, 0, "'Russos'")
        Insert("influenciaexterna", connect_str, 1, "'Bolivianos'")
        Insert("influenciaexterna", connect_str, 2, "'Cubanos'")
        Insert("influenciaexterna", connect_str, 3, "'Americanos'")
        Insert("influenciaexterna", connect_str, 4, "'Colombianos'")
        Insert("influenciaexterna", connect_str, 5, "'Portugueses'")

        Insert("idioma", connect_str, 0, "'Português'")
        Insert("idioma", connect_str, 1, "'Inglês'")
        Insert("idioma", connect_str, 2, "'Russo'")

        Insert("palavraschave", connect_str, "'Corrupção'", 0)
        Insert("palavraschave", connect_str, "'Desvio de verba'", 0)
        Insert("palavraschave", connect_str, "'Lavagem de dinheiro'", 0)
        Insert("palavraschave", connect_str, "'Formação de quadrilha'", 0)
        Insert("palavraschave", connect_str, "'Corrupção passiva'", 0)
        Insert("palavraschave", connect_str, "'Irresponsabilidade pública'", 0)

        Insert("local", connect_str, "'DF'", "'Distrito Federal'", "'MDB'")
        Insert("local", connect_str, "'SP'", "'São Paulo'", "'PSB'")
        Insert("local", connect_str, "'RJ'", "'Rio de Janeiro'", "'MDB'")
        Insert("local", connect_str, "'MG'", "'Minas Gerais'", "'PSDB'")
        Insert("local", connect_str, "'PB'", "'Paraíba'", "'PSB'")

        # Insert("fonteconfiavel", connect_str, "'nome'", "'descricao'")

        Insert("ocupacao", connect_str, 0, "'Governador'", "'Responsável pela administração de um Estado da Federação'");
        Insert("ocupacao", connect_str, 1, "'Presidente de Partido'", "'Líder de um partido político que representa um segmento da população'");
        Insert("ocupacao", connect_str, 2, "'Presidente'", "'Líder da nação'");
        Insert("ocupacao", connect_str, 3, "'Deputado'", "'Representante do povo de um Estado da Federação'");
        Insert("ocupacao", connect_str, 4, "'Senador'", "'Representante de um Estado da Federação'");

        Insert("pessoa", connect_str, 0, "'Lance'", 20, 0);
        Insert("pessoa", connect_str, 1, "'Eduardo'", 19, 3);
        Insert("pessoa", connect_str, 2, "'Pedro'", 22, 4);
        Insert("pessoa", connect_str, 3, "'Lucas'", 50, 1);
        Insert("pessoa", connect_str, 4, "'Jão'", 30, 3);
        Insert("pessoa", connect_str, 5, "'Marcos'", 35, 2);
        Insert("pessoa", connect_str, 6, "'Marcelo'", 40, 3);

        Insert("categoriamidia", connect_str, 0, "'Televisão'", "'Comentaristas e jornais.'")
        Insert("categoriamidia", connect_str, 1, "'Revistas'", "'Opiniões de autores conhecidos.'")
        Insert("categoriamidia", connect_str, 2, "'Redes Sociais'", "'Facebook, Whats App, dentre outros.'")
        Insert("categoriamidia", connect_str, 3, "'Rádio'", "'Comentaristas do dia a dia'")
        Insert("categoriamidia", connect_str, 4, "'Blogs'", "'Artigos com opiniões dos autores'")

        Insert("autor_noticia", connect_str, 4, 3);
        Insert("autor_noticia", connect_str, 3, 3);
        Insert("autor_noticia", connect_str, 1, 5);
        Insert("autor_noticia", connect_str, 0, 5);
        Insert("autor_noticia", connect_str, 2, 4);

        Insert("vitima_noticia", connect_str, 4, 0);
        Insert("vitima_noticia", connect_str, 3, 2);
        Insert("vitima_noticia", connect_str, 1, 1);
        Insert("vitima_noticia", connect_str, 0, 1);
        Insert("vitima_noticia", connect_str, 2, 6);

    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
