class PrintView():

	table_columns = {"CategoriaNoticia": ("Id", "Nome", "Descrição")}


	def printTableCategoryNews(self, conn):
		cursor = conn.cursor()
		print(*self.table_columns['CategoriaNoticia'])
		sql = """SELECT * FROM CategoriaNoticia;"""
		cursor.execute(sql)
		print(cursor.fetchall())

		cursor.close()
