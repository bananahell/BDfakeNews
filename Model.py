from PyQt5 import QtWidgets, QtSql

table_columns = {"categorianoticia":  ("id", "nomecategoria", "descricaocategoria"),
                 "noticia":           ("id", "manchete", "descricao", "consequencia", "popularidade", "data", "piada"),
                 "influenciaexterna": ("id", "nome"),
                 "palavraschave":     ("nome", "idioma"),
                 "local":             ("sigla", "nome", "complemento"),
                 "fonteconfiavel":    ("id", "nome", "descricaofonte"),
                 "ocupacao":          ("id", "emprego", "descricao"),
                 "pessoa":            ("id", "nome", "idade", "ocupacaoid"),
                 "categoriamidia":    ("id", "nomecategoria", "descricaocategoria"),
                 "midia":             ("id", "nome", "descricaomidia", "categoriaid"),
                 "idioma":            ("id", "nome"),

                 "full_Noticia": ("categoriaid", "id", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "autorid", "vitimaid", "localid", "palavraschaveid", "fonteid", "midiaid", "influenciaid"),
                 "autor_Vitima": ("autorid", "nome", "idade", "ocupacaoid", "noticiaid", "vitimaid"),
                 "pessoa_Ocupacao": ("id", "nome", "idade", "ocupacaoid", "emprego", "descricao"),
                 "midia_CategoriaM": ("id", "nome", "descricaomidia", "categoriaid", "nomecategoria", "descricaocategoria"),
                 "noticia_CategoriaN": ("noticiaid", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "categoriaid", "nomecategoria", "descricaocategoria"),
                 "full_Influencia_Noticia": ("noticiaid", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "incluenciaid", "nome"),
                 "full_Midia_Noticia": ("noticiaid", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "midiaid", "nome", "descricaomidia", "categoriaid"),
                 "full_FonteConfiavel_Noticia": ("noticiaid", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "fonteid", "nome", "descricaofonte"),
                 "full_PalavrasChave_Noticia": ("noticiaid", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "palavraschaveid", "idioma"),
                 "full_Local_Noticia": ("noticiaid", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "localid", "nome", "complemento"),

                 "fonteconfiavel_noticia":    ("noticiaid", "fonteid"),
                 "influencia_noticia": ("noticiaid", "influenciaid"),
                 "midia_noticia":             ("noticiaid", "midiaid"),
                 "palavraschave_noticia":     ("noticiaid", "palavraschaveid"),
                 "local_noticia":             ("noticiaid", "localid"),
                 "categorianoticia_noticia":  ("noticiaid", "categoriaid"),
                 "autor_noticia":             ("noticiaid", "autorid"),
                 "vitima_noticia":            ("noticiaid", "vitimaid")}

table_keys = {"categorianoticia": "id",
              "noticia": "id",
              "categoriamidia": "id",
              "midia": "id",
              "pessoa": "id",
              "palavraschave": "Nome",
              "local": "Sigla",
              "fonteconfiavel": "id",
              "ocupacao": "id",
              "influenciaexterna": "id",
              "idioma": "id"}

procedures_insert = {"categorianoticia": "Insere_CategoriaNoticia",
                     "noticia": "Insere_Noticia",
                     "categoriamidia": "Insere_CategoriaMidia",
                     "midia": "Insere_Midia",
                     "pessoa": "Insere_Pessoa",
                     "palavraschave": "Insere_PalavrasChave",
                     "local": "Insere_Local",
                     "fonteconfiavel": "Insere_FonteConfiavel",
                     "ocupacao": "Insere_Ocupacao",
                     "influenciaexterna": "Insere_InfluenciaExterna",
                     "idioma": "Insere_Idioma",
                     
                     "autor_noticia": "Insere_Autor_Noticia",
                     "vitima_noticia": "Insere_Vitima_Noticia",
                     "categorianoticia_noticia": "Insere_CategoriaNoticia_Noticia",
                     "local_noticia": "Insere_Local_Noticia",
                     "palavraschave_noticia": "Insere_PalavrasChave_Noticia",
                     "fonteconfiavel_noticia": "Insere_FonteConfiavel_Noticia",
                     "midia_noticia": "Insere_Midia_Noticia",
                     "influencia_noticia": "Insere_Influencia_Noticia"}

