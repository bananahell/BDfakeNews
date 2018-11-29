from PyQt5 import QtWidgets, QtSql

table_columns = {"categorianoticia":  ("id", "nome", "descricao"),
                 "noticia":           ("id", "manchete", "descricao", "consequencia", "popularidade", "data", "piada"),
                 "Influenciaexterna": ("id", "nome"),
                 "palavraschave":     ("nome, idioma"),
                 "local":             ("sigla", "nome", "complemento"),
                 "fonteconfiavel":    ("nome", "descricao"),
                 "ocupacao":          ("id", "emprego", "descricao"),
                 "pessoa":            ("id", "nome", "idade", "ocupacaoid"),
                 "categoriamidia":    ("id", "nome", "descricao"),
                 "midia":             ("id", "nome", "descricao", "categoriaid"),

                 "fonteconfiavel_noticia":    ("noticiaid", "fonteid"),
                 "influenciaexterna_noticia": ("noticiaid", "influenciaid"),
                 "midia_noticia":             ("noticiaid", "midiaid"),
                 "palavraschave_noticia":     ("noticiaid", "palavraschaveid"),
                 "local_noticia":             ("noticiaid", "localid"),
                 "categorianoticia_noticia":  ("noticiaid", "categorianoticia_noticia"),
                 "autor_noticia":             ("noticiaid", "autorid"),
                 "vitima_noticia":            ("noticiaid", "vitimaid")}


def Insert(TableName, conn, *args):
    string_args = list(map(lambda a: str(a), args))
    cursor = conn.cursor()
    sql = """INSERT INTO """ + TableName + " VALUES(" + (", ".join(string_args)) + """);"""
    cursor.execute(sql)

    cursor.close()


def Select(whichtable, arg):

    model = QtSql.QSqlQueryModel()
    sql = "SELECT * FROM {table} WHERE "
    sql += "::text LIKE '%{search}%' OR ".join(table_columns[whichtable])
    sql += "::text LIKE '%{search}%'"
    newsql = sql.format(table=whichtable, search=arg)
    print(newsql)
    model.setQuery(newsql)
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.show()
    return model

