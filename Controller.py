import Model
import re


def ControllerSearchButton(whichtable, searchText):
	return Model.Select(whichtable, searchText)


def ControllerInsertSubmitButton(whichtable, conn, *args):
	return Model.Insert(whichtable, conn, args)


def ControllerDeleteSubmitButton(whichtable, conn, *args):
	return Model.Delete(whichtable, conn, args)


def ControllerFull_Noticia():
	return Model.Full_Noticia()


def ControllerAutor_Vitima():
	return Model.Autor_Vitima()


def ControllerPessoa_Ocupacao():
	return Model.Pessoa_Ocupacao()


def ControllerMidia_CategoriaM():
	return Model.Midia_CategoriaM()


def ControllerNoticia_CategoriaN():
	return Model.Noticia_CategoriaN()


def ControllerInfluencia_Noticia():
	return Model.Influencia_Noticia()


def ControllerMidia_Noticia():
	return Model.Midia_Noticia()


def ControllerFonteConfiavel_Noticia():
	return Model.FonteConfiavel_Noticia()


def ControllerPalavrasChave_Noticia():
	return Model.PalavrasChave_Noticia()


def ControllerLocal_Noticia():
	return Model.Local_Noticia()


def ControllerCountTable(whichtable, conn):
	return Model.Count(whichtable, conn)

def CheckField(string):
	cpfPattern = r"(?:^\d{3}.\d{3}.\d{3}-\d{2}$)"
	# phonePattern = r"(?:\(\d{2}\)\d{5}-\d{4}$)"
	matches = re.search(cpfPattern, string, re.IGNORECASE)
	if matches:
		print("Match: " + matches.group(0))
		return 0
	else:
		print("No match")
		return -1  


