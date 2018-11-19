import psycopg2
import Model as bd
# from View import PrintView as show


# def doQuery(conn):
# 	cur = conn.cursor()
# 	cur.execute("SELECT fname, lname FROM Employee")
# 	for firstname, lastname in cur.fetchall():
# 		print(firstname, lastname)
# 	cur.close()


def main():
	try:
		connect_str = "dbname='Projeto' user='admin' host='localhost' " + \
			"password='123'"

		conn = psycopg2.connect(connect_str)
		bd.CreateTables(conn)
		bd.Insert("CategoriaNoticia", conn, "'Violência'",
		"'Agressão física e/ou moral a própria pessoa ou a terceiros relacionados.'")
		# print("|Teste do Banco de Dados de Fake News|")
		# View = show()
		# View.printTableCategoryNews(conn)



		conn.commit()


	except Exception as e:
		print("Uh oh, can't connect. Invalid dbname, user or password?")
		print(e)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	main()
