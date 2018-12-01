CREATE OR REPLACE FUNCTION Insere_CategoriaNoticia(Id INTEGER, Nome VARCHAR(30), Descricao varchar(150))
 
      RETURNS void AS $$
      BEGIN
        INSERT INTO CategoriaNoticia 
         VALUES (Id, Nome, Descricao);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_InfluenciaExterna (Id INTEGER,Nome VARCHAR(30))
 
      RETURNS void AS $$
      BEGIN
        INSERT INTO InfluenciaExterna 
         VALUES (id,Nome);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Noticia (id INTEGER,Manchete VARCHAR(100), Descricao VARCHAR(500), Consequencia VARCHAR(300), Popularidade INTEGER, Data DATE, Piada BOOLEAN)
 
      RETURNS void AS $$
      BEGIN
      	#IF (SELECT COUNT(*) FROM InfluenciaExterna WHERE InfluenciaExterna.Nome = Influencia)
        INSERT INTO Noticia 
        	VALUES (id,Manchete , Descricao, Consequencia, Popularidade, Data, Piada, Influencia);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_PalavrasChave (Nome VARCHAR(30), Idioma VARCHAR(15))
 
      RETURNS void AS $$
      BEGIN
        INSERT INTO PalavrasChave
         VALUES (Nome, Idioma);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Local (Sigla CHAR(2), Nome VARCHAR(10), Complemento VARCHAR(50))
 
      RETURNS void AS $$
      BEGIN
        INSERT INTO Local
         VALUES (Sigla, Nome, Complemento);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_FonteConfiavel (Nome VARCHAR(30), Descricao VARCHAR(200)) 
      RETURNS void AS $$
      BEGIN
        INSERT INTO FonteConfiavel
         VALUES (Nome, Descricao);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Ocupacao (id INTEGER,Emprego VARCHAR(40), Descricao VARCHAR(100))
      RETURNS void AS $$
      BEGIN
        INSERT INTO Ocupacao
         VALUES (id,Emprego, Descricao);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Pessoa (id INTEGER,Nome VARCHAR(50), Idade INTEGER, OcupacaoId INTEGER)
      RETURNS void AS $$
      BEGIN
        INSERT INTO Pessoa
         VALUES (id,Nome, Idade, OcupacaoId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_CategoriaMidia (id INTEGER,Nome VARCHAR(30), Descricao VARCHAR(60))
      RETURNS void AS $$
      BEGIN
        INSERT INTO CategoriaMidia
         VALUES (id,Nome, Descricao);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Midia (id INTEGER,Nome VARCHAR(50), Descricao VARCHAR(250), CategoriaId INTEGER)
      RETURNS void AS $$
      BEGIN
        INSERT INTO Midia
         VALUES (id,Nome, Descricao, CategoriaId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Idioma (id INTEGER,Nome VARCHAR(60))
      RETURNS void AS $$
      BEGIN
        INSERT INTO Idioma
         VALUES (id,Nome);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_FonteConfiavel_Noticia (NoticiaId INTEGER, FonteId INTEGER)
  RETURNS void AS $$
      BEGIN
        INSERT INTO FonteConfiavel_Noticia
         VALUES (NoticiaId, FonteId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Influencia_Noticia (NoticiaId INTEGER, InfluenciaId INTEGER)
  RETURNS void AS $$
      BEGIN
        INSERT INTO Influencia_Noticia
         VALUES (NoticiaId, InfluenciaId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Midia_Noticia (NoticiaId INTEGER, MidiaId INTEGER)
	RETURNS void AS $$
      BEGIN
        INSERT INTO Midia_Noticia
         VALUES (NoticiaId, MidiaId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_PalavrasChave_Noticia (NoticiaId INTEGER, PalavrasChaveId INTEGER)
      RETURNS void AS $$
      BEGIN
        INSERT INTO PalavrasChave_Noticia
         VALUES (NoticiaId, PalavrasChaveId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Local_Noticia (NoticiaId INTEGER, LocalId CHAR(2))
      RETURNS void AS $$
      BEGIN
        INSERT INTO Local_Noticia
         VALUES (NoticiaId, 'LocalId');
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_CategoriaNoticia_Noticia(NoticiaId INTEGER, CategoriaId INTEGER) 
      RETURNS void AS $$
      BEGIN
        INSERT INTO CategoriaNoticia_Noticia
         VALUES (NoticiaId, CategoriaId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Autor_Noticia (NoticiaId INTEGER, AutorId INTEGER)
 
      RETURNS void AS $$
      BEGIN
        INSERT INTO Autor_Noticia
         VALUES (NoticiaId, AutorId);
      END;
      $$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION Insere_Vitima_Noticia (NoticiaId INTEGER, VitimaId INTEGER)
 
      RETURNS void AS $$
      BEGIN
        INSERT INTO Vitima_Noticia
         VALUES (NoticiaId, VitimaId);
      END;
      $$ LANGUAGE 'plpgsql';


SELECT Insere_CategoriaNoticia(id,'Nome','Descricao');
SELECT Insere_InfluenciaExterna(id,'Nome');
SELECT Insere_Noticia(id,'Manchete','Descricao','Consequencia', Popularidade, Data, Piada(0-1));
SELECT Insere_PalavrasChave('Nome','Idioma');
SELECT Insere_Local('Sigla','Nome', 'Complemento');
SELECT Insere_FonteConfiavel('Nome','Descricao');
SELECT Insere_Ocupacao(id,'Emprego','Descricao');
SELECT Insere_Pessoa(id,'Nome',Idade, OcupacaoId);
SELECT Insere_CategoriaMidia(id,'Nome','Descricao');
SELECT Insere_Midia(id,'Nome','Descricao', CategoriaId);
SELECT Insere_Midia(id,'Nome');
SELECT Insere_FonteConfiavel_Noticia(NoticiaId, FonteId);
SELECT Insere_Influencia_Noticia (NoticiaId, InfluenciaId);
SELECT Insere_Midia_Noticia(NoticiaId, MidiaId);
SELECT Insere_PalavrasChave_Noticia(NoticiaId, PalavrasChaveId);
SELECT Insere_Local_Noticia(NoticiaId,LocalId);
SELECT Insere_CategoriaNoticia_Noticia(NoticiaId,CategoriaId);
SELECT Insere_Autor_Noticia(NoticiaId,AutorId);
SELECT Insere_Vitima_Noticia(NoticiaId,VitimaId);