procedures_delete = {"categorianoticia": "Delete_CategoriaNoticia",
                     "noticia": "Delete_Noticia",
                     "categoriamidia": "Delete_CategoriaMidia",
                     "midia": "Delete_Midia",
                     "pessoa": "Delete_Pessoa",
                     "palavraschave": "Delete_PalavrasChave",
                     "local": "Delete_Local",
                     "fonteconfiavel": "Delete_FonteConfiavel",
                     "ocupacao": "Delete_Ocupacao",
                     "influenciaexterna": "Delete_InfluenciaExterna",
                     "idioma": "Delete_Idioma",

                     "autor_noticia": "Delete_Autor_Noticia",
                     "vitima_noticia": "Delete_Vitima_Noticia",
                     "categorianoticia_noticia": "Delete_CategoriaNoticia_Noticia",
                     "local_noticia": "Delete_Local_Noticia",
                     "palavraschave_noticia": "Delete_PalavrasChave_Noticia",
                     "fonteconfiavel_noticia": "Delete_FonteConfiavel_Noticia",
                     "midia_noticia": "Delete_Midia_Noticia",
                     "influencia_noticia": "Delete_Influencia_Noticia"}


def Insert(TableName, conn, *args):
   try:
      string_args = list(map(lambda a: str(a), args))
      cursor = conn.cursor()
      sql = """SELECT """ + procedures_insert[TableName] + (", ".join(string_args)) + """;"""
      cursor.execute(sql)
      conn.commit()
   
   except Exception as e:
      print("Problem ocurred during insert")
      print(e)
   finally:
      cursor.close()


def Delete(TableName, conn, *args):
   try:
      string_args = list(map(lambda a: str(a), args))
      cursor = conn.cursor()
      if(len(args) == 1):
         aux = str(args[0][0])
         sql = """SELECT """ + procedures_delete[TableName] + "(" + aux + """);"""
      else:
         sql = """SELECT """ + procedures_delete[TableName] + (", ".join(string_args)) + """;"""
         
      cursor.execute(sql)
      conn.commit()
   
   except Exception as e:
      print("Problem ocurred during delete")
      print(e)
   finally:
      cursor.close()


def Count(TableName, conn):
   cursor = conn.cursor()
   sql = """SELECT COUNT(""" + table_keys[TableName] + ") FROM " + TableName + """;"""
   cursor.execute(sql)
   aux = cursor.fetchall()
   return (aux[0][0])


def Select(whichtable, arg):

   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM {table} WHERE "
   sql += "::text LIKE '%{search}%' OR ".join(table_columns[whichtable])
   sql += "::text LIKE '%{search}%'"
   newsql = sql.format(table=whichtable, search=arg)
   model.setQuery(newsql)
   return model


def Full_Noticia():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Full_Noticia"
   model.setQuery(sql)
   return model


def Autor_Vitima():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Autor_Vitima"
   model.setQuery(sql)
   return model


def Pessoa_Ocupacao():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Pessoa_Ocupacao"
   model.setQuery(sql)
   return model

def Midia_CategoriaM():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Midia_CategoriaM"
   model.setQuery(sql)
   return model


def Noticia_CategoriaN():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Noticia_CategoriaN"
   model.setQuery(sql)
   return model


def Influencia_Noticia():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Full_Influencia_Noticia"
   model.setQuery(sql)
   return model


def Midia_Noticia():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Full_Midia_Noticia"
   model.setQuery(sql)
   return model


def FonteConfiavel_Noticia():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Full_FonteConfiavel_Noticia"
   model.setQuery(sql)
   return model


def PalavrasChave_Noticia():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Full_PalavrasChave_Noticia"
   model.setQuery(sql)
   return model


def Local_Noticia():
   model = QtSql.QSqlQueryModel()
   sql = "SELECT * FROM Full_Local_Noticia"
   model.setQuery(sql)
   return model

