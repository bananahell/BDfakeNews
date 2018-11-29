from PyQt5 import QtWidgets, QtSql

table_columns = {"categorianoticia": ("id", "nome", "descricao"),
                "noticia": ("id", "manchete", "descricao", "consequencia", "popularidade", "data", "piada", "influenciaid")}


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
   
