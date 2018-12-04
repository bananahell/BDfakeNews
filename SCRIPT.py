import psycopg2
import Model

def CreateSchema(conn):
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaNoticia (
        Id INTEGER PRIMARY KEY,
        NomeCategoria VARCHAR(50) NOT NULL,
        DescricaoCategoria VARCHAR(200) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS InfluenciaExterna (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Noticia (
        Id INTEGER PRIMARY KEY,
        Manchete VARCHAR(200) NOT NULL,
        Descricao VARCHAR(700),
        Consequencia VARCHAR(400),
        Popularidade INTEGER,
        Data DATE,
        Piada BOOLEAN
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Idioma (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(60) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PalavrasChave (
        Nome VARCHAR(50) PRIMARY KEY,
        Idioma INTEGER REFERENCES Idioma (Id) ON DELETE CASCADE
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Local (
        Sigla CHAR(2) PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Complemento VARCHAR(50)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS FonteConfiavel (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        DescricaoFonte VARCHAR(300)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Ocupacao (
        Id INTEGER PRIMARY KEY,
        Emprego VARCHAR(60) NOT NULL,
        Descricao VARCHAR(200)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(70) NOT NULL,
        Idade INTEGER,
        OcupacaoId INTEGER REFERENCES Ocupacao (Id) ON DELETE CASCADE
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaMidia (
        Id INTEGER PRIMARY KEY,
        NomeCategoria VARCHAR(50) NOT NULL,
        DescricaoCategoria VARCHAR(80) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(70) NOT NULL,
        DescricaoMidia VARCHAR(300),
        CategoriaId INTEGER REFERENCES CategoriaMidia (Id) ON DELETE CASCADE
        );""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Influencia_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        InfluenciaId INTEGER REFERENCES InfluenciaExterna (Id) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, InfluenciaId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Midia_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        MidiaId INTEGER REFERENCES Midia (Id) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, MidiaId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS FonteConfiavel_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        FonteId INTEGER REFERENCES FonteConfiavel (Id) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, FonteId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PalavrasChave_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        PalavrasChaveId VARCHAR(50) REFERENCES PalavrasChave (Nome) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, PalavrasChaveId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Local_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        LocalId CHAR(2) REFERENCES Local (Sigla) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, LocalId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaNoticia_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        CategoriaId INTEGER REFERENCES CategoriaNoticia (Id) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, CategoriaId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Autor_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        AutorId INTEGER REFERENCES Pessoa (Id) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, AutorId)
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Vitima_Noticia (
        NoticiaId INTEGER REFERENCES Noticia (Id) ON DELETE CASCADE,
        VitimaId INTEGER REFERENCES Pessoa (Id) ON DELETE CASCADE,
        PRIMARY KEY (NoticiaId, VitimaId)
        );""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_CategoriaNoticia(Id INTEGER, NomeCategoria VARCHAR(30), DescricaoCategoria varchar(150))
        RETURNS void AS $$
        BEGIN
        INSERT INTO CategoriaNoticia
            VALUES (id, NomeCategoria, DescricaoCategoria);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_InfluenciaExterna (Id INTEGER,Nome VARCHAR(30))
        RETURNS void AS $$
        BEGIN
        INSERT INTO InfluenciaExterna
            VALUES (id,Nome);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Noticia (id INTEGER,Manchete VARCHAR(100), Descricao VARCHAR(500), Consequencia VARCHAR(300), Popularidade INTEGER, Data DATE, Piada BOOLEAN)
        RETURNS void AS $$
        BEGIN
        INSERT INTO Noticia
            VALUES (id,Manchete , Descricao, Consequencia, Popularidade, Data, Piada);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_CategoriaMidia (id INTEGER,NomeCategoria VARCHAR(30), DescricaoCategoria VARCHAR(60))
        RETURNS void AS $$
        BEGIN
        INSERT INTO CategoriaMidia
            VALUES (id,NomeCategoria, DescricaoCategoria);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Midia (id INTEGER,Nome VARCHAR(50), DescricaoMidia VARCHAR(250), CategoriaId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO Midia
            VALUES (id,Nome, DescricaoMidia, CategoriaId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Pessoa (id INTEGER,Nome VARCHAR(50), Idade INTEGER, OcupacaoId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO Pessoa
            VALUES (id,Nome, Idade, OcupacaoId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_PalavrasChave (Nome VARCHAR(30), Idioma INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO PalavrasChave
            VALUES (Nome, Idioma);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Local (Sigla CHAR(2), Nome VARCHAR(10), Complemento VARCHAR(50))
        RETURNS void AS $$
        BEGIN
        INSERT INTO Local
            VALUES (Sigla, Nome, Complemento);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_FonteConfiavel (Id INTEGER, Nome VARCHAR(30), DescricaoFonte VARCHAR(200))
        RETURNS void AS $$
        BEGIN
        INSERT INTO FonteConfiavel
            VALUES (Id, Nome, DescricaoFonte);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Ocupacao (id INTEGER,Emprego VARCHAR(40), Descricao VARCHAR(100))
        RETURNS void AS $$
        BEGIN
        INSERT INTO Ocupacao
            VALUES (id,Emprego, Descricao);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_InfluenciaExterna (Id INTEGER,Nome VARCHAR(30))
        RETURNS void AS $$
        BEGIN
        INSERT INTO InfluenciaExterna
            VALUES (id,Nome);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Idioma (id INTEGER,Nome VARCHAR(60))
        RETURNS void AS $$
        BEGIN
        INSERT INTO Idioma
            VALUES (id,Nome);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Autor_Noticia(NoticiaId INTEGER, AutorId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO Autor_Noticia
            VALUES (NoticiaId, AutorId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Vitima_Noticia(NoticiaId INTEGER, VitimaId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO Vitima_Noticia
            VALUES (NoticiaId, VitimaId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_CategoriaNoticia_Noticia(NoticiaId INTEGER, CategoriaId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO CategoriaNoticia_Noticia
            VALUES (NoticiaId, CategoriaId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Local_Noticia(NoticiaId INTEGER, LocalId CHAR(2))
        RETURNS void AS $$
        BEGIN
        INSERT INTO Local_Noticia
            VALUES (NoticiaId, LocalId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_PalavrasChave_Noticia(NoticiaId INTEGER, PalavrasChaveId VARCHAR(50))
        RETURNS void AS $$
        BEGIN
        INSERT INTO PalavrasChave_Noticia
            VALUES (NoticiaId, PalavrasChaveId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_FonteConfiavel_Noticia(NoticiaId INTEGER, FonteId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO FonteConfiavel_Noticia
            VALUES (NoticiaId, FonteId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Midia_Noticia(NoticiaId INTEGER, MidiaId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO Midia_Noticia
            VALUES (NoticiaId, MidiaId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Insere_Influencia_Noticia(NoticiaId INTEGER, InfluenciaId INTEGER)
        RETURNS void AS $$
        BEGIN
        INSERT INTO Influencia_Noticia
            VALUES (NoticiaId, InfluciaId);
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_CategoriaNoticia (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  CategoriaNoticia CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_InfluenciaExterna (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  InfluenciaExterna CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Noticia (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Noticia CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Idioma (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Idioma CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_PalavrasChave (n VARCHAR(50))
        RETURNS void AS $$
        BEGIN
        DELETE FROM  PalavrasChave CASCADE
            WHERE n = Nome;
            END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Local (n CHAR(2))
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Local CASCADE
            WHERE n = Sigla;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_FonteConfiavel (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  FonteConfiavel CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Ocupacao (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Ocupacao CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Pessoa (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Pessoa CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_CategoriaMidia (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  CategoriaMidia CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Midia (n INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Midia CASCADE
            WHERE n = Id;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Influencia_Noticia (n INTEGER, m INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Influencia_Noticia CASCADE
            WHERE n = NoticiaId AND m = InfluenciaId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Midia_Noticia (n INTEGER, m INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Midia_Noticia CASCADE
            WHERE n = NoticiaId AND m = MidiaId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_FonteConfiavel_Noticia (n INTEGER, m INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  FonteConfiavel_Noticia CASCADE
            WHERE n = NoticiaId AND m = FonteId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_PalavrasChave_Noticia (n INTEGER, m VARCHAR(50))
        RETURNS void AS $$
        BEGIN
        DELETE FROM  PalavrasChave_Noticia CASCADE
            WHERE n = NoticiaId AND m = PalavrasChaveId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Local_Noticia (n INTEGER, m CHAR(2))
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Local_Noticia CASCADE
            WHERE n = NoticiaId AND m = LocalId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_CategoriaNoticia_Noticia (n INTEGER, m INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  CategoriaNoticia_Noticia CASCADE
            WHERE n = NoticiaId AND m = CategoriaId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Autor_Noticia (n INTEGER, m INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Autor_Noticia CASCADE
            WHERE n = NoticiaId AND m = AutorId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE OR REPLACE FUNCTION Delete_Vitima_Noticia (n INTEGER, m INTEGER)
        RETURNS void AS $$
        BEGIN
        DELETE FROM  Vitima_Noticia CASCADE
            WHERE n = NoticiaId AND m = VitimaId;
        END;
        $$ LANGUAGE 'plpgsql';""")

    cursor.execute("""CREATE VIEW Autor_Vitima AS SELECT Autor_Noticia.AutorId, Pessoa.Nome, Pessoa.Idade, Pessoa.OcupacaoId,
        Vitima_Noticia.NoticiaId, Vitima_Noticia.VitimaId
        FROM Autor_Noticia
        JOIN Vitima_Noticia ON Autor_Noticia.NoticiaId = Vitima_Noticia.NoticiaId
        JOIN Pessoa ON Pessoa.Id = Autor_Noticia.AutorId;""")

    cursor.execute("""CREATE VIEW Pessoa_Ocupacao AS SELECT Pessoa.Id, Pessoa.Nome, Pessoa.Idade, Pessoa.OcupacaoId,
        Ocupacao.Emprego, Ocupacao.Descricao
        FROM Pessoa
        LEFT OUTER JOIN Ocupacao ON Pessoa.OcupacaoId = Ocupacao.Id;""")

    cursor.execute("""CREATE VIEW Midia_CategoriaM AS SELECT Midia.Id, Midia.Nome, Midia.DescricaoMidia, Midia.CategoriaId,
        CategoriaMidia.NomeCategoria, CategoriaMidia.DescricaoCategoria
        FROM Midia
        LEFT OUTER  JOIN CategoriaMidia ON Midia.CategoriaId = CategoriaMidia.Id;""")

    cursor.execute("""CREATE VIEW Noticia_CategoriaN AS SELECT CategoriaNoticia_Noticia.NoticiaId, Noticia.Manchete, Noticia.Descricao,
        Noticia.Consequencia, Noticia.Popularidade, Noticia.Data, Noticia.Piada,
        CategoriaNoticia_Noticia.CategoriaId, CategoriaNoticia.NomeCategoria, CategoriaNoticia.DescricaoCategoria
        FROM CategoriaNoticia_Noticia
        JOIN CategoriaNoticia ON CategoriaNoticia.Id = CategoriaNoticia_Noticia.CategoriaId
        RIGHT OUTER JOIN Noticia ON Noticia.Id = CategoriaNoticia_Noticia.NoticiaId;""")

    cursor.execute("""CREATE VIEW Full_Influencia_Noticia AS SELECT Influencia_Noticia.NoticiaId, Noticia.Manchete, Noticia.Descricao,
        Noticia.Consequencia, Noticia.Popularidade, Noticia.Data, Noticia.Piada,
        Influencia_Noticia.InfluenciaId, InfluenciaExterna.Nome
        FROM Influencia_Noticia
        JOIN InfluenciaExterna ON InfluenciaExterna.Id = Influencia_Noticia.InfluenciaId
        RIGHT OUTER JOIN Noticia ON Noticia.Id = Influencia_Noticia.NoticiaId;""")

    cursor.execute("""CREATE VIEW Full_Midia_Noticia AS SELECT Midia_Noticia.NoticiaId, Noticia.Manchete, Noticia.Descricao,
        Noticia.Consequencia, Noticia.Popularidade, Noticia.Data, Noticia.Piada,
        Midia_Noticia.MidiaId, Midia.Nome, Midia.DescricaoMidia, Midia.CategoriaId
        FROM Midia_Noticia
        JOIN Midia ON Midia.Id = Midia_Noticia.MidiaId
        RIGHT OUTER JOIN Noticia ON Noticia.Id = Midia_Noticia.NoticiaId;""")

    cursor.execute("""CREATE VIEW Full_FonteConfiavel_Noticia AS SELECT FonteConfiavel_Noticia.NoticiaId, Noticia.Manchete, Noticia.Descricao,
        Noticia.Consequencia, Noticia.Popularidade, Noticia.Data, Noticia.Piada,
        FonteConfiavel_Noticia.FonteId, FonteConfiavel.Nome, FonteConfiavel.DescricaoFonte
        FROM FonteConfiavel_Noticia
        JOIN FonteConfiavel ON FonteConfiavel.Id = FonteConfiavel_Noticia.FonteId
        RIGHT OUTER JOIN Noticia ON Noticia.Id = FonteConfiavel_Noticia.NoticiaId;""")

    cursor.execute("""CREATE VIEW Full_PalavrasChave_Noticia AS SELECT PalavrasChave_Noticia.NoticiaId, Noticia.Manchete, Noticia.Descricao,
        Noticia.Consequencia, Noticia.Popularidade, Noticia.Data, Noticia.Piada,
        PalavrasChave_Noticia.PalavrasChaveId, PalavrasChave.Idioma
        FROM PalavrasChave_Noticia
        JOIN PalavrasChave ON PalavrasChave.Nome = PalavrasChave_Noticia.PalavrasChaveId
        RIGHT OUTER JOIN Noticia ON Noticia.Id = PalavrasChave_Noticia.NoticiaId;""")

    cursor.execute("""CREATE VIEW Full_Local_Noticia AS SELECT Local_Noticia.NoticiaId, Noticia.Manchete, Noticia.Descricao,
        Noticia.Consequencia, Noticia.Popularidade, Noticia.Data, Noticia.Piada,
        Local_Noticia.LocalId, Local.Nome, Local.Complemento
        FROM Local_Noticia
        JOIN Local ON Local.Sigla = Local_Noticia.LocalId
        RIGHT OUTER JOIN Noticia ON Noticia.Id = Local_Noticia.NoticiaId;""")


    cursor.execute("""CREATE VIEW Full_Noticia AS SELECT CategoriaNoticia_Noticia.CategoriaId,
        Noticia.Id, Noticia.Manchete, Noticia.Descricao,
        Noticia.Consequencia, Noticia.Popularidade, Noticia.Data, Noticia.Piada,
        Autor_Noticia.AutorId,
        Vitima_Noticia.VitimaId,
        Local_Noticia.LocalId,
        PalavrasChave_Noticia.PalavrasChaveId,
        FonteConfiavel_Noticia.FonteId,
        Midia_Noticia.MidiaId,
        Influencia_Noticia.InfluenciaId
        FROM Noticia
        LEFT OUTER JOIN Autor_Noticia ON Autor_Noticia.NoticiaId = Noticia.Id
        LEFT OUTER JOIN Vitima_Noticia ON Vitima_Noticia.NoticiaId = Noticia.Id
        LEFT OUTER JOIN CategoriaNoticia_Noticia ON CategoriaNoticia_Noticia.NoticiaId = Noticia.Id
        LEFT OUTER JOIN Local_Noticia ON Local_Noticia.NoticiaId = Noticia.Id
        LEFT OUTER JOIN PalavrasChave_Noticia ON PalavrasChave_Noticia.NoticiaId = Noticia.Id
        LEFT OUTER JOIN FonteConfiavel_Noticia ON FonteConfiavel_Noticia.NoticiaId = Noticia.Id
        LEFT OUTER JOIN Midia_Noticia ON Midia_Noticia.NoticiaId = Noticia.Id
        LEFT OUTER JOIN Influencia_Noticia ON Influencia_Noticia.NoticiaId = Noticia.Id;""")


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
        CreateSchema(conn)
        conn.commit()

        Insert("categorianoticia", connect_str, 0, "'Violência'", "'Agressão física e/ou moral a própria pessoa ou a terceiros relacionados.'")
        Insert("categorianoticia", connect_str, 1, "'Política'", "'Escândalo de teor político.'")
        Insert("categorianoticia", connect_str, 2, "'Corrupção'", "'Roubo ou desvio de verba pública.'")
        Insert("categorianoticia", connect_str, 3, "'Escândalo'", "'Notícia pejorativa.'")
        Insert("categorianoticia", connect_str, 4, "'Difamação'", "'Notícia com intuito de prejudicar a imagem frente ao povo.'")

        Insert("noticia", connect_str, 0, "'Corrupção'", "'Acusado de desviar verba publica.'", "'perde confiança do povo'", 80, "'2018-10-12'", "false")
        Insert("noticia", connect_str, 1, "'Crime'", "'Acusado de agredir outro político.'", "'odiado pela câmara'", 80, "'2018-10-12'", "false")
        Insert("noticia", connect_str, 2, "'Abuso'", "'Acusado de xingar outro político.'", "'adorado pelas revistas de fofoca'", 80, "'2018-10-12'", "false")
        Insert("noticia", connect_str, 3, "'Crime contra animais'", "'Acusado de comparar a Dilma a um animal.'", "'adorado pelas massas.'", 100, "'2018-10-12'", "false")
        Insert("noticia", connect_str, 4, "'Assassinato'", "'Acusado de matar o senador.'", "'Sanidade é posta em dúvida.'", 80, "'2018-10-12'", "false")
        Insert("noticia", connect_str, 5, "'Escravidão'", "'Acusado de importar escravos chineses.'", "'Advogados vão ao museu olhar a Carta Aurea.'", 80, "'2018-10-12'", "false")

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

        Insert("ocupacao", connect_str, 0, "'Governador'", "'Responsável pela administração de um Estado da Federação'")
        Insert("ocupacao", connect_str, 1, "'Presidente de Partido'", "'Líder de um partido político que representa um segmento da população'")
        Insert("ocupacao", connect_str, 2, "'Presidente'", "'Líder da nação'")
        Insert("ocupacao", connect_str, 3, "'Deputado'", "'Representante do povo de um Estado da Federação'")
        Insert("ocupacao", connect_str, 4, "'Senador'", "'Representante de um Estado da Federação'")

        Insert("pessoa", connect_str, 0, "'Lance'", 20, 0)
        Insert("pessoa", connect_str, 1, "'Eduardo'", 19, 3)
        Insert("pessoa", connect_str, 2, "'Pedro'", 22, 4)
        Insert("pessoa", connect_str, 3, "'Lucas'", 50, 1)
        Insert("pessoa", connect_str, 4, "'Jão'", 30, 3)
        Insert("pessoa", connect_str, 5, "'Marcos'", 35, 2)
        Insert("pessoa", connect_str, 6, "'Marcelo'", 40, 3)

        Insert("categoriamidia", connect_str, 0, "'Televisão'", "'Comentaristas e jornais.'")
        Insert("categoriamidia", connect_str, 1, "'Revistas'", "'Opiniões de autores conhecidos.'")
        Insert("categoriamidia", connect_str, 2, "'Redes Sociais'", "'Facebook, Whats App, dentre outros.'")
        Insert("categoriamidia", connect_str, 3, "'Rádio'", "'Comentaristas do dia a dia'")
        Insert("categoriamidia", connect_str, 4, "'Blogs'", "'Artigos com opiniões dos autores'")

        Insert("autor_noticia", connect_str, 4, 3)
        Insert("autor_noticia", connect_str, 3, 3)
        Insert("autor_noticia", connect_str, 1, 5)
        Insert("autor_noticia", connect_str, 0, 5)
        Insert("autor_noticia", connect_str, 2, 4)

        Insert("vitima_noticia", connect_str, 4, 0)
        Insert("vitima_noticia", connect_str, 3, 2)
        Insert("vitima_noticia", connect_str, 1, 1)
        Insert("vitima_noticia", connect_str, 0, 1)
        Insert("vitima_noticia", connect_str, 2, 6)

        Insert("fonteconfiavel", connect_str, 0, "'Anonimus'", "'Grupo hacker que resoveu fornecer informações'")
        Insert("fonteconfiavel", connect_str, 1, "'Repórter'", "'O repórter que divulgou a notícia descobriu/confessou que a notícia é falsa'")
        Insert("fonteconfiavel", connect_str, 2, "'Testemunhas'", "'Testemunhas do ocorrido relatam a verdade'")
        Insert("fonteconfiavel", connect_str, 3, "'Polícia'", "'A polícia investigou e descobriu a verdade'")
        Insert("fonteconfiavel", connect_str, 4, "'Divisão de inteligência'", "'A divisão de inteligência e espionagem descobriu a verdade'")

        Insert("fonteconfiavel_noticia", connect_str, 0, 0)
        Insert("fonteconfiavel_noticia", connect_str, 4, 1)
        Insert("fonteconfiavel_noticia", connect_str, 1, 2)
        Insert("fonteconfiavel_noticia", connect_str, 5, 3)
        Insert("fonteconfiavel_noticia", connect_str, 1, 4)

        Insert("midia", connect_str, 0, "'Jornal Nacional'", "'Jornal na televisão da Rede Globo'", 0)
        Insert("midia", connect_str, 1, "'Veja'", "'Revista Veja'", 2)
        Insert("midia", connect_str, 2, "'Facebook'", "'Rede social autamente popular'", 3)
        Insert("midia", connect_str, 3, "'JustiçaFM'", "'Rádio do justiceiro, que não investiga nada antes de publicar noticias'", 1)
        Insert("midia", connect_str, 4, "'O Caozeiro'", "'Blog conhecido por passar noticias engraçadas, independente da veracidade delas.'", 4)

        Insert("influencia_noticia", connect_str, 0, 1)
        Insert("influencia_noticia", connect_str, 1, 0)
        Insert("influencia_noticia", connect_str, 2, 2)
        Insert("influencia_noticia", connect_str, 3, 4)
        Insert("influencia_noticia", connect_str, 4, 3)

        Insert("midia_noticia", connect_str, 0, 0)
        Insert("midia_noticia", connect_str, 1, 3)
        Insert("midia_noticia", connect_str, 2, 2)
        Insert("midia_noticia", connect_str, 3, 3)
        Insert("midia_noticia", connect_str, 4, 4)

        Insert("palavraschave_noticia", connect_str, 0, "'Irresponsabilidade pública'")
        Insert("palavraschave_noticia", connect_str, 1, "'Irresponsabilidade pública'")
        Insert("palavraschave_noticia", connect_str, 2, "'Irresponsabilidade pública'")
        Insert("palavraschave_noticia", connect_str, 3, "'Irresponsabilidade pública'")
        Insert("palavraschave_noticia", connect_str, 4, "'Irresponsabilidade pública'")

        Insert("categorianoticia_noticia", connect_str, 0, 2)
        Insert("categorianoticia_noticia", connect_str, 1, 0)
        Insert("categorianoticia_noticia", connect_str, 2, 3)
        Insert("categorianoticia_noticia", connect_str, 3, 4)
        Insert("categorianoticia_noticia", connect_str, 4, 0)

        Insert("local_noticia", connect_str, 0, "'DF'")
        Insert("local_noticia", connect_str, 1, "'DF'")
        Insert("local_noticia", connect_str, 2, "'DF'")
        Insert("local_noticia", connect_str, 3, "'DF'")
        Insert("local_noticia", connect_str, 4, "'DF'")

    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()
