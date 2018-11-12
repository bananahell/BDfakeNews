import psycopg2
import Model as bd


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
		bd.Insert("Employee", conn, 2, "'Hugo'", "'Fonseca'")
		print("|Teste do Banco de Dados de Fake News|")



		conn.commit()


	except Exception as e:
		print("Uh oh, can't connect. Invalid dbname, user or password?")
		print(e)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	main()
