

def CreateTables(conn):
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Employee (
        Id INTEGER PRIMARY KEY,
        fname VARCHAR(30) NOT NULL,
        lname VARCHAR(30) NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Notícia (
        Id INTEGER PRIMARY KEY,
        Manchete VARCHAR(100) NOT NULL,
        Descrição VARCHAR(200) NOT NULL,
        Consequência VARCHAR(200) NOT NULL,
        Popularidade INTEGER
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaMídia (
        Id INTEGER PRIMARY KEY,
        Nome NOT NULL
        );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Mídia (
        Id INTEGER PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL
        );""")

    cursor.close()


def Insert(TableName, conn, *args):
    string_args = list(map(lambda a: str(a), args))
    cursor = conn.cursor()
    sql = """INSERT INTO """ + TableName + " VALUES(" + (", ".join(string_args)) + """);"""
    cursor.execute(sql)

    cursor.close()
