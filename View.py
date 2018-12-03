# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import Controller
import Model
import psycopg2
from PyQt5.QtCore import Qt

table_columns_tabs = {(0, 0, 0): "categorianoticia",
                    (0, 0, 1): "noticia",
                    (0, 0, 2): "categoriamidia",
                    (0, 0, 3): "midia",
                    (0, 0, 4): "pessoa",
                    (0, 0, 5): "palavraschave",
                    (0, 0, 6): "local",
                    (0, 0, 7): "fonteconfiavel",
                    (0, 0, 8): "ocupacao",
                    (0, 0, 9): "influenciaexterna",
                    (0, 0, 10): "idioma",

                    (1, 1, 0): "full_Noticia",
                    (1, 1, 0): "autor_Vitima",
                    (1, 2, 0): "pessoa_Ocupacao",
                    (1, 3, 0): "midia_CategoriaM",
                    (1, 4, 0): "noticia_CategoriaN",
                    (1, 5, 0): "full_Influencia_Noticia",
                    (1, 6, 0): "full_Midia_Noticia",
                    (1, 7, 0): "full_FonteConfiavel_Noticia",
                    (1, 8, 0): "full_PalavrasChave_Noticia",
                    (1, 9, 0): "full_Local_Noticia",

                    (2, 0, 0): "autor_noticia",
                    (2, 0, 1): "vitima_noticia",
                    (2, 0, 2): "influencia_noticia",
                    (2, 0, 3): "midia_noticia",
                    (2, 0, 4): "fonteconfiavel_noticia",
                    (2, 0, 5): "palavraschave_noticia",
                    (2, 0, 6): "local_noticia",
                    (2, 0, 7): "categorianoticia_noticia"}

table_columns_view = {(0, 0, 0):  ("ID", "Nome", "Descrição"),
                      (0, 0, 1):  ("ID", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada"),
                      (0, 0, 2):  ("ID", "Nome", "Descrição"),
                      (0, 0, 3):  ("ID", "Nome", "Descrição", "Índice da Categoria"),
                      (0, 0, 4):  ("ID", "Nome", "Idade", "Índice de Ocupação"),
                      (0, 0, 5):  ("Nome", "Idioma"),
                      (0, 0, 6):  ("Sigla", "Nome", "Complemento"),
                      (0, 0, 7):  ("Nome", "Descrição"),
                      (0, 0, 8):  ("ID", "Emprego", "Descrição"),
                      (0, 0, 9):  ("ID", "Nome"),
                      (0, 0, 10): ("ID", "Nome"),
                      
                      (1, 0, 0):  ("Índice da Categoria da Nóticia", "Índice da Notícia", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "Índice do Autor", "Índice da Vítima", "Índice do Local", "Índice da Palavra Chave", "Índice da Fonte Confiável", "Índice da Mídia", "Índice da Influência Externa"),
                      (1, 1, 0):  ("Índice do Autor", "Nome", "Idade", "Índice da Ocupação", "Índice da Notícia", "Índice da Vítima"),
                      (1, 2, 0):  ("Índice da Pessoa", "Nome", "Idade", "Índice da Ocupação", "Emprego", "Descrição Emprego"),
                      (1, 3, 0):  ("Índice da Mídia", "Nome", "Descrição", "Índice da Categoria", "Nome da Categoria"),
                      (1, 4, 0):  ("Índice da Notícia", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "Índice da Categoria", "Nome da Categoria", "Descrição da Categoria"),
                      (1, 5, 0):  ("Índice da Notícia", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "Índice da Influência", "Nome da Influência"),
                      (1, 6, 0):  ("Índice da Notícia", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "Índice da Midia", "Nome da Mídia", "Descrição da Mídia", "Índice da Categoria da Mídia"),
                      (1, 7, 0):  ("Índice da Notícia", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "Índice da Fonte", "Nome da Fonte", "Descrição da Fonte"),
                      (1, 8, 0):  ("Índice da Notícia", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "Palavra", "Índice do Idioma"),
                      (1, 9, 0):  ("Índice da Notícia", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "Sigla do Local", "Nome do Local", "Complemento do Local"),

                      (2, 0, 0): ("Índice da Notícia", "Índice do Autor"),
                      (2, 0, 1): ("Índice da Nóticia", "Índice da Vítima"),
                      (2, 0, 2): ("Índice da Notícia", "Índice da Influência Externa"),
                      (2, 0, 3): ("Índice da Notícia", "Índice da Mídia"),
                      (2, 0, 4): ("Índice da Notícia", "Índice da Fonte Confiável"),
                      (2, 0, 5): ("Índice da Notícia", "Índice da Palavra Chave"),
                      (2, 0, 6): ("Índice da Notícia", "Índice do Local"),
                      (2, 0, 7): ("Índice da Notícia", "Índice da Categoria da Notícia")}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 700)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.modesTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.modesTabs.setGeometry(QtCore.QRect(0, 0, 1300, 675))
        self.modesTabs.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.modesTabs.setTabPosition(QtWidgets.QTabWidget.West)
        self.modesTabs.setObjectName("modesTabs")

        self.where = 0
        self.page = 0

        # SELECTION SECTION

        self.Selection = QtWidgets.QWidget()
        self.Selection.setObjectName("Selection")

        self.tabsSelection = QtWidgets.QTabWidget(self.Selection)
        self.tabsSelection.setGeometry(QtCore.QRect(0, 130, 1251, 545))
        self.tabsSelection.setObjectName("tabsSelection")

        self.relationalButton = QtWidgets.QPushButton(self.Selection)
        self.relationalButton.setGeometry(QtCore.QRect(990, 40, 250, 29))
        self.relationalButton.setObjectName("relationalButton")
        self.relationalButton.clicked.connect(self.clickrelational)

        self.normalButton = QtWidgets.QPushButton(self.Selection)
        self.normalButton.setGeometry(QtCore.QRect(990, 75, 250, 29))
        self.normalButton.setObjectName("normalButton")
        self.normalButton.clicked.connect(self.clicknormal)

        self.refreshButton = QtWidgets.QPushButton(self.Selection)
        self.refreshButton.setGeometry(QtCore.QRect(885, 75, 101, 29))
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.clickrefresh)

        self.searchButton = QtWidgets.QPushButton(self.Selection)
        self.searchButton.setGeometry(QtCore.QRect(885, 40, 101, 29))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.clicksearch)

        self.Full_NoticiaButton = QtWidgets.QPushButton(self.Selection)
        self.Full_NoticiaButton.setGeometry(QtCore.QRect(63, 75, 140, 21))
        self.Full_NoticiaButton.setObjectName("Full_NoticiaButton")
        self.Full_NoticiaButton.clicked.connect(self.clickFull_Noticia)

        self.Autor_VitimaButton = QtWidgets.QPushButton(self.Selection)
        self.Autor_VitimaButton.setGeometry(QtCore.QRect(63, 100, 140, 21))
        self.Autor_VitimaButton.setObjectName("Full_Autor_VitimaButton")
        self.Autor_VitimaButton.clicked.connect(self.clickAutor_Vitima)

        self.Pessoa_OcupacaoButton = QtWidgets.QPushButton(self.Selection)
        self.Pessoa_OcupacaoButton.setGeometry(QtCore.QRect(211, 75, 140, 21))
        self.Pessoa_OcupacaoButton.setObjectName("Pessoa_OcupacaoButton")
        self.Pessoa_OcupacaoButton.clicked.connect(self.clickPessoa_Ocupacao)

        self.Midia_CategoriaMButton = QtWidgets.QPushButton(self.Selection)
        self.Midia_CategoriaMButton.setGeometry(QtCore.QRect(211, 100, 140, 21))
        self.Midia_CategoriaMButton.setObjectName("Midia_CategoriaMButton")
        self.Midia_CategoriaMButton.clicked.connect(self.clickMidia_CategoriaM)

        self.Noticia_CategoriaNButton = QtWidgets.QPushButton(self.Selection)
        self.Noticia_CategoriaNButton.setGeometry(QtCore.QRect(359, 75, 140, 21))
        self.Noticia_CategoriaNButton.setObjectName("Noticia_CategoriaNButton")
        self.Noticia_CategoriaNButton.clicked.connect(self.clickNoticia_CategoriaN)

        self.Influencia_NoticiaButton = QtWidgets.QPushButton(self.Selection)
        self.Influencia_NoticiaButton.setGeometry(QtCore.QRect(359, 100, 140, 21))
        self.Influencia_NoticiaButton.setObjectName("Influencia_NoticiaButton")
        self.Influencia_NoticiaButton.clicked.connect(self.clickInfluencia_Noticia)

        self.Midia_NoticiaButton = QtWidgets.QPushButton(self.Selection)
        self.Midia_NoticiaButton.setGeometry(QtCore.QRect(507, 75, 140, 21))
        self.Midia_NoticiaButton.setObjectName("Midia_NoticiaButton")
        self.Midia_NoticiaButton.clicked.connect(self.clickMidia_Noticia)

        self.FonteConfiavel_NoticiaButton = QtWidgets.QPushButton(self.Selection)
        self.FonteConfiavel_NoticiaButton.setGeometry(QtCore.QRect(507, 100, 140, 21))
        self.FonteConfiavel_NoticiaButton.setObjectName("FonteConfiavel_NoticiaButton")
        self.FonteConfiavel_NoticiaButton.clicked.connect(self.clickFonteConfiavel_Noticia)

        self.PalavrasChave_NoticiaButton = QtWidgets.QPushButton(self.Selection)
        self.PalavrasChave_NoticiaButton.setGeometry(QtCore.QRect(655, 75, 140, 21))
        self.PalavrasChave_NoticiaButton.setObjectName("PalavrasChave_NoticiaButton")
        self.PalavrasChave_NoticiaButton.clicked.connect(self.clickPalavrasChave_Noticia)

        self.Local_NoticiaButton = QtWidgets.QPushButton(self.Selection)
        self.Local_NoticiaButton.setGeometry(QtCore.QRect(655, 100, 140, 21))
        self.Local_NoticiaButton.setObjectName("Local_NoticiaButton")
        self.Local_NoticiaButton.clicked.connect(self.clickLocal_Noticia)

        self.searchField = QtWidgets.QLineEdit(self.Selection)
        self.searchField.setGeometry(QtCore.QRect(10, 40, 871, 29))
        self.searchField.setObjectName("searchField")

        self.searchLabel = QtWidgets.QLabel(self.Selection)
        self.searchLabel.setGeometry(QtCore.QRect(10, 20, 391, 17))
        self.searchLabel.setObjectName("searchLabel")

        self.viewsLabel = QtWidgets.QLabel(self.Selection)
        self.viewsLabel.setGeometry(QtCore.QRect(10, 90, 50, 17))
        self.viewsLabel.setObjectName("viewsLabel")


        self.modesTabs.addTab(self.Selection, "")

        # INSERTION SECTION

        self.Insertion = QtWidgets.QWidget()
        self.Insertion.setObjectName("Insertion")
        self.instruction = QtWidgets.QLabel(self.Insertion)
        self.instruction.setGeometry(QtCore.QRect(10, 30, 591, 17))
        self.instruction.setObjectName("instruction")

        self.tabsInsertion = QtWidgets.QTabWidget(self.Insertion)
        self.tabsInsertion.setGeometry(QtCore.QRect(0, 75, 1251, 600))
        self.tabsInsertion.setObjectName("tabsInsertion")

        self.insertrelationalButton = QtWidgets.QPushButton(self.Insertion)
        self.insertrelationalButton.setGeometry(QtCore.QRect(610, 26, 250, 29))
        self.insertrelationalButton.setObjectName("relationalButton")
        self.insertrelationalButton.clicked.connect(self.clickinsertrelational)

        self.insertnormalButton = QtWidgets.QPushButton(self.Insertion)
        self.insertnormalButton.setGeometry(QtCore.QRect(866, 26, 250, 29))
        self.insertnormalButton.setObjectName("normalButton")
        self.insertnormalButton.clicked.connect(self.clickinsertnormal)
        
        self.modesTabs.addTab(self.Insertion, "")

        # DELETION SECTION
        
        self.Deletion = QtWidgets.QWidget()
        self.Deletion.setObjectName("Deletion")
        self.instruction_2 = QtWidgets.QLabel(self.Deletion)
        self.instruction_2.setGeometry(QtCore.QRect(10, 30, 691, 17))
        self.instruction_2.setObjectName("instruction_2")

        self.tabsDeletion = QtWidgets.QTabWidget(self.Deletion)
        self.tabsDeletion.setGeometry(QtCore.QRect(0, 75, 1251, 600))
        self.tabsDeletion.setObjectName("tabsDeletion")

        self.deleterelationalButton = QtWidgets.QPushButton(self.Deletion)
        self.deleterelationalButton.setGeometry(QtCore.QRect(551, 24, 250, 29))
        self.deleterelationalButton.setObjectName("relationalButton")
        self.deleterelationalButton.clicked.connect(self.clickdeleterelational)

        self.deletenormalButton = QtWidgets.QPushButton(self.Deletion)
        self.deletenormalButton.setGeometry(QtCore.QRect(807, 24, 250, 29))
        self.deletenormalButton.setObjectName("normalButton")
        self.deletenormalButton.clicked.connect(self.clickdeletenormal)

        self.modesTabs.addTab(self.Deletion, "")

        # UPDATE SECTION
        
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.modesTabs.addTab(self.Update, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.modesTabs.setCurrentIndex(0)
        self.tabsSelection.setCurrentIndex(0)
        self.tabsInsertion.setCurrentIndex(1)
        self.tabsDeletion.setCurrentIndex(2)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def clickdeleterelational(self):
        self.tabsInsertion.clear()

        self.where = 2
        self.page = 0


    def clicksubmitdelete(self):
        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)

        self.statusbar.showMessage("Carregando...")
        whichtable = table_columns_tabs[self.where,self.page, self.tabsDeletion.currentIndex()]
        if whichtable is "categorianoticia":
            Id = str(self.spinBox_categorianoticiaid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "noticia":
            Id = str(self.spinBox_noticiaid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "categoriamidia":
            Id = str(self.spinBox_categoriamidiaid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "midia":
            Id = str(self.spinBox_categoriamidiaid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "pessoa":
            Id = str(self.spinBox_pessoaid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "palavraschave":
            palavra = self.spinBox_palavraschaveid.text()
            Controller.ControllerDeleteSubmitButton(whichtable, conn, palavra)
            self.statusbar.showMessage("Ready")
        elif whichtable is "local":
            sigla = self.spinBox_categorianoticiaid.text()
            Controller.ControllerDeleteSubmitButton(whichtable, conn, sigla)
            self.statusbar.showMessage("Ready")
        elif whichtable is "fonteconfiavel":
            Id = str(self.spinBox_fonteconfiavelid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "ocupacao":
            Id = str(self.spinBox_ocupacaoid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "influenciaexterna":
            Id = str(self.spinBox_influeciaexternaid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")
        elif whichtable is "idioma":
            Id = str(self.spinBox_idiomaid.value())
            Controller.ControllerDeleteSubmitButton(whichtable, conn, Id)
            self.statusbar.showMessage("Ready")

    
    def clickdeletenormal(self):

        self.tabsDeletion.clear()

        self.where = 0
        self.page = 0

        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)

        self.categorianoticia_3 = QtWidgets.QWidget()
        self.categorianoticia_3.setEnabled(True)
        self.categorianoticia_3.setObjectName("categorianoticia_3")

        self.searchLabel_categorianoticiaid = QtWidgets.QLabel(
            self.categorianoticia_3)
        self.searchLabel_categorianoticiaid.setGeometry(
            QtCore.QRect(10, 25, 220, 20))
        self.searchLabel_categorianoticiaid.setObjectName(
            "searchLabel_categorianoticiaid")


        self.spinBox_categorianoticiaid = QtWidgets.QSpinBox(
            self.categorianoticia_3)
        self.spinBox_categorianoticiaid.setGeometry(226, 26, 61, 27)
        self.spinBox_categorianoticiaid.setMaximum(
            Controller.ControllerCountTable("categorianoticia", conn) - 1)
        self.spinBox_categorianoticiaid.setObjectName("spinBox_categorianoticiaid")

        self.submitButton_categorianoticia = QtWidgets.QPushButton(
            self.categorianoticia_3)
        self.submitButton_categorianoticia.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_categorianoticia.setObjectName(
            "submitButton_categorianoticia")
        self.submitButton_categorianoticia.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.categorianoticia_3, "")

        self.noticia_3 = QtWidgets.QWidget()
        self.noticia_3.setObjectName("noticia_3")

        self.searchLabel_noticiaid = QtWidgets.QLabel(
            self.noticia_3)
        self.searchLabel_noticiaid.setGeometry(
            QtCore.QRect(10, 25, 120, 20))
        self.searchLabel_noticiaid.setObjectName(
            "searchLabel_noticiaid")

        self.spinBox_noticiaid = QtWidgets.QSpinBox(
            self.noticia_3)
        self.spinBox_noticiaid.setGeometry(136, 26, 61, 27)
        self.spinBox_noticiaid.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid.setObjectName(
            "spinBox_noticiaid")
        
        self.submitButton_noticia_2 = QtWidgets.QPushButton(self.noticia_3)
        self.submitButton_noticia_2.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_noticia_2.setObjectName("submitButton_noticia_2")
        self.submitButton_noticia_2.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.noticia_3, "")

        self.categoriamidia_3 = QtWidgets.QWidget()
        self.categoriamidia_3.setEnabled(True)
        self.categoriamidia_3.setObjectName("categoriamidia_3")

        self.searchLabel_categoriamidiaid = QtWidgets.QLabel(
            self.categoriamidia_3)
        self.searchLabel_categoriamidiaid.setGeometry(
            QtCore.QRect(10, 25, 220, 20))
        self.searchLabel_categoriamidiaid.setObjectName(
            "searchLabel_categoriamidiaid")

        self.spinBox_categoriamidiaid = QtWidgets.QSpinBox(
            self.categoriamidia_3)
        self.spinBox_categoriamidiaid.setGeometry(226, 26, 61, 27)
        self.spinBox_categoriamidiaid.setMaximum(
            Controller.ControllerCountTable("categoriamidia", conn) - 1)
        self.spinBox_categoriamidiaid.setObjectName(
            "spinBox_categoriamidiaid")

        self.submitButton_categoriamidia = QtWidgets.QPushButton(
            self.categoriamidia_3)
        self.submitButton_categoriamidia.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_categoriamidia.setObjectName(
            "submitButton_categoriamidia")
        self.submitButton_categoriamidia.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.categoriamidia_3, "")

        self.midia_3 = QtWidgets.QWidget()
        self.midia_3.setEnabled(True)
        self.midia_3.setObjectName("midia_3")

        self.searchLabel_midiaid = QtWidgets.QLabel(
            self.midia_3)
        self.searchLabel_midiaid.setGeometry(
            QtCore.QRect(10, 25, 120, 20))
        self.searchLabel_midiaid.setObjectName(
            "searchLabel_midiaid")

        self.spinBox_midiaid = QtWidgets.QSpinBox(
            self.midia_3)
        self.spinBox_midiaid.setGeometry(136, 26, 61, 27)
        self.spinBox_midiaid.setMaximum(
            Controller.ControllerCountTable("midia", conn) - 1)
        self.spinBox_midiaid.setObjectName(
            "spinBox_midiaid")

        self.submitButton_midia = QtWidgets.QPushButton(
            self.midia_3)
        self.submitButton_midia.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_midia.setObjectName(
            "submitButton_midia")
        self.submitButton_midia.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.midia_3, "")

        self.pessoa_3 = QtWidgets.QWidget()
        self.pessoa_3.setEnabled(True)
        self.pessoa_3.setObjectName("pessoa_3")

        self.searchLabel_pessoaid = QtWidgets.QLabel(
            self.pessoa_3)
        self.searchLabel_pessoaid.setGeometry(
            QtCore.QRect(10, 25, 120, 20))
        self.searchLabel_pessoaid.setObjectName(
            "searchLabel_pessoaid")

        self.spinBox_pessoaid = QtWidgets.QSpinBox(
            self.pessoa_3)
        self.spinBox_pessoaid.setGeometry(136, 26, 61, 27)
        self.spinBox_pessoaid.setMaximum(
            Controller.ControllerCountTable("pessoa", conn) - 1)
        self.spinBox_pessoaid.setObjectName(
            "spinBox_pessoaid")

        self.submitButton_pessoa = QtWidgets.QPushButton(
            self.pessoa_3)
        self.submitButton_pessoa.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_pessoa.setObjectName(
            "submitButton_pessoa")
        self.submitButton_pessoa.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.pessoa_3, "")

        self.palavraschave_3 = QtWidgets.QWidget()
        self.palavraschave_3.setEnabled(True)
        self.palavraschave_3.setObjectName("palavraschave_3")

        self.searchLabel_palavraschaveid = QtWidgets.QLabel(
            self.palavraschave_3)
        self.searchLabel_palavraschaveid.setGeometry(
            QtCore.QRect(10, 25, 220, 20))
        self.searchLabel_palavraschaveid.setObjectName(
            "searchLabel_palavraschaveid")

        self.searchField_nomepalavra = QtWidgets.QLineEdit(
            self.palavraschave_3)
        self.searchField_nomepalavra.setGeometry(QtCore.QRect(127, 25, 200, 29))
        self.searchField_nomepalavra.setObjectName("searchField_nomepalavra")

        self.submitButton_palavraschave = QtWidgets.QPushButton(
            self.palavraschave_3)
        self.submitButton_palavraschave.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_palavraschave.setObjectName(
            "submitButton_palavraschave")
        self.submitButton_palavraschave.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.palavraschave_3, "")

        self.local_3 = QtWidgets.QWidget()
        self.local_3.setEnabled(True)
        self.local_3.setObjectName("local_3")

        self.searchLabel_localid = QtWidgets.QLabel(
            self.local_3)
        self.searchLabel_localid.setGeometry(
            QtCore.QRect(10, 25, 220, 20))
        self.searchLabel_localid.setObjectName(
            "searchLabel_localid")

        self.searchField_sigla = QtWidgets.QLineEdit(
            self.local_3)
        self.searchField_sigla.setGeometry(
            QtCore.QRect(67, 25, 200, 29))
        self.searchField_sigla.setObjectName("searchField_sigla")

        self.submitButton_local = QtWidgets.QPushButton(
            self.local_3)
        self.submitButton_local.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_local.setObjectName(
            "submitButton_local")
        self.submitButton_local.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.local_3, "")

        self.fonteconfiavel_3 = QtWidgets.QWidget()
        self.fonteconfiavel_3.setEnabled(True)
        self.fonteconfiavel_3.setObjectName("fonteconfiavel_3")

        self.searchLabel_fonteconfiavelid = QtWidgets.QLabel(
            self.fonteconfiavel_3)
        self.searchLabel_fonteconfiavelid.setGeometry(
            QtCore.QRect(10, 25, 220, 20))
        self.searchLabel_fonteconfiavelid.setObjectName(
            "searchLabel_fonteconfiavelid")

        self.spinBox_fonteconfiavelid = QtWidgets.QSpinBox(
            self.fonteconfiavel_3)
        self.spinBox_fonteconfiavelid.setGeometry(193, 26, 61, 27)
        self.spinBox_fonteconfiavelid.setMaximum(
            Controller.ControllerCountTable("fonteconfiavel", conn) - 1)
        self.spinBox_fonteconfiavelid.setObjectName(
            "spinBox_fonteconfiavelid")

        self.submitButton_fonteconfiavel = QtWidgets.QPushButton(
            self.fonteconfiavel_3)
        self.submitButton_fonteconfiavel.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_fonteconfiavel.setObjectName(
            "submitButton_fonteconfiavel")
        self.submitButton_fonteconfiavel.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.fonteconfiavel_3, "")

        self.ocupacao_3 = QtWidgets.QWidget()
        self.ocupacao_3.setEnabled(True)
        self.ocupacao_3.setObjectName("ocupacao_3")

        self.searchLabel_ocupacaoid = QtWidgets.QLabel(
            self.ocupacao_3)
        self.searchLabel_ocupacaoid.setGeometry(
            QtCore.QRect(10, 25, 220, 20))
        self.searchLabel_ocupacaoid.setObjectName(
            "searchLabel_ocupacaoid")

        self.spinBox_ocupacaoid = QtWidgets.QSpinBox(
            self.ocupacao_3)
        self.spinBox_ocupacaoid.setGeometry(193, 26, 61, 27)
        self.spinBox_ocupacaoid.setMaximum(
            Controller.ControllerCountTable("ocupacao", conn) - 1)
        self.spinBox_ocupacaoid.setObjectName(
            "spinBox_ocupacaoid")

        self.submitButton_ocupacao = QtWidgets.QPushButton(
            self.ocupacao_3)
        self.submitButton_ocupacao.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_ocupacao.setObjectName(
            "submitButton_ocupacao")
        self.submitButton_ocupacao.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.ocupacao_3, "")

        self.influenciaexterna_3 = QtWidgets.QWidget()
        self.influenciaexterna_3.setEnabled(True)
        self.influenciaexterna_3.setObjectName("influenciaexterna_3")

        self.searchLabel_influenciaexternaid = QtWidgets.QLabel(
            self.influenciaexterna_3)
        self.searchLabel_influenciaexternaid.setGeometry(
            QtCore.QRect(10, 25, 220, 20))
        self.searchLabel_influenciaexternaid.setObjectName(
            "searchLabel_influenciaexternaid")

        self.spinBox_influenciaexternaid = QtWidgets.QSpinBox(
            self.influenciaexterna_3)
        self.spinBox_influenciaexternaid.setGeometry(226, 26, 61, 27)
        self.spinBox_influenciaexternaid.setMaximum(
            Controller.ControllerCountTable("influenciaexterna", conn) - 1)
        self.spinBox_influenciaexternaid.setObjectName(
            "spinBox_influenciaexternaid")

        self.submitButton_influenciaexterna = QtWidgets.QPushButton(
            self.influenciaexterna_3)
        self.submitButton_influenciaexterna.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_influenciaexterna.setObjectName(
            "submitButton_influenciaexterna")
        self.submitButton_influenciaexterna.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.influenciaexterna_3, "")

        self.idioma_3 = QtWidgets.QWidget()
        self.idioma_3.setEnabled(True)
        self.idioma_3.setObjectName("idioma_3")

        self.searchLabel_idiomaid = QtWidgets.QLabel(
            self.idioma_3)
        self.searchLabel_idiomaid.setGeometry(
            QtCore.QRect(10, 25, 120, 20))
        self.searchLabel_idiomaid.setObjectName(
            "searchLabel_idiomaid")

        self.spinBox_idiomaid = QtWidgets.QSpinBox(
            self.idioma_3)
        self.spinBox_idiomaid.setGeometry(136, 26, 61, 27)
        self.spinBox_idiomaid.setMaximum(
            Controller.ControllerCountTable("idioma", conn) - 1)
        self.spinBox_idiomaid.setObjectName(
            "spinBox_idiomaid")

        self.submitButton_idioma = QtWidgets.QPushButton(
            self.idioma_3)
        self.submitButton_idioma.setGeometry(
            QtCore.QRect(20, 65, 101, 29))
        self.submitButton_idioma.setObjectName(
            "submitButton_idioma")
        self.submitButton_idioma.clicked.connect(
            self.clicksubmitdelete)

        self.tabsDeletion.addTab(self.idioma_3, "")


        _translate = QtCore.QCoreApplication.translate
        self.searchLabel_categorianoticiaid.setText(
            _translate("MainWindow", "Índice da Categoria da Notícia*:"))
        self.submitButton_categorianoticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.categorianoticia_3), _translate("MainWindow", "Categoria Notícia"))
        self.searchLabel_noticiaid.setText(
            _translate("MainWindow", "Índice da Notícia*:"))
        self.submitButton_noticia_2.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.noticia_3), _translate("MainWindow", "Notícia"))
        self.searchLabel_categoriamidiaid.setText(
            _translate("MainWindow", "Índice da Categoria da Mídia*:"))
        self.submitButton_categoriamidia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.categoriamidia_3), _translate("MainWindow", "Categoria Mídia"))
        self.searchLabel_midiaid.setText(
            _translate("MainWindow", "Índice da Mídia*:"))
        self.submitButton_midia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.midia_3), _translate("MainWindow", "Mídia"))
        self.searchLabel_pessoaid.setText(
            _translate("MainWindow", "Índice da Pessoa*:"))
        self.submitButton_pessoa.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.pessoa_3), _translate("MainWindow", "Pessoa"))
        self.searchLabel_palavraschaveid.setText(
            _translate("MainWindow", "Palavra Chave*:"))
        self.submitButton_palavraschave.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.palavraschave_3), _translate("MainWindow", "Palavras Chave"))
        self.searchLabel_localid.setText(
            _translate("MainWindow", "Sigla*:"))
        self.submitButton_local.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.local_3), _translate("MainWindow", "Local"))
        self.searchLabel_fonteconfiavelid.setText(
            _translate("MainWindow", "Índice da Fonte Confiável*:"))
        self.submitButton_fonteconfiavel.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.fonteconfiavel_3), _translate("MainWindow", "Fonte Confiável"))
        self.searchLabel_ocupacaoid.setText(
            _translate("MainWindow", "Índice da Ocupação*:"))
        self.submitButton_ocupacao.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.ocupacao_3), _translate("MainWindow", "Ocupação"))
        self.searchLabel_influenciaexternaid.setText(
            _translate("MainWindow", "Índice da Influência Externa*:"))
        self.submitButton_influenciaexterna.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.influenciaexterna_3), _translate("MainWindow", "Influência Externa"))
        self.searchLabel_idiomaid.setText(
            _translate("MainWindow", "Índice do Idioma*:"))
        self.submitButton_idioma.setText(
            _translate("MainWindow", "Submit"))
        self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(
            self.idioma_3), _translate("MainWindow", "Idioma"))


    def clickLocal_Noticia(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 9

        model = Controller.ControllerLocal_Noticia()

        self.Full_Local_Noticia = QtWidgets.QWidget()
        self.Full_Local_Noticia.setEnabled(True)
        self.Full_Local_Noticia.setObjectName(
            "Full_Local_Noticia")

        self.Full_Local_Noticia.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(1, Qt.Horizontal, "Manchete")
        model.setHeaderData(
            2, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            3, Qt.Horizontal, "Consequência")
        model.setHeaderData(
            4, Qt.Horizontal, "Popularidade")
        model.setHeaderData(
            5, Qt.Horizontal, "Data")
        model.setHeaderData(
            6, Qt.Horizontal, "Piada")
        model.setHeaderData(
            7, Qt.Horizontal, "Sigla do Local")
        model.setHeaderData(
            8, Qt.Horizontal, "Nome do Local")
        model.setHeaderData(
            9, Qt.Horizontal, "Complemento do Local")

        self.Full_Local_Noticia_view = QtWidgets.QTableView(
            self.Full_Local_Noticia)
        self.Full_Local_Noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.Full_Local_Noticia_view.setObjectName(
            "tab_Local_Noticia_view")
        self.Full_Local_Noticia_view.setModel(model)
        self.Full_Local_Noticia_view.resizeRowsToContents()
        self.Full_Local_Noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Full_Local_Noticia, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Full_Local_Noticia), _translate("MainWindow", "Local - Notícia"))


    def clickPalavrasChave_Noticia(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 8

        model = Controller.ControllerPalavrasChave_Noticia()

        self.Full_PalavrasChave_Noticia = QtWidgets.QWidget()
        self.Full_PalavrasChave_Noticia.setEnabled(True)
        self.Full_PalavrasChave_Noticia.setObjectName(
            "Full_PalavrasChave_Noticia")

        self.Full_PalavrasChave_Noticia.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(1, Qt.Horizontal, "Manchete")
        model.setHeaderData(
            2, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            3, Qt.Horizontal, "Consequência")
        model.setHeaderData(
            4, Qt.Horizontal, "Popularidade")
        model.setHeaderData(
            5, Qt.Horizontal, "Data")
        model.setHeaderData(
            6, Qt.Horizontal, "Piada")
        model.setHeaderData(
            7, Qt.Horizontal, "Palavra")
        model.setHeaderData(
            8, Qt.Horizontal, "Índice do Idioma")

        self.Full_PalavrasChave_Noticia_view = QtWidgets.QTableView(
            self.Full_PalavrasChave_Noticia)
        self.Full_PalavrasChave_Noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.Full_PalavrasChave_Noticia_view.setObjectName(
            "tab_PalavrasChave_Noticia_view")
        self.Full_PalavrasChave_Noticia_view.setModel(model)
        self.Full_PalavrasChave_Noticia_view.resizeRowsToContents()
        self.Full_PalavrasChave_Noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Full_PalavrasChave_Noticia, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Full_PalavrasChave_Noticia), _translate("MainWindow", "Palavra - Notícia"))


    def clickFonteConfiavel_Noticia(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 7

        model = Controller.ControllerFonteConfiavel_Noticia()

        self.Full_FonteConfiavel_Noticia = QtWidgets.QWidget()
        self.Full_FonteConfiavel_Noticia.setEnabled(True)
        self.Full_FonteConfiavel_Noticia.setObjectName(
            "Full_FonteConfiavel_Noticia")

        self.Full_FonteConfiavel_Noticia.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(1, Qt.Horizontal, "Manchete")
        model.setHeaderData(
            2, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            3, Qt.Horizontal, "Consequência")
        model.setHeaderData(
            4, Qt.Horizontal, "Popularidade")
        model.setHeaderData(
            5, Qt.Horizontal, "Data")
        model.setHeaderData(
            6, Qt.Horizontal, "Piada")
        model.setHeaderData(
            7, Qt.Horizontal, "Índice da Fonte")
        model.setHeaderData(
            8, Qt.Horizontal, "Nome da Fonte")
        model.setHeaderData(
            9, Qt.Horizontal, "Descrição da Fonte")

        self.Full_FonteConfiavel_Noticia_view = QtWidgets.QTableView(
            self.Full_FonteConfiavel_Noticia)
        self.Full_FonteConfiavel_Noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.Full_FonteConfiavel_Noticia_view.setObjectName(
            "tab_Full_FonteConfiavel_Noticia_view")
        self.Full_FonteConfiavel_Noticia_view.setModel(model)
        self.Full_FonteConfiavel_Noticia_view.resizeRowsToContents()
        self.Full_FonteConfiavel_Noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Full_FonteConfiavel_Noticia, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Full_FonteConfiavel_Noticia), _translate("MainWindow", "Fonte - Notícia"))


    def clickMidia_Noticia(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 6

        model = Controller.ControllerMidia_Noticia()

        self.Full_Midia_Noticia = QtWidgets.QWidget()
        self.Full_Midia_Noticia.setEnabled(True)
        self.Full_Midia_Noticia.setObjectName("Full_Midia_Noticia")

        self.Full_Midia_Noticia.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(1, Qt.Horizontal, "Manchete")
        model.setHeaderData(
            2, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            3, Qt.Horizontal, "Consequência")
        model.setHeaderData(
            4, Qt.Horizontal, "Popularidade")
        model.setHeaderData(
            5, Qt.Horizontal, "Data")
        model.setHeaderData(
            6, Qt.Horizontal, "Piada")
        model.setHeaderData(
            7, Qt.Horizontal, "Índice da Mídia")
        model.setHeaderData(
            8, Qt.Horizontal, "Nome da Mídia")
        model.setHeaderData(
            9, Qt.Horizontal, "Descrição da Mídia")
        model.setHeaderData(
            10, Qt.Horizontal, "Índice da Categoria da Mídia")

        self.Full_Midia_Noticia_view = QtWidgets.QTableView(
            self.Full_Midia_Noticia)
        self.Full_Midia_Noticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.Full_Midia_Noticia_view.setObjectName(
            "tab_Full_Midia_Noticia_view")
        self.Full_Midia_Noticia_view.setModel(model)
        self.Full_Midia_Noticia_view.resizeRowsToContents()
        self.Full_Midia_Noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Full_Midia_Noticia, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Full_Midia_Noticia), _translate("MainWindow", "Mídia - Notícia"))


    def clickInfluencia_Noticia(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 5

        model = Controller.ControllerInfluencia_Noticia()

        self.Full_Influencia_Noticia = QtWidgets.QWidget()
        self.Full_Influencia_Noticia.setEnabled(True)
        self.Full_Influencia_Noticia.setObjectName("Full_Influencia_Noticia")

        self.Full_Influencia_Noticia.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(1, Qt.Horizontal, "Manchete")
        model.setHeaderData(
            2, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            3, Qt.Horizontal, "Consequência")
        model.setHeaderData(
            4, Qt.Horizontal, "Popularidade")
        model.setHeaderData(
            5, Qt.Horizontal, "Data")
        model.setHeaderData(
            6, Qt.Horizontal, "Piada")
        model.setHeaderData(
            7, Qt.Horizontal, "Índice da Influência")
        model.setHeaderData(
            8, Qt.Horizontal, "Nome da Influência")

        self.Full_Influencia_Noticia_view = QtWidgets.QTableView(
            self.Full_Influencia_Noticia)
        self.Full_Influencia_Noticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.Full_Influencia_Noticia_view.setObjectName(
            "tab_Full_Influencia_Noticia_view")
        self.Full_Influencia_Noticia_view.setModel(model)
        self.Full_Influencia_Noticia_view.resizeRowsToContents()
        self.Full_Influencia_Noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Full_Influencia_Noticia, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Full_Influencia_Noticia), _translate("MainWindow", "Influência - Notícia"))


    def clickNoticia_CategoriaN(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 4

        model = Controller.ControllerNoticia_CategoriaN()

        self.Noticia_CategoriaN = QtWidgets.QWidget()
        self.Noticia_CategoriaN.setEnabled(True)
        self.Noticia_CategoriaN.setObjectName("Noticia_CategoriaN")

        self.Noticia_CategoriaN.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(1, Qt.Horizontal, "Manchete")
        model.setHeaderData(
            2, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            3, Qt.Horizontal, "Consequência")
        model.setHeaderData(
            4, Qt.Horizontal, "Popularidade")
        model.setHeaderData(
            5, Qt.Horizontal, "Data")
        model.setHeaderData(
            6, Qt.Horizontal, "Piada")
        model.setHeaderData(
            7, Qt.Horizontal, "Índice da Categoria")
        model.setHeaderData(
            8, Qt.Horizontal, "Nome da Categoria")
        model.setHeaderData(
            9, Qt.Horizontal, "Descrição da Categoria")

        self.Noticia_CategoriaN_view = QtWidgets.QTableView(
            self.Noticia_CategoriaN)
        self.Noticia_CategoriaN_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.Noticia_CategoriaN_view.setObjectName(
            "tab_Noticia_CategoriaN_view")
        self.Noticia_CategoriaN_view.setModel(model)
        self.Noticia_CategoriaN_view.resizeRowsToContents()
        self.Noticia_CategoriaN_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Noticia_CategoriaN, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Noticia_CategoriaN), _translate("MainWindow", "Notícia - Categoria"))


    def clickMidia_CategoriaM(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 3

        model = Controller.ControllerMidia_CategoriaM()

        self.Midia_CategoriaM = QtWidgets.QWidget()
        self.Midia_CategoriaM.setEnabled(True)
        self.Midia_CategoriaM.setObjectName("Midia_CategoriaM")

        self.Midia_CategoriaM.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Mídia")
        model.setHeaderData(1, Qt.Horizontal, "Nome")
        model.setHeaderData(
            2, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            3, Qt.Horizontal, "Índice da Categoria")
        model.setHeaderData(
            4, Qt.Horizontal, "Nome da Categoria")
        model.setHeaderData(
            5, Qt.Horizontal, "Descrição da Categoria")

        self.Midia_CategoriaM_view = QtWidgets.QTableView(
            self.Midia_CategoriaM)
        self.Midia_CategoriaM_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.Midia_CategoriaM_view.setObjectName("tab_Midia_CategoriaM_view")
        self.Midia_CategoriaM_view.setModel(model)
        self.Midia_CategoriaM_view.resizeRowsToContents()
        self.Midia_CategoriaM_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Midia_CategoriaM, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Midia_CategoriaM), _translate("MainWindow", "Mídia - Categoria"))


    def clickPessoa_Ocupacao(self):
        self.tabsSelection.clear()

        self.where = 1
        self.page = 2

        model = Controller.ControllerPessoa_Ocupacao()

        self.Pessoa_Ocupacao = QtWidgets.QWidget()
        self.Pessoa_Ocupacao.setEnabled(True)
        self.Pessoa_Ocupacao.setObjectName("Pessoa_Ocupacao")

        self.Pessoa_Ocupacao.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Pessoa")
        model.setHeaderData(1, Qt.Horizontal, "Nome")
        model.setHeaderData(
            2, Qt.Horizontal, "Idade")
        model.setHeaderData(
            3, Qt.Horizontal, "Índice da Ocupação")
        model.setHeaderData(
            4, Qt.Horizontal, "Emprego")
        model.setHeaderData(
            5, Qt.Horizontal, "Descrição Emprego")

        self.Pessoa_Ocupacao_view = QtWidgets.QTableView(self.Pessoa_Ocupacao)
        self.Pessoa_Ocupacao_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.Pessoa_Ocupacao_view.setObjectName("tab_Pessoa_Ocupacao_view")
        self.Pessoa_Ocupacao_view.setModel(model)
        self.Pessoa_Ocupacao_view.resizeRowsToContents()
        self.Pessoa_Ocupacao_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Pessoa_Ocupacao, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Pessoa_Ocupacao), _translate("MainWindow", "Pessoa - Ocupação"))

    
    def clickAutor_Vitima(self):

        self.tabsSelection.clear()

        self.where = 1
        self.page = 1

        model = Controller.ControllerAutor_Vitima()

        self.Autor_Vitima = QtWidgets.QWidget()
        self.Autor_Vitima.setEnabled(True)
        self.Autor_Vitima.setObjectName("Autor_Vitima")

        self.Autor_Vitima.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice do Autor")
        model.setHeaderData(1, Qt.Horizontal, "Nome")
        model.setHeaderData(
            2, Qt.Horizontal, "Idade")
        model.setHeaderData(
            3, Qt.Horizontal, "Índice da Ocupação")
        model.setHeaderData(
            4, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(
            5, Qt.Horizontal, "Índice da Vítima")

        self.Autor_Vitima_view = QtWidgets.QTableView(self.Autor_Vitima)
        self.Autor_Vitima_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.Autor_Vitima_view.setObjectName("tab_Autor_Vitima_view")
        self.Autor_Vitima_view.setModel(model)
        self.Autor_Vitima_view.resizeRowsToContents()
        self.Autor_Vitima_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Autor_Vitima, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Autor_Vitima), _translate("MainWindow", "Autor - Vítima"))

    
    def clickFull_Noticia(self):

        self.tabsSelection.clear()

        self.where = 1
        self.page = 0

        model = Controller.ControllerFull_Noticia()

        self.Full_Noticia = QtWidgets.QWidget()
        self.Full_Noticia.setEnabled(True)
        self.Full_Noticia.setObjectName("Full_Noticia")

        self.Full_Noticia.model = model

        model.setHeaderData(0, Qt.Horizontal, "Índice da Categoria da Notícia")
        model.setHeaderData(1, Qt.Horizontal, "Índice da Notícia")
        model.setHeaderData(
            2, Qt.Horizontal, "Manchete")
        model.setHeaderData(
            3, Qt.Horizontal, "Descrição")
        model.setHeaderData(
            4, Qt.Horizontal, "Consequência")
        model.setHeaderData(
            5, Qt.Horizontal, "Popularidade")
        model.setHeaderData(
            6, Qt.Horizontal, "Data")
        model.setHeaderData(
            7, Qt.Horizontal, "Piada")
        model.setHeaderData(
            8, Qt.Horizontal, "Índice do Autor")
        model.setHeaderData(
            9, Qt.Horizontal, "Índice da Vítima")
        model.setHeaderData(
            10, Qt.Horizontal, "Índice do Local")
        model.setHeaderData(
            11, Qt.Horizontal, "Índice da Palavra Chave")
        model.setHeaderData(
            12, Qt.Horizontal, "Índice da Fonte Confiável")
        model.setHeaderData(
            13, Qt.Horizontal, "Índice da Mídia")
        model.setHeaderData(
            14, Qt.Horizontal, "Índice da Influência Externa")

        self.Full_Noticia_view = QtWidgets.QTableView(self.Full_Noticia)
        self.Full_Noticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.Full_Noticia_view.setObjectName("tab_Full_Noticia_view")
        self.Full_Noticia_view.setModel(model)
        self.Full_Noticia_view.resizeRowsToContents()
        self.Full_Noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.Full_Noticia, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.Full_Noticia), _translate("MainWindow", "Notícia Completa"))
    

    def clicknormal(self):

        self.tabsSelection.clear()

        self.where = 0
        self.page = 0

        self.categorianoticia = QtWidgets.QWidget()
        self.categorianoticia.setEnabled(True)
        self.categorianoticia.setObjectName("categorianoticia")

        self.categorianoticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.categorianoticia.model.setTable("categorianoticia")
        self.categorianoticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.categorianoticia.model.select()
        self.categorianoticia.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.categorianoticia.model.setHeaderData(
            1, Qt.Horizontal, "Nome")
        self.categorianoticia.model.setHeaderData(
            2, Qt.Horizontal, "Descrição")

        self.categorianoticia_view = QtWidgets.QTableView(
            self.categorianoticia)
        self.categorianoticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.categorianoticia_view.setObjectName("tab_categorianoticia_view")
        self.categorianoticia_view.setModel(self.categorianoticia.model)
        self.categorianoticia_view.resizeRowsToContents()
        self.categorianoticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.categorianoticia, "")

        self.noticia = QtWidgets.QWidget()
        self.noticia.setObjectName("noticia")

        self.noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.noticia.model.setTable("noticia")
        self.noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.noticia.model.select()
        self.noticia.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.noticia.model.setHeaderData(1, Qt.Horizontal, "Manchete")
        self.noticia.model.setHeaderData(2, Qt.Horizontal, "Descrição")
        self.noticia.model.setHeaderData(3, Qt.Horizontal, "Consequência")
        self.noticia.model.setHeaderData(4, Qt.Horizontal, "Popularidade")
        self.noticia.model.setHeaderData(5, Qt.Horizontal, "Data")
        self.noticia.model.setHeaderData(6, Qt.Horizontal, "Piada")
        self.noticia.model.setHeaderData(7, Qt.Horizontal, "InfluenciaId")

        self.noticia_view = QtWidgets.QTableView(self.noticia)
        self.noticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.noticia_view.setObjectName("tab_noticia_view")
        self.noticia_view.setModel(self.noticia.model)
        self.noticia_view.resizeRowsToContents()
        self.noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.noticia, "")

        self.categoriamidia = QtWidgets.QWidget()
        self.categoriamidia.setObjectName("categoriamidia")

        self.categoriamidia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.categoriamidia.model.setTable("categoriamidia")
        self.categoriamidia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.categoriamidia.model.select()
        self.categoriamidia.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.categoriamidia.model.setHeaderData(
            1, Qt.Horizontal, "Nome")
        self.categoriamidia.model.setHeaderData(
            2, Qt.Horizontal, "Descrição")

        self.categoriamidia_view = QtWidgets.QTableView(self.categoriamidia)
        self.categoriamidia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.categoriamidia_view.setObjectName("tab_categoriamidia_view")
        self.categoriamidia_view.setModel(self.categoriamidia.model)
        self.categoriamidia_view.resizeRowsToContents()
        self.categoriamidia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.categoriamidia, "")

        self.midia = QtWidgets.QWidget()
        self.midia.setObjectName("midia")

        self.midia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.midia.model.setTable("midia")
        self.midia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.midia.model.select()
        self.midia.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.midia.model.setHeaderData(1, Qt.Horizontal, "Nome")
        self.midia.model.setHeaderData(2, Qt.Horizontal, "Descrição")
        self.midia.model.setHeaderData(3, Qt.Horizontal, "Índice da Categoria")

        self.midia_view = QtWidgets.QTableView(self.midia)
        self.midia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.midia_view.setObjectName("tab_midia_view")
        self.midia_view.setModel(self.midia.model)
        self.midia_view.resizeRowsToContents()
        self.midia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.midia, "")

        self.pessoa = QtWidgets.QWidget()
        self.pessoa.setObjectName("pessoa")

        self.pessoa.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.pessoa.model.setTable("pessoa")
        self.pessoa.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.pessoa.model.select()
        self.pessoa.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.pessoa.model.setHeaderData(1, Qt.Horizontal, "Nome")
        self.pessoa.model.setHeaderData(2, Qt.Horizontal, "Idade")
        self.pessoa.model.setHeaderData(3, Qt.Horizontal, "Índice de Ocupação")

        self.pessoa_view = QtWidgets.QTableView(self.pessoa)
        self.pessoa_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.pessoa_view.setObjectName("tab_pessoa_view")
        self.pessoa_view.setModel(self.pessoa.model)
        self.pessoa_view.resizeRowsToContents()
        self.pessoa_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.pessoa, "")

        self.palavraschave = QtWidgets.QWidget()
        self.palavraschave.setObjectName("palavraschave")

        self.palavraschave.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.palavraschave.model.setTable("palavraschave")
        self.palavraschave.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.palavraschave.model.select()
        self.palavraschave.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.palavraschave.model.setHeaderData(
            1, Qt.Horizontal, "Índice do Idioma")

        self.palavraschave_view = QtWidgets.QTableView(self.palavraschave)
        self.palavraschave_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.palavraschave_view.setObjectName("palavraschave_view")
        self.palavraschave_view.setModel(self.palavraschave.model)
        self.palavraschave_view.resizeRowsToContents()
        self.palavraschave_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.palavraschave, "")

        self.fonteconfiavel = QtWidgets.QWidget()
        self.fonteconfiavel.setObjectName("fonteconfiavel")

        self.fonteconfiavel.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.fonteconfiavel.model.setTable("fonteconfiavel")
        self.fonteconfiavel.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.fonteconfiavel.model.select()
        self.fonteconfiavel.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.fonteconfiavel.model.setHeaderData(1, Qt.Horizontal, "Nome")
        self.fonteconfiavel.model.setHeaderData(2, Qt.Horizontal, "Descrição")

        self.fonteconfiavel_view = QtWidgets.QTableView(self.fonteconfiavel)
        self.fonteconfiavel_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.fonteconfiavel_view.setObjectName("tab_fonteconfiavel_view")
        self.fonteconfiavel_view.setModel(self.fonteconfiavel.model)
        self.fonteconfiavel_view.resizeRowsToContents()
        self.fonteconfiavel_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.fonteconfiavel, "")

        self.local = QtWidgets.QWidget()
        self.local.setObjectName("local")

        self.local.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.local.model.setTable("local")
        self.local.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.local.model.select()
        self.local.model.setHeaderData(0, Qt.Horizontal, "Sigla")
        self.local.model.setHeaderData(1, Qt.Horizontal, "Nome")
        self.local.model.setHeaderData(2, Qt.Horizontal, "Complemento")

        self.local_view = QtWidgets.QTableView(self.local)
        self.local_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.local_view.setObjectName("tab_local_view")
        self.local_view.setModel(self.local.model)
        self.local_view.resizeRowsToContents()
        self.local_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.local, "")

        self.ocupacao = QtWidgets.QWidget()
        self.ocupacao.setObjectName("ocupacao")

        self.ocupacao.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.ocupacao.model.setTable("ocupacao")
        self.ocupacao.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.ocupacao.model.select()
        self.ocupacao.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.ocupacao.model.setHeaderData(1, Qt.Horizontal, "Emprego")
        self.ocupacao.model.setHeaderData(2, Qt.Horizontal, "Descrição")

        self.ocupacao_view = QtWidgets.QTableView(self.ocupacao)
        self.ocupacao_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.ocupacao_view.setObjectName("tab_ocupacao_view")
        self.ocupacao_view.setModel(self.ocupacao.model)
        self.ocupacao_view.resizeRowsToContents()
        self.ocupacao_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.ocupacao, "")

        self.influenciaexterna = QtWidgets.QWidget()
        self.influenciaexterna.setObjectName("influenciaexterna")

        self.influenciaexterna.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.influenciaexterna.model.setTable("influenciaexterna")
        self.influenciaexterna.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.influenciaexterna.model.select()
        self.influenciaexterna.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.influenciaexterna.model.setHeaderData(1, Qt.Horizontal, "Nome")

        self.influenciaexterna_view = QtWidgets.QTableView(
            self.influenciaexterna)
        self.influenciaexterna_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.influenciaexterna_view.setObjectName("tab_influenciaexterna_view")
        self.influenciaexterna_view.setModel(self.influenciaexterna.model)
        self.influenciaexterna_view.resizeRowsToContents()
        self.influenciaexterna_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.influenciaexterna, "")

        self.idioma = QtWidgets.QWidget()
        self.idioma.setObjectName("idioma")

        self.idioma.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.idioma.model.setTable("idioma")
        self.idioma.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.idioma.model.select()
        self.idioma.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.idioma.model.setHeaderData(1, Qt.Horizontal, "Nome")

        self.idioma_view = QtWidgets.QTableView(self.idioma)
        self.idioma_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.idioma_view.setObjectName("tab_idioma_view")
        self.idioma_view.setModel(self.idioma.model)
        self.idioma_view.resizeRowsToContents()
        self.idioma_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.idioma, "")


        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.categorianoticia), _translate("MainWindow", "Categoria Notícia"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.noticia), _translate("MainWindow", "Notícia"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.categoriamidia), _translate("MainWindow", "Categoria Mídia"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.midia), _translate("MainWindow", "Mídia"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.pessoa), _translate("MainWindow", "Pessoa"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.palavraschave), _translate("MainWindow", "Palavras Chave"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.fonteconfiavel), _translate("MainWindow", "Fonte Confiável"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.local), _translate("MainWindow", "Local"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.ocupacao), _translate("MainWindow", "Ocupação"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.influenciaexterna), _translate("MainWindow", "Influência Externa"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.idioma), _translate("MainWindow", "Idioma"))


    def clickrelational(self):

        self.tabsSelection.clear()

        self.where = 2
        self.page = 0

        self.autor_noticia = QtWidgets.QWidget()
        self.autor_noticia.setEnabled(True)
        self.autor_noticia.setObjectName("autor_noticia")

        self.autor_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.autor_noticia.model.setTable(
            "autor_noticia")
        self.autor_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.autor_noticia.model.select()
        self.autor_noticia.model.setHeaderData(
            0, Qt.Horizontal, "Índice da Notícia")
        self.autor_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice do Autor")

        self.autor_noticia_view = QtWidgets.QTableView(
            self.autor_noticia)
        self.autor_noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.autor_noticia_view.setObjectName(
            "tab_autor_noticia_view")
        self.autor_noticia_view.setModel(
            self.autor_noticia.model)
        self.autor_noticia_view.resizeRowsToContents()
        self.autor_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.autor_noticia, "")

        self.vitima_noticia = QtWidgets.QWidget()
        self.vitima_noticia.setEnabled(True)
        self.vitima_noticia.setObjectName("vitima_noticia")

        self.vitima_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.vitima_noticia.model.setTable(
            "vitima_noticia")
        self.vitima_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.vitima_noticia.model.select()
        self.vitima_noticia.model.setHeaderData(
            0, Qt.Horizontal, "Índice da Notícia")
        self.vitima_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice da Vítima")

        self.vitima_noticia_view = QtWidgets.QTableView(
            self.vitima_noticia)
        self.vitima_noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.vitima_noticia_view.setObjectName(
            "tab_autor_noticia_view")
        self.vitima_noticia_view.setModel(
            self.vitima_noticia.model)
        self.vitima_noticia_view.resizeRowsToContents()
        self.vitima_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.vitima_noticia, "")

        self.influencia_noticia = QtWidgets.QWidget()
        self.influencia_noticia.setEnabled(True)
        self.influencia_noticia.setObjectName("influencia_noticia")

        self.influencia_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.influencia_noticia.model.setTable("influencia_noticia")
        self.influencia_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.influencia_noticia.model.select()
        self.influencia_noticia.model.setHeaderData(0, Qt.Horizontal, "Índice da Notícia")
        self.influencia_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice da Influência Externa")

        self.influencia_noticia_view = QtWidgets.QTableView(
            self.influencia_noticia)
        self.influencia_noticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.influencia_noticia_view.setObjectName("tab_influencia_noticia_view")
        self.influencia_noticia_view.setModel(self.influencia_noticia.model)
        self.influencia_noticia_view.resizeRowsToContents()
        self.influencia_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.influencia_noticia, "")

        self.midia_noticia = QtWidgets.QWidget()
        self.midia_noticia.setEnabled(True)
        self.midia_noticia.setObjectName("midia_noticia")

        self.midia_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.midia_noticia.model.setTable("midia_noticia")
        self.midia_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.midia_noticia.model.select()
        self.midia_noticia.model.setHeaderData(
            0, Qt.Horizontal, "Índice da Notícia")
        self.midia_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice da Mídia")

        self.midia_noticia_view = QtWidgets.QTableView(
            self.midia_noticia)
        self.midia_noticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.midia_noticia_view.setObjectName(
            "tab_midia_noticia_view")
        self.midia_noticia_view.setModel(self.influencia_noticia.model)
        self.midia_noticia_view.resizeRowsToContents()
        self.midia_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.midia_noticia, "")

        self.fonteconfiavel_noticia = QtWidgets.QWidget()
        self.fonteconfiavel_noticia.setEnabled(True)
        self.fonteconfiavel_noticia.setObjectName("fonteconfiavel_noticia")

        self.fonteconfiavel_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.fonteconfiavel_noticia.model.setTable("fonteconfiavel_noticia")
        self.fonteconfiavel_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.fonteconfiavel_noticia.model.select()
        self.fonteconfiavel_noticia.model.setHeaderData(
            0, Qt.Horizontal, "Índice da Notícia")
        self.fonteconfiavel_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice da Fonte Confiável")

        self.fonteconfiavel_noticia_view = QtWidgets.QTableView(
            self.fonteconfiavel_noticia)
        self.fonteconfiavel_noticia_view.setGeometry(QtCore.QRect(0, 0, 1246, 513))
        self.fonteconfiavel_noticia_view.setObjectName(
            "tab_fonteconfiavel_noticia_view")
        self.fonteconfiavel_noticia_view.setModel(
            self.fonteconfiavel_noticia.model)
        self.fonteconfiavel_noticia_view.resizeRowsToContents()
        self.fonteconfiavel_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.fonteconfiavel_noticia, "")

        self.palavraschave_noticia = QtWidgets.QWidget()
        self.palavraschave_noticia.setEnabled(True)
        self.palavraschave_noticia.setObjectName("palavraschave_noticia")

        self.palavraschave_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.palavraschave_noticia.model.setTable("palavraschave_noticia")
        self.palavraschave_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.palavraschave_noticia.model.select()
        self.palavraschave_noticia.model.setHeaderData(
            0, Qt.Horizontal, "Índice da Notícia")
        self.palavraschave_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice da Palavra Chave")

        self.palavraschave_noticia_view = QtWidgets.QTableView(
            self.palavraschave_noticia)
        self.palavraschave_noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.palavraschave_noticia_view.setObjectName(
            "tab_palavraschave_noticia_view")
        self.palavraschave_noticia_view.setModel(
            self.palavraschave_noticia.model)
        self.palavraschave_noticia_view.resizeRowsToContents()
        self.palavraschave_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.palavraschave_noticia, "")

        self.local_noticia = QtWidgets.QWidget()
        self.local_noticia.setEnabled(True)
        self.local_noticia.setObjectName("local_noticia")

        self.local_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.local_noticia.model.setTable("local_noticia")
        self.local_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.local_noticia.model.select()
        self.local_noticia.model.setHeaderData(
            0, Qt.Horizontal, "Índice da Notícia")
        self.local_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice da Local")

        self.local_noticia_view = QtWidgets.QTableView(
            self.local_noticia)
        self.local_noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.local_noticia_view.setObjectName(
            "tab_local_noticia_view")
        self.local_noticia_view.setModel(
            self.local_noticia.model)
        self.local_noticia_view.resizeRowsToContents()
        self.local_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.local_noticia, "")

        self.categorianoticia_noticia = QtWidgets.QWidget()
        self.categorianoticia_noticia.setEnabled(True)
        self.categorianoticia_noticia.setObjectName("categorianoticia_noticia")

        self.categorianoticia_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.categorianoticia_noticia.model.setTable(
            "categorianoticia_noticia")
        self.categorianoticia_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.categorianoticia_noticia.model.select()
        self.categorianoticia_noticia.model.setHeaderData(
            0, Qt.Horizontal, "Índice da Notícia")
        self.categorianoticia_noticia.model.setHeaderData(
            1, Qt.Horizontal, "Índice da Categoria da Notícia")

        self.categorianoticia_noticia_view = QtWidgets.QTableView(
            self.categorianoticia_noticia)
        self.categorianoticia_noticia_view.setGeometry(
            QtCore.QRect(0, 0, 1246, 513))
        self.categorianoticia_noticia_view.setObjectName(
            "tab_categorianoticia_noticia_view")
        self.categorianoticia_noticia_view.setModel(
            self.categorianoticia_noticia.model)
        self.categorianoticia_noticia_view.resizeRowsToContents()
        self.categorianoticia_noticia_view.resizeColumnsToContents()

        self.tabsSelection.addTab(self.categorianoticia_noticia, "")

        _translate = QtCore.QCoreApplication.translate
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.autor_noticia), _translate("MainWindow", "Notícia/Autor"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.vitima_noticia), _translate("MainWindow", "Notícia/Vítima"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.influencia_noticia), _translate("MainWindow", "Notícia/Influência Externa"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.midia_noticia), _translate("MainWindow", "Notícia/Mídia"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.fonteconfiavel_noticia), _translate("MainWindow", "Notícia/Fonte Confiável"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.palavraschave_noticia), _translate("MainWindow", "Notícia/Palavra Chave"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.local_noticia), _translate("MainWindow", "Notícia/Local"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(
            self.categorianoticia_noticia), _translate("MainWindow", "Notícia/Categoria da Notícia"))
    

    def clicksearch(self):
        searchText = self.searchField.text()
        self.statusbar.showMessage("Carregando...")

        model = Controller.ControllerSearchButton(
            table_columns_tabs[self.where, self.page, self.tabsSelection.currentIndex()], searchText)
        columns = table_columns_view[self.where, self.page, self.tabsSelection.currentIndex()]

        for i in range(0, len(columns)):
            model.setHeaderData(i, Qt.Horizontal, columns[i])

        whichtable = table_columns_tabs[self.where, self.page, self.tabsSelection.currentIndex()]

        if whichtable is "categorianoticia":
            self.categorianoticia_view.setModel(model)
            self.categorianoticia_view.resizeRowsToContents()
            self.categorianoticia_view.resizeColumnsToContents()
        elif whichtable is "noticia":
            self.noticia_view.setModel(model)
            self.noticia_view.resizeRowsToContents()
            self.noticia_view.resizeColumnsToContents()
        elif whichtable is "categoriamidia":
            self.categoriamidia_view.setModel(model)
            self.categoriamidia_view.resizeRowsToContents()
            self.categoriamidia_view.resizeColumnsToContents()
        elif whichtable is "midia":
            self.midia_view.setModel(model)
            self.midia_view.resizeRowsToContents()
            self.midia_view.resizeColumnsToContents()
        elif whichtable is "pessoa":
            self.pessoa_view.setModel(model)
            self.pessoa_view.resizeRowsToContents()
            self.pessoa_view.resizeColumnsToContents()
        elif whichtable is "palavraschave":
            self.palavraschave_view.setModel(model)
            self.palavraschave_view.resizeRowsToContents()
            self.palavraschave_view.resizeColumnsToContents()
        elif whichtable is "local":
            self.local_view.setModel(model)
            self.local_view.resizeRowsToContents()
            self.local_view.resizeColumnsToContents()
        elif whichtable is "fonteconfiavel":
            self.fonteconfiavel_view.setModel(model)
            self.fonteconfiavel_view.resizeRowsToContents()
            self.fonteconfiavel_view.resizeColumnsToContents()
        elif whichtable is "ocupacao":
            self.ocupacao_view.setModel(model)
            self.ocupacao_view.resizeRowsToContents()
            self.ocupacao_view.resizeColumnsToContents()
        elif whichtable is "influenciaexterna":
            self.influenciaexterna_view.setModel(model)
            self.influenciaexterna_view.resizeRowsToContents()
            self.influenciaexterna_view.resizeColumnsToContents()
        elif whichtable is "idioma":
            self.idioma_view.setModel(model)
            self.idioma_view.resizeRowsToContents()
            self.idioma_view.resizeColumnsToContents()

        elif whichtable is "full_Noticia":
            self.Full_Noticia_view.setModel(model)
            self.Full_Noticia_view.resizeRowsToContents()
            self.Full_Noticia_view.resizeColumnsToContents()
        elif whichtable is "autor_Vitima":
            self.Autor_Vitima_view.setModel(model)
            self.Autor_Vitima_view.resizeRowsToContents()
            self.Autor_Vitima_view.resizeColumnsToContents()
        elif whichtable is "pessoa_Ocupacao":
            self.Pessoa_Ocupacao_view.setModel(model)
            self.Pessoa_Ocupacao_view.resizeRowsToContents()
            self.Pessoa_Ocupacao_view.resizeColumnsToContents()
        elif whichtable is "midia_CategoriaM":
            self.Midia_CategoriaM_view.setModel(model)
            self.Midia_CategoriaM_view.resizeRowsToContents()
            self.Midia_CategoriaM_view.resizeColumnsToContents()
        elif whichtable is "noticia_CategoriaN":
            self.Noticia_CategoriaN_view.setModel(model)
            self.Noticia_CategoriaN_view.resizeRowsToContents()
            self.Noticia_CategoriaN_view.resizeColumnsToContents()
        elif whichtable is "full_Influencia_Noticia":
            self.Full_Influencia_Noticia_view.setModel(model)
            self.Full_Influencia_Noticia_view.resizeRowsToContents()
            self.Full_Influencia_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_Midia_Noticia":
            self.Full_Midia_Noticia_view.setModel(model)
            self.Full_Midia_Noticia_view.resizeRowsToContents()
            self.Full_Midia_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_FonteConfiavel_Noticia":
            self.Full_FonteConfiavel_Noticia_view.setModel(model)
            self.Full_FonteConfiavel_Noticia_view.resizeRowsToContents()
            self.Full_FonteConfiavel_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_PalavrasChave_Noticia":
            self.Full_PalavrasChave_Noticia_view.setModel(model)
            self.Full_PalavrasChave_Noticia_view.resizeRowsToContents()
            self.Full_PalavrasChave_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_Local_Noticia":
            self.Full_Local_Noticia_view.setModel(model)
            self.Full_Local_Noticia_view.resizeRowsToContents()
            self.Full_Local_Noticia_view.resizeColumnsToContents()
        
        elif whichtable is "autor_noticia":
            self.autor_noticia_view.setModel(model)
            self.autor_noticia_view.resizeRowsToContents()
            self.autor_noticia_view.resizeColumnsToContents()
        elif whichtable is "vitima_noticia":
            self.vitima_noticia_view.setModel(model)
            self.vitima_noticia_view.resizeRowsToContents()
            self.vitima_noticia_view.resizeColumnsToContents()
        elif whichtable is "influencia_noticia":
            self.influencia_noticia_view.setModel(model)
            self.influencia_noticia_view.resizeRowsToContents()
            self.influencia_noticia_view.resizeColumnsToContents()
        elif whichtable is "midia_noticia":
            self.midia_noticia_view.setModel(model)
            self.midia_noticia_view.resizeRowsToContents()
            self.midia_noticia_view.resizeColumnsToContents()
        elif whichtable is "fonteconfiavel_noticia":
            self.fonteconfiavel_noticia_view.setModel(model)
            self.fonteconfiavel_noticia_view.resizeRowsToContents()
            self.fonteconfiavel_noticia_view.resizeColumnsToContents()
        elif whichtable is "palavraschave_noticia":
            self.palavraschave_noticia_view.setModel(model)
            self.palavraschave_noticia_view.resizeRowsToContents()
            self.palavraschave_noticia_view.resizeColumnsToContents()
        elif whichtable is "local_noticia":
            self.local_noticia_view.setModel(model)
            self.local_noticia_view.resizeRowsToContents()
            self.local_noticia_view.resizeColumnsToContents()
        elif whichtable is "categorianoticia_noticia":
            self.categorianoticia_noticia_view.setModel(model)
            self.categorianoticia_noticia_view.resizeRowsToContents()
            self.categorianoticia_noticia_view.resizeColumnsToContents()

        self.statusbar.showMessage("Ready")


    def clickrefresh(self):
        self.statusbar.showMessage("Carregando...")
        whichtable = table_columns_tabs[self.where, self.page, self.tabsSelection.currentIndex()]

        if whichtable is "categorianoticia":
            self.categorianoticia_view.setModel(self.categorianoticia.model)
            self.categorianoticia_view.resizeRowsToContents()
            self.categorianoticia_view.resizeColumnsToContents()
        elif whichtable is "noticia":
            self.noticia_view.setModel(self.noticia.model)
            self.noticia_view.resizeRowsToContents()
            self.noticia_view.resizeColumnsToContents()
        elif whichtable is "categoriamidia":
            self.categoriamidia_view.setModel(self.categoriamidia.model)
            self.categoriamidia_view.resizeRowsToContents()
            self.categoriamidia_view.resizeColumnsToContents()
        elif whichtable is "midia":
            self.midia_view.setModel(self.midia.model)
            self.midia_view.resizeRowsToContents()
            self.midia_view.resizeColumnsToContents()
        elif whichtable is "pessoa":
            self.pessoa_view.setModel(self.pessoa.model)
            self.pessoa_view.resizeRowsToContents()
            self.pessoa_view.resizeColumnsToContents()
        elif whichtable is "palavraschave":
            self.palavraschave_view.setModel(self.palavraschave.model)
            self.palavraschave_view.resizeRowsToContents()
            self.palavraschave_view.resizeColumnsToContents()
        elif whichtable is "local":
            self.local_view.setModel(self.local.model)
            self.local_view.resizeRowsToContents()
            self.local_view.resizeColumnsToContents()
        elif whichtable is "fonteconfiavel":
            self.fonteconfiavel_view.setModel(self.fonteconfiavel.model)
            self.fonteconfiavel_view.resizeRowsToContents()
            self.fonteconfiavel_view.resizeColumnsToContents()
        elif whichtable is "ocupacao":
            self.ocupacao_view.setModel(self.ocupacao.model)
            self.ocupacao_view.resizeRowsToContents()
            self.ocupacao_view.resizeColumnsToContents()
        elif whichtable is "influenciaexterna":
            self.influenciaexterna_view.setModel(self.influenciaexterna.model)
            self.influenciaexterna_view.resizeRowsToContents()
            self.influenciaexterna_view.resizeColumnsToContents()
        elif whichtable is "idioma":
            self.idioma_view.setModel(self.idioma.model)
            self.idioma_view.resizeRowsToContents()
            self.idioma_view.resizeColumnsToContents()

        elif whichtable is "full_Noticia":
            self.Full_Noticia_view.setModel(self.Full_Noticia.model)
            self.Full_Noticia_view.resizeRowsToContents()
            self.Full_Noticia_view.resizeColumnsToContents()
        elif whichtable is "autor_Vitima":
            self.Autor_Vitima_view.setModel(self.Autor_Vitima.model)
            self.Autor_Vitima_view.resizeRowsToContents()
            self.Autor_Vitima_view.resizeColumnsToContents()
        elif whichtable is "pessoa_Ocupacao":
            self.Pessoa_Ocupacao_view.setModel(self.Pessoa_Ocupacao.model)
            self.Pessoa_Ocupacao_view.resizeRowsToContents()
            self.Pessoa_Ocupacao_view.resizeColumnsToContents()
        elif whichtable is "midia_CategoriaM":
            self.Midia_CategoriaM_view.setModel(self.Midia_CategoriaM.model)
            self.Midia_CategoriaM_view.resizeRowsToContents()
            self.Midia_CategoriaM_view.resizeColumnsToContents()
        elif whichtable is "noticia_CategoriaN":
            self.Noticia_CategoriaN_view.setModel(self.Noticia_CategoriaN.model)
            self.Noticia_CategoriaN_view.resizeRowsToContents()
            self.Noticia_CategoriaN_view.resizeColumnsToContents()
        elif whichtable is "full_Influencia_Noticia":
            self.Full_Influencia_Noticia_view.setModel(self.Full_Influencia_Noticia.model)
            self.Full_Influencia_Noticia_view.resizeRowsToContents()
            self.Full_Influencia_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_Midia_Noticia":
            self.Full_Midia_Noticia_view.setModel(self.Full_Midia_Noticia.model)
            self.Full_Midia_Noticia_view.resizeRowsToContents()
            self.Full_Midia_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_FonteConfiavel_Noticia":
            self.Full_FonteConfiavel_Noticia_view.setModel(self.Full_FonteConfiavel_Noticia.model)
            self.Full_FonteConfiavel_Noticia_view.resizeRowsToContents()
            self.Full_FonteConfiavel_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_PalavrasChave_Noticia":
            self.Full_PalavrasChave_Noticia_view.setModel(self.Full_PalavrasChave_Noticia.model)
            self.Full_PalavrasChave_Noticia_view.resizeRowsToContents()
            self.Full_PalavrasChave_Noticia_view.resizeColumnsToContents()
        elif whichtable is "full_Local_Noticia":
            self.Full_Local_Noticia_view.setModel(self.Full_Local_Noticia.model)
            self.Full_Local_Noticia_view.resizeRowsToContents()
            self.Full_Local_Noticia_view.resizeColumnsToContents()
        
        elif whichtable is "autor_noticia":
            self.autor_noticia_view.setModel(self.autor_noticia.model)
            self.autor_noticia_view.resizeRowsToContents()
            self.autor_noticia_view.resizeColumnsToContents()
        elif whichtable is "vitima_noticia":
            self.vitima_noticia_view.setModel(self.vitima_noticia.model)
            self.vitima_noticia_view.resizeRowsToContents()
            self.vitima_noticia_view.resizeColumnsToContents()
        elif whichtable is "influencia_noticia":
            self.influencia_noticia_view.setModel(self.influencia_noticia.model)
            self.influencia_noticia_view.resizeRowsToContents()
            self.influencia_noticia_view.resizeColumnsToContents()
        elif whichtable is "midia_noticia":
            self.midia_noticia_view.setModel(self.midia_noticia.model)
            self.midia_noticia_view.resizeRowsToContents()
            self.midia_noticia_view.resizeColumnsToContents()
        elif whichtable is "fonteconfiavel_noticia":
            self.fonteconfiavel_noticia_view.setModel(self.fonteconfiavel_noticia.model)
            self.fonteconfiavel_noticia_view.resizeRowsToContents()
            self.fonteconfiavel_noticia_view.resizeColumnsToContents()
        elif whichtable is "palavraschave_noticia":
            self.palavraschave_noticia_view.setModel(self.palavraschave_noticia.model)
            self.palavraschave_noticia_view.resizeRowsToContents()
            self.palavraschave_noticia_view.resizeColumnsToContents()
        elif whichtable is "local_noticia":
            self.local_noticia_view.setModel(self.local_noticia.model)
            self.local_noticia_view.resizeRowsToContents()
            self.local_noticia_view.resizeColumnsToContents()
        elif whichtable is "categorianoticia_noticia":
            self.categorianoticia_noticia_view.setModel(self.categorianoticia_noticia.model)
            self.categorianoticia_noticia_view.resizeRowsToContents()
            self.categorianoticia_noticia_view.resizeColumnsToContents()

        self.statusbar.showMessage("Ready")


    def clicksubmitinsert(self):
        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)

        self.statusbar.showMessage("Carregando...")
        whichtable = table_columns_tabs[self.where,self.page, self.tabsInsertion.currentIndex()]
        if whichtable is "categorianoticia":
            Id = Controller.ControllerCountTable(whichtable, conn)
            nome = self.searchField_nomecategorian.text()
            descricao = self.searchField_descricaocategorian.text()
            if(nome == "" or descricao == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, nome, descricao)
                self.statusbar.showMessage("Ready")
        elif whichtable is "noticia":
            Id = Controller.ControllerCountTable(whichtable, conn)
            manchete = self.searchField_manchete.text()
            descricao = self.searchField_descricaonoticia.text()
            consequencia = self.searchField_consequencia.text()
            data = str(self.spinBox_ano.value()) + "-" + str(self.spinBox_mes.value()) + "-" + str(self.spinBox_dias.value())
            popularidade = str(self.spinBox_popularidade.value())
            piada = self.checkBox.isChecked()
            if(manchete == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, manchete, descricao, consequencia, popularidade, data, piada)
                self.statusbar.showMessage("Ready")
        elif whichtable is "categoriamidia":
            Id = Controller.ControllerCountTable(whichtable, conn)
            nome = self.searchField_nomecategoriam.text()
            descricao = self.searchField_descricaocategoriam.text()
            if(nome == "" or descricao == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, nome, descricao)
                self.statusbar.showMessage("Ready")
        elif whichtable is "midia":
            Id = Controller.ControllerCountTable(whichtable, conn)
            nome = self.searchField_nomemidia.text()
            descricao = self.searchField_descricaomidia.text()
            categoriaid = str(self.spinBox_categoriamidia.value())
            if(nome == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, nome, descricao, categoriaid)
                self.statusbar.showMessage("Ready")
        elif whichtable is "pessoa":
            Id = Controller.ControllerCountTable(whichtable, conn)
            nome = self.searchField_nomepessoa.text()
            idade = str(self.spinBox_idade.value())
            ocupacaoid = str(self.spinBox_ocupacao.value())
            if(nome == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, nome, idade, ocupacaoid)
                self.statusbar.showMessage("Ready")
        elif whichtable is "palavraschave":
            nome = self.searchField_nomepalavra.text()
            idioma = str(self.spinBox_idioma.value())
            if(nome == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, nome, idioma)
                self.statusbar.showMessage("Ready")
        elif whichtable is "local":
            sigla = self.searchField_sigla.text()
            nome = self.searchField_nomelocal.text()
            complemento = self.searchField_complemento.text()
            if(nome == "" or sigla == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, sigla, nome, complemento)
                self.statusbar.showMessage("Ready")
        elif whichtable is "fonteconfiavel":
            Id = Controller.ControllerCountTable(whichtable, conn)
            nome = self.searchField_nomefonte.text()
            descricao = self.searchField_descricaofonte.text()
            if(nome == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, nome, descricao)
                self.statusbar.showMessage("Ready")
        elif whichtable is "ocupacao":
            Id = Controller.ControllerCountTable(whichtable, conn)
            emprego = self.searchField_emprego.text()
            descricao = self.searchField_descricaoocupacao.text()
            if(emprego == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, emprego, descricao)
                self.statusbar.showMessage("Ready")
        elif whichtable is "influenciaexterna":
            Id = Controller.ControllerCountTable(whichtable, conn)
            nome = self.searchField_nomeinfluencia.text()
            if(nome == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, nome)
                self.statusbar.showMessage("Ready")
        elif whichtable is "idioma":
            Id = Controller.ControllerCountTable(whichtable, conn)
            nome = self.searchField_nomeidioma.text()
            if(nome == ""):
                self.statusbar.showMessage("Preencha todos com *")
            else:
                Controller.ControllerInsertSubmitButton(whichtable, conn, Id, nome)
                self.statusbar.showMessage("Ready")

        elif whichtable is "autor_noticia":
            autorid = str(self.spinBox_autorid.value())
            noticiaid = str(self.spinBox_noticiaid.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, autorid)
            self.statusbar.showMessage("Ready")
        elif whichtable is "vitima_noticia":
            vitimaid = str(self.spinBox_vitimaid.value())
            noticiaid = str(self.spinBox_noticiaid_2.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, vitimaid)
            self.statusbar.showMessage("Ready")
        elif whichtable is "vitima_noticia":
            influenciaid = str(self.spinBox_influenciaid.value())
            noticiaid = str(self.spinBox_noticiaid_3.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, influenciaid)
            self.statusbar.showMessage("Ready")
        elif whichtable is "midia_noticia":
            midiaid = str(self.spinBox_midiaid.value())
            noticiaid = str(self.spinBox_noticiaid_4.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, midiaid)
            self.statusbar.showMessage("Ready")
        elif whichtable is "fonteconfiavel_noticia":
            fonteid = str(self.spinBox_fonteid.value())
            noticiaid = str(self.spinBox_noticiaid_5.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, fonteid)
            self.statusbar.showMessage("Ready")
        elif whichtable is "palavraschave_noticia":
            palavraschaveid = self.searchField_palavraschaveid.text()
            noticiaid = str(self.spinBox_noticiaid_6.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, palavraschaveid)
            self.statusbar.showMessage("Ready")
        elif whichtable is "local_noticia":
            localid = self.searchField_localid.text()
            noticiaid = str(self.spinBox_noticiaid_7.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, localid)
            self.statusbar.showMessage("Ready")
        elif whichtable is "categorianoticia_noticia":
            categoriaid = str(self.spinBox_categoriaid.value())
            noticiaid = str(self.spinBox_noticiaid_7.value())
            Controller.ControllerInsertSubmitButton(whichtable, conn, noticiaid, categoriaid)
            self.statusbar.showMessage("Ready")


    def clickinsertrelational(self):

        self.tabsInsertion.clear()

        self.where = 2
        self.page = 0

        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)

        self.autor_noticia_2 = QtWidgets.QWidget()
        self.autor_noticia_2.setEnabled(True)
        self.autor_noticia_2.setObjectName("autor_noticia_2")

        self.searchLabel_autorid = QtWidgets.QLabel(
            self.autor_noticia_2)
        self.searchLabel_autorid.setGeometry(
            QtCore.QRect(10, 85, 130, 20))
        self.searchLabel_autorid.setObjectName(
            "searchLabel_autorid")

        self.searchLabel_noticiaid = QtWidgets.QLabel(
            self.autor_noticia_2)
        self.searchLabel_noticiaid.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid.setObjectName(
            "searchLabel_noticiaid")

        self.spinBox_autorid = QtWidgets.QSpinBox(self.autor_noticia_2)
        self.spinBox_autorid.setGeometry(132, 83, 61, 27)
        self.spinBox_autorid.setMaximum(Controller.ControllerCountTable("pessoa", conn) - 1)
        self.spinBox_autorid.setObjectName("spinBox_autorid")


        self.spinBox_noticiaid = QtWidgets.QSpinBox(self.autor_noticia_2)
        self.spinBox_noticiaid.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid.setMaximum(Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid.setObjectName("spinBox_noticiaid")

        self.submitButton_autor_noticia = QtWidgets.QPushButton(
            self.autor_noticia_2)
        self.submitButton_autor_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_autor_noticia.setObjectName(
            "submitButton_autor_noticia")
        self.submitButton_autor_noticia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.autor_noticia_2, "")

        self.vitima_noticia_2 = QtWidgets.QWidget()
        self.vitima_noticia_2.setEnabled(True)
        self.vitima_noticia_2.setObjectName("vitima_noticia_2")

        self.searchLabel_vitimaid = QtWidgets.QLabel(
            self.vitima_noticia_2)
        self.searchLabel_vitimaid.setGeometry(
            QtCore.QRect(10, 85, 130, 20))
        self.searchLabel_vitimaid.setObjectName(
            "searchLabel_vitimaid")

        self.searchLabel_noticiaid_2 = QtWidgets.QLabel(
            self.vitima_noticia_2)
        self.searchLabel_noticiaid_2.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid_2.setObjectName(
            "searchLabel_noticiaid_2")

        self.spinBox_vitimaid = QtWidgets.QSpinBox(self.vitima_noticia_2)
        self.spinBox_vitimaid.setGeometry(132, 83, 61, 27)
        self.spinBox_vitimaid.setMaximum(
            Controller.ControllerCountTable("pessoa", conn) - 1)
        self.spinBox_vitimaid.setObjectName("spinBox_vitimaid")

        self.spinBox_noticiaid_2 = QtWidgets.QSpinBox(self.vitima_noticia_2)
        self.spinBox_noticiaid_2.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid_2.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid_2.setObjectName("spinBox_noticiaid")

        self.submitButton_vitima_noticia = QtWidgets.QPushButton(
            self.vitima_noticia_2)
        self.submitButton_vitima_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_vitima_noticia.setObjectName(
            "submitButton_vitima_noticia")
        self.submitButton_vitima_noticia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.vitima_noticia_2, "")

        self.influencia_noticia_2 = QtWidgets.QWidget()
        self.influencia_noticia_2.setEnabled(True)
        self.influencia_noticia_2.setObjectName("influencia_noticia_2")

        self.searchLabel_influenciaid = QtWidgets.QLabel(
            self.influencia_noticia_2)
        self.searchLabel_influenciaid.setGeometry(
            QtCore.QRect(10, 85, 143, 20))
        self.searchLabel_influenciaid.setObjectName(
            "searchLabel_influencia")

        self.searchLabel_noticiaid_3 = QtWidgets.QLabel(
            self.influencia_noticia_2)
        self.searchLabel_noticiaid_3.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid_3.setObjectName(
            "searchLabel_noticiaid_3")

        self.spinBox_influenciaid = QtWidgets.QSpinBox(self.influencia_noticia_2)
        self.spinBox_influenciaid.setGeometry(158, 83, 61, 27)
        self.spinBox_influenciaid.setMaximum(
            Controller.ControllerCountTable("influenciaexterna", conn) - 1)
        self.spinBox_vitimaid.setObjectName("spinBox_influenciaid")

        self.spinBox_noticiaid_3 = QtWidgets.QSpinBox(
            self.influencia_noticia_2)
        self.spinBox_noticiaid_3.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid_3.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid_2.setObjectName("spinBox_noticiaid")

        self.submitButton_influencia_noticia = QtWidgets.QPushButton(
            self.influencia_noticia_2)
        self.submitButton_influencia_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_influencia_noticia.setObjectName(
            "submitButton_influencia_noticia")
        self.submitButton_influencia_noticia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.influencia_noticia_2, "")

        self.midia_noticia_2 = QtWidgets.QWidget()
        self.midia_noticia_2.setEnabled(True)
        self.midia_noticia_2.setObjectName("midia_noticia_2")

        self.searchLabel_midiaid = QtWidgets.QLabel(
            self.midia_noticia_2)
        self.searchLabel_midiaid.setGeometry(
            QtCore.QRect(10, 85, 130, 20))
        self.searchLabel_midiaid.setObjectName(
            "searchLabel_midiaid")

        self.searchLabel_noticiaid_4 = QtWidgets.QLabel(
            self.midia_noticia_2)
        self.searchLabel_noticiaid_4.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid_4.setObjectName(
            "searchLabel_noticiaid_4")

        self.spinBox_midiaid = QtWidgets.QSpinBox(self.midia_noticia_2)
        self.spinBox_midiaid.setGeometry(132, 83, 61, 27)
        self.spinBox_midiaid.setMaximum(
            Controller.ControllerCountTable("midia", conn) - 1)
        self.spinBox_midiaid.setObjectName("spinBox_midiaid")

        self.spinBox_noticiaid_4 = QtWidgets.QSpinBox(self.midia_noticia_2)
        self.spinBox_noticiaid_4.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid_4.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid_4.setObjectName("spinBox_noticiaid")

        self.submitButton_midia_noticia = QtWidgets.QPushButton(
            self.midia_noticia_2)
        self.submitButton_midia_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_midia_noticia.setObjectName(
            "submitButton_midia_noticia")
        self.submitButton_midia_noticia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.midia_noticia_2, "")

        self.fonteconfiavel_noticia_2 = QtWidgets.QWidget()
        self.fonteconfiavel_noticia_2.setEnabled(True)
        self.fonteconfiavel_noticia_2.setObjectName("fonteconfiavel_noticia_2")

        self.searchLabel_fonteid = QtWidgets.QLabel(
            self.fonteconfiavel_noticia_2)
        self.searchLabel_fonteid.setGeometry(
            QtCore.QRect(10, 85, 182, 20))
        self.searchLabel_fonteid.setObjectName(
            "searchLabel_fonteid")

        self.searchLabel_noticiaid_5 = QtWidgets.QLabel(
            self.fonteconfiavel_noticia_2)
        self.searchLabel_noticiaid_5.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid_5.setObjectName(
            "searchLabel_noticiaid_5")

        self.spinBox_fonteid = QtWidgets.QSpinBox(self.fonteconfiavel_noticia_2)
        self.spinBox_fonteid.setGeometry(199, 83, 61, 27)
        self.spinBox_fonteid.setMaximum(
            Controller.ControllerCountTable("fonteconfiavel", conn) - 1)
        self.spinBox_fonteid.setObjectName("spinBox_fonteid")

        self.spinBox_noticiaid_5 = QtWidgets.QSpinBox(self.fonteconfiavel_noticia_2)
        self.spinBox_noticiaid_5.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid_5.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid_5.setObjectName("spinBox_noticiaid")

        self.submitButton_fonteconfiavel_noticia = QtWidgets.QPushButton(
            self.fonteconfiavel_noticia_2)
        self.submitButton_fonteconfiavel_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_fonteconfiavel_noticia.setObjectName(
            "submitButton_fonteconfiavel_noticia")
        self.submitButton_fonteconfiavel_noticia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.fonteconfiavel_noticia_2, "")

        self.palavraschave_noticia_2 = QtWidgets.QWidget()
        self.palavraschave_noticia_2.setEnabled(True)
        self.palavraschave_noticia_2.setObjectName("palavraschave_noticia_2")

        self.searchLabel_palavraschaveid = QtWidgets.QLabel(
            self.palavraschave_noticia_2)
        self.searchLabel_palavraschaveid.setGeometry(
            QtCore.QRect(10, 85, 182, 20))
        self.searchLabel_palavraschaveid.setObjectName(
            "searchLabel_palavraschaveid")

        self.searchLabel_noticiaid_6 = QtWidgets.QLabel(
            self.palavraschave_noticia_2)
        self.searchLabel_noticiaid_6.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid_6.setObjectName(
            "searchLabel_noticiaid_6")

        self.searchField_palavraschaveid = QtWidgets.QLineEdit(
            self.palavraschave_noticia_2)
        self.searchField_palavraschaveid.setGeometry(
            QtCore.QRect(120, 83, 120, 29))
        self.searchField_palavraschaveid.setObjectName(
            "searchField_palavraschaveid")

        self.spinBox_noticiaid_6 = QtWidgets.QSpinBox(
            self.palavraschave_noticia_2)
        self.spinBox_noticiaid_6.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid_6.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid_6.setObjectName("spinBox_noticiaid")

        self.submitButton_palavraschave_noticia = QtWidgets.QPushButton(
            self.palavraschave_noticia_2)
        self.submitButton_palavraschave_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_palavraschave_noticia.setObjectName(
            "submitButton_palavraschave_noticia")
        self.submitButton_palavraschave_noticia.clicked.connect(
            self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.palavraschave_noticia_2, "")

        self.local_noticia_2 = QtWidgets.QWidget()
        self.local_noticia_2.setEnabled(True)
        self.local_noticia_2.setObjectName("local_noticia_2")

        self.searchLabel_localid = QtWidgets.QLabel(
            self.local_noticia_2)
        self.searchLabel_localid.setGeometry(
            QtCore.QRect(10, 85, 182, 20))
        self.searchLabel_localid.setObjectName(
            "searchLabel_localid")

        self.searchLabel_noticiaid_7 = QtWidgets.QLabel(
            self.local_noticia_2)
        self.searchLabel_noticiaid_7.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid_7.setObjectName(
            "searchLabel_noticiaid_7")

        self.searchField_localid = QtWidgets.QLineEdit(
            self.local_noticia_2)
        self.searchField_localid.setGeometry(
            QtCore.QRect(65, 83, 120, 29))
        self.searchField_localid.setObjectName(
            "searchField_localid")

        self.spinBox_noticiaid_7 = QtWidgets.QSpinBox(
            self.local_noticia_2)
        self.spinBox_noticiaid_7.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid_7.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid_7.setObjectName("spinBox_noticiaid")

        self.submitButton_local_noticia = QtWidgets.QPushButton(
            self.local_noticia_2)
        self.submitButton_local_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_local_noticia.setObjectName(
            "submitButton_local_noticia")
        self.submitButton_local_noticia.clicked.connect(
            self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.local_noticia_2, "")

        self.categorianoticia_noticia_2 = QtWidgets.QWidget()
        self.categorianoticia_noticia_2.setEnabled(True)
        self.categorianoticia_noticia_2.setObjectName("categorianoticia_noticia_2")

        self.searchLabel_categoriaid = QtWidgets.QLabel(
            self.categorianoticia_noticia_2)
        self.searchLabel_categoriaid.setGeometry(
            QtCore.QRect(10, 85, 182, 20))
        self.searchLabel_categoriaid.setObjectName(
            "searchLabel_categoriaid")

        self.searchLabel_noticiaid_8 = QtWidgets.QLabel(
            self.categorianoticia_noticia_2)
        self.searchLabel_noticiaid_8.setGeometry(
            QtCore.QRect(10, 35, 130, 20))
        self.searchLabel_noticiaid_8.setObjectName(
            "searchLabel_noticiaid_8")

        self.spinBox_categoriaid = QtWidgets.QSpinBox(
            self.categorianoticia_noticia_2)
        self.spinBox_categoriaid.setGeometry(96, 83, 61, 27)
        self.spinBox_categoriaid.setMaximum(
            Controller.ControllerCountTable("categorianoticia", conn) - 1)
        self.spinBox_categoriaid.setObjectName("spinBox_categoriaid")

        self.spinBox_noticiaid_8 = QtWidgets.QSpinBox(
            self.categorianoticia_noticia_2)
        self.spinBox_noticiaid_8.setGeometry(140, 33, 61, 27)
        self.spinBox_noticiaid_8.setMaximum(
            Controller.ControllerCountTable("noticia", conn) - 1)
        self.spinBox_noticiaid_8.setObjectName("spinBox_noticiaid")

        self.submitButton_categorianoticia_noticia = QtWidgets.QPushButton(
            self.categorianoticia_noticia_2)
        self.submitButton_categorianoticia_noticia.setGeometry(
            QtCore.QRect(20, 120, 101, 29))
        self.submitButton_categorianoticia_noticia.setObjectName(
            "submitButton_categorianoticia_noticia")
        self.submitButton_categorianoticia_noticia.clicked.connect(
            self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.categorianoticia_noticia_2, "")

        _translate = QtCore.QCoreApplication.translate
        self.searchLabel_autorid.setText(
            _translate("MainWindow", "Índice do Autor*:"))
        self.searchLabel_noticiaid.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_autor_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.autor_noticia_2), _translate("MainWindow", "Notícia/Autor"))
        self.searchLabel_vitimaid.setText(
            _translate("MainWindow", "Índice da Vítima*:"))
        self.searchLabel_noticiaid_2.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_vitima_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.vitima_noticia_2), _translate("MainWindow", "Notícia/Vítima"))
        self.searchLabel_influenciaid.setText(
            _translate("MainWindow", "Índice da Influência*:"))
        self.searchLabel_noticiaid_3.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_influencia_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.influencia_noticia_2), _translate("MainWindow", "Notícia/Influência"))
        self.searchLabel_midiaid.setText(
            _translate("MainWindow", "Índice da Mídia*:"))
        self.searchLabel_noticiaid_4.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_midia_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.midia_noticia_2), _translate("MainWindow", "Notícia/Mídia"))
        self.searchLabel_fonteid.setText(
            _translate("MainWindow", "Índice da Fonte Confiável*:"))
        self.searchLabel_noticiaid_5.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_fonteconfiavel_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.fonteconfiavel_noticia_2), _translate("MainWindow", "Notícia/Fonte Confiável"))
        self.searchLabel_palavraschaveid.setText(
            _translate("MainWindow", "Palavra Chave*:"))
        self.searchLabel_noticiaid_6.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_palavraschave_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.palavraschave_noticia_2), _translate("MainWindow", "Notícia/Palavra Chave"))
        self.searchLabel_localid.setText(
            _translate("MainWindow", "Local*:"))
        self.searchLabel_noticiaid_7.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_local_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.local_noticia_2), _translate("MainWindow", "Notícia/Local"))
        self.searchLabel_categoriaid.setText(
            _translate("MainWindow", "Categoria*:"))
        self.searchLabel_noticiaid_8.setText(
            _translate("MainWindow", "Índice do Notícia*:"))
        self.submitButton_categorianoticia_noticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.categorianoticia_noticia_2), _translate("MainWindow", "Notícia/Categoria da Notícia"))


    def clickinsertnormal(self):

        self.tabsInsertion.clear()

        self.where = 0
        self.page = 0

        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)

        self.categorianoticia_2 = QtWidgets.QWidget()
        self.categorianoticia_2.setEnabled(True)
        self.categorianoticia_2.setObjectName("categorianoticia_2")

        self.searchLabel_nomecategorian = QtWidgets.QLabel(
            self.categorianoticia_2)
        self.searchLabel_nomecategorian.setGeometry(
            QtCore.QRect(10, 10, 61, 20))
        self.searchLabel_nomecategorian.setObjectName(
            "searchLabel_nomecategorian")
        self.searchLabel_descricaocategorian = QtWidgets.QLabel(
            self.categorianoticia_2)
        self.searchLabel_descricaocategorian.setGeometry(
            QtCore.QRect(10, 90, 81, 20))
        self.searchLabel_descricaocategorian.setObjectName(
            "searchLabel_descricaocategorian")

        self.searchField_nomecategorian = QtWidgets.QLineEdit(
            self.categorianoticia_2)
        self.searchField_nomecategorian.setGeometry(
            QtCore.QRect(80, 10, 291, 61))
        self.searchField_nomecategorian.setObjectName(
            "searchField_nomecategorian")

        self.searchField_descricaocategorian = QtWidgets.QLineEdit(
            self.categorianoticia_2)
        self.searchField_descricaocategorian.setGeometry(
            QtCore.QRect(110, 90, 441, 221))
        self.searchField_descricaocategorian.setObjectName(
            "searchField_descricaocategorian")

        self.submitButton_categorianoticia = QtWidgets.QPushButton(
            self.categorianoticia_2)
        self.submitButton_categorianoticia.setGeometry(
            QtCore.QRect(20, 340, 101, 29))
        self.submitButton_categorianoticia.setObjectName(
            "submitButton_categorianoticia")
        self.submitButton_categorianoticia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.categorianoticia_2, "")

        self.noticia_2 = QtWidgets.QWidget()
        self.noticia_2.setObjectName("noticia_2")
        self.searchLabel_manchete = QtWidgets.QLabel(self.noticia_2)

        self.searchLabel_manchete.setGeometry(QtCore.QRect(30, 30, 91, 20))
        self.searchLabel_manchete.setObjectName("searchLabel_manchete")
        self.searchLabel_descricaonoticia = QtWidgets.QLabel(self.noticia_2)
        self.searchLabel_descricaonoticia.setGeometry(
            QtCore.QRect(30, 110, 81, 20))
        self.searchLabel_descricaonoticia.setObjectName(
            "searchLabel_descricaonoticia")
        self.searchLabel_consequencia = QtWidgets.QLabel(self.noticia_2)
        self.searchLabel_consequencia.setGeometry(
            QtCore.QRect(10, 350, 111, 20))
        self.searchLabel_consequencia.setObjectName("searchLabel_consequencia")
        self.searchLabel_popularidade = QtWidgets.QLabel(self.noticia_2)
        self.searchLabel_popularidade.setGeometry(
            QtCore.QRect(600, 20, 111, 21))
        self.searchLabel_popularidade.setObjectName("searchLabel_popularidade")
        self.searchLabel_data = QtWidgets.QLabel(self.noticia_2)
        self.searchLabel_data.setGeometry(QtCore.QRect(780, 10, 151, 51))
        self.searchLabel_data.setObjectName("searchLabel_data")
        self.searchLabel_piada = QtWidgets.QLabel(self.noticia_2)
        self.searchLabel_piada.setGeometry(QtCore.QRect(600, 90, 111, 21))
        self.searchLabel_piada.setObjectName("searchLabel_piada")


        self.searchField_manchete = QtWidgets.QLineEdit(self.noticia_2)
        self.searchField_manchete.setGeometry(QtCore.QRect(120, 10, 441, 61))
        self.searchField_manchete.setObjectName("searchField_manchete")

        self.searchField_descricaonoticia = QtWidgets.QLineEdit(self.noticia_2)
        self.searchField_descricaonoticia.setGeometry(
            QtCore.QRect(120, 90, 441, 221))
        self.searchField_descricaonoticia.setObjectName(
            "searchField_descricaonoticia")
        self.searchField_consequencia = QtWidgets.QLineEdit(self.noticia_2)
        self.searchField_consequencia.setGeometry(
            QtCore.QRect(120, 330, 441, 221))
        self.searchField_consequencia.setObjectName("searchField_consequencia")

        self.spinBox_ano = QtWidgets.QSpinBox(self.noticia_2)
        self.spinBox_ano.setGeometry(QtCore.QRect(930, 20, 61, 27))
        self.spinBox_ano.setMinimum(1)
        self.spinBox_ano.setMaximum(3000)
        self.spinBox_ano.setObjectName("spinBox_ano")

        self.spinBox_mes = QtWidgets.QSpinBox(self.noticia_2)
        self.spinBox_mes.setGeometry(QtCore.QRect(1000, 20, 48, 27))
        self.spinBox_mes.setMinimum(1)
        self.spinBox_mes.setMaximum(12)
        self.spinBox_mes.setObjectName("spinBox_mes")

        self.spinBox_dias = QtWidgets.QSpinBox(self.noticia_2)
        self.spinBox_dias.setGeometry(QtCore.QRect(1060, 20, 48, 27))
        self.spinBox_dias.setMinimum(1)
        self.spinBox_dias.setMaximum(31)
        self.spinBox_dias.setObjectName("spinBox_dias")

        self.spinBox_popularidade = QtWidgets.QSpinBox(self.noticia_2)
        self.spinBox_popularidade.setGeometry(QtCore.QRect(720, 20, 48, 27))
        self.spinBox_popularidade.setObjectName("spinBox_popularidade")

        self.checkBox = QtWidgets.QCheckBox(self.noticia_2)
        self.checkBox.setGeometry(QtCore.QRect(710, 90, 21, 22))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")

        self.submitButton_noticia = QtWidgets.QPushButton(self.noticia_2)
        self.submitButton_noticia.setGeometry(QtCore.QRect(620, 260, 101, 29))
        self.submitButton_noticia.setObjectName("submitButton_noticia")
        self.submitButton_noticia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.noticia_2, "")

        self.tab_categoriamidia_2 = QtWidgets.QWidget()
        self.tab_categoriamidia_2.setObjectName("tab_categoriamidia_2")

        self.searchLabel_nomecategoriam = QtWidgets.QLabel(
            self.tab_categoriamidia_2)
        self.searchLabel_nomecategoriam.setGeometry(
            QtCore.QRect(10, 10, 61, 20))
        self.searchLabel_nomecategoriam.setObjectName(
            "searchLabel_nomecategoriam")
        self.searchLabel_descricaocategoriam = QtWidgets.QLabel(
            self.tab_categoriamidia_2)
        self.searchLabel_descricaocategoriam.setGeometry(
            QtCore.QRect(10, 90, 81, 20))
        self.searchLabel_descricaocategoriam.setObjectName(
            "searchLabel_descricaocategoriam")

        self.searchField_descricaocategoriam = QtWidgets.QLineEdit(
            self.tab_categoriamidia_2)
        self.searchField_descricaocategoriam.setGeometry(
            QtCore.QRect(110, 90, 441, 221))
        self.searchField_descricaocategoriam.setObjectName(
            "searchField_descricaocategoriam")


        self.searchField_nomecategoriam = QtWidgets.QLineEdit(
            self.tab_categoriamidia_2)
        self.searchField_nomecategoriam.setGeometry(
            QtCore.QRect(80, 10, 291, 61))
        self.searchField_nomecategoriam.setObjectName(
            "searchField_nomecategoriam")

        self.submitButton_categoriamidia = QtWidgets.QPushButton(
            self.tab_categoriamidia_2)
        self.submitButton_categoriamidia.setGeometry(
            QtCore.QRect(20, 340, 101, 29))
        self.submitButton_categoriamidia.setObjectName(
            "submitButton_categoriamidia")
        self.submitButton_categoriamidia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_categoriamidia_2, "")

        self.tab_midia_2 = QtWidgets.QWidget()
        self.tab_midia_2.setObjectName("tab_midia_2")

        self.searchLabel_nomemidia = QtWidgets.QLabel(self.tab_midia_2)
        self.searchLabel_nomemidia.setGeometry(QtCore.QRect(10, 10, 61, 20))
        self.searchLabel_nomemidia.setObjectName("searchLabel_nomemidia")
        self.searchLabel_descricaomidia = QtWidgets.QLabel(self.tab_midia_2)
        self.searchLabel_descricaomidia.setGeometry(
            QtCore.QRect(10, 90, 81, 20))
        self.searchLabel_descricaomidia.setObjectName(
            "searchLabel_descricaomidia")
        self.searchLabel_categoriamidia = QtWidgets.QLabel(self.tab_midia_2)
        self.searchLabel_categoriamidia.setGeometry(
            QtCore.QRect(10, 340, 81, 31))
        self.searchLabel_categoriamidia.setObjectName(
            "searchLabel_categoriamidia")

        self.searchField_descricaomidia = QtWidgets.QLineEdit(self.tab_midia_2)
        self.searchField_descricaomidia.setGeometry(
            QtCore.QRect(110, 90, 441, 221))
        self.searchField_descricaomidia.setObjectName(
            "searchField_descricaomidia")

        self.searchField_nomemidia = QtWidgets.QLineEdit(self.tab_midia_2)
        self.searchField_nomemidia.setGeometry(QtCore.QRect(80, 10, 291, 61))
        self.searchField_nomemidia.setObjectName("searchField_nomemidia")

        self.spinBox_categoriamidia = QtWidgets.QSpinBox(self.tab_midia_2)
        self.spinBox_categoriamidia.setGeometry(QtCore.QRect(100, 340, 48, 27))
        self.spinBox_categoriamidia.setObjectName("spinBox_categoriamidia")
        self.spinBox_categoriamidia.setMaximum(Controller.ControllerCountTable("categoriamidia", conn) - 1)


        self.submitButton_midia = QtWidgets.QPushButton(self.tab_midia_2)
        self.submitButton_midia.setGeometry(QtCore.QRect(10, 400, 101, 29))
        self.submitButton_midia.setObjectName("submitButton_midia")
        self.submitButton_midia.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_midia_2, "")

        self.tab_pessoa_2 = QtWidgets.QWidget()
        self.tab_pessoa_2.setObjectName("tab_pessoa_2")

        self.searchLabel_ocupacao = QtWidgets.QLabel(self.tab_pessoa_2)
        self.searchLabel_ocupacao.setGeometry(QtCore.QRect(20, 110, 81, 20))
        self.searchLabel_ocupacao.setObjectName("searchLabel_ocupacao")
        self.searchLabel_idade = QtWidgets.QLabel(self.tab_pessoa_2)
        self.searchLabel_idade.setGeometry(QtCore.QRect(180, 110, 71, 20))
        self.searchLabel_idade.setObjectName("searchLabel_idade")
        self.searchLabel_nomepessoa = QtWidgets.QLabel(self.tab_pessoa_2)
        self.searchLabel_nomepessoa.setGeometry(QtCore.QRect(20, 30, 61, 20))
        self.searchLabel_nomepessoa.setObjectName("searchLabel_nomepessoa")

        self.spinBox_ocupacao = QtWidgets.QSpinBox(self.tab_pessoa_2)
        self.spinBox_ocupacao.setGeometry(QtCore.QRect(110, 110, 48, 27))
        self.spinBox_ocupacao.setObjectName("spinBox_ocupacao")
        self.spinBox_ocupacao.setMaximum(Controller.ControllerCountTable("ocupacao", conn) - 1)

        self.searchField_nomepessoa = QtWidgets.QLineEdit(self.tab_pessoa_2)
        self.searchField_nomepessoa.setGeometry(QtCore.QRect(80, 20, 441, 61))
        self.searchField_nomepessoa.setObjectName("searchField_nomepessoa")

        self.spinBox_idade = QtWidgets.QSpinBox(self.tab_pessoa_2)
        self.spinBox_idade.setGeometry(QtCore.QRect(230, 110, 48, 27))
        self.spinBox_idade.setObjectName("spinBox_idade")
        self.spinBox_idade.setMinimum(1)

        self.submitButton_pessoa = QtWidgets.QPushButton(self.tab_pessoa_2)
        self.submitButton_pessoa.setGeometry(QtCore.QRect(20, 170, 101, 29))
        self.submitButton_pessoa.setObjectName("submitButton_pessoa")
        self.submitButton_pessoa.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_pessoa_2, "")

        self.tab_palavraschave_2 = QtWidgets.QWidget()
        self.tab_palavraschave_2.setObjectName("tab_palavraschave_2")

        self.searchLabel_nomepalavra = QtWidgets.QLabel(
            self.tab_palavraschave_2)
        self.searchLabel_nomepalavra.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.searchLabel_nomepalavra.setObjectName("searchLabel_nomepalavra")
        self.searchLabel_idioma = QtWidgets.QLabel(self.tab_palavraschave_2)
        self.searchLabel_idioma.setGeometry(QtCore.QRect(20, 130, 61, 20))
        self.searchLabel_idioma.setObjectName("searchLabel_idioma")

        self.searchField_nomepalavra = QtWidgets.QLineEdit(
            self.tab_palavraschave_2)
        self.searchField_nomepalavra.setGeometry(QtCore.QRect(90, 30, 441, 61))
        self.searchField_nomepalavra.setObjectName("searchField_nomepalavra")

        self.spinBox_idioma = QtWidgets.QSpinBox(self.tab_palavraschave_2)
        self.spinBox_idioma.setGeometry(QtCore.QRect(85, 127, 48, 27))
        self.spinBox_idioma.setObjectName("spinBox_idioma")
        self.spinBox_idioma.setMaximum(Controller.ControllerCountTable("idioma", conn) - 1)

        self.submitButton_palavraschave = QtWidgets.QPushButton(
            self.tab_palavraschave_2)
        self.submitButton_palavraschave.setGeometry(
            QtCore.QRect(20, 210, 101, 29))
        self.submitButton_palavraschave.setObjectName(
            "submitButton_palavraschave")
        self.submitButton_palavraschave.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_palavraschave_2, "")

        self.tab_local_2 = QtWidgets.QWidget()
        self.tab_local_2.setObjectName("tab_local_2")

        self.searchLabel_sigla = QtWidgets.QLabel(self.tab_local_2)
        self.searchLabel_sigla.setGeometry(QtCore.QRect(10, 10, 61, 20))
        self.searchLabel_sigla.setObjectName("searchLabel_sigla")
        self.searchLabel_complemento = QtWidgets.QLabel(self.tab_local_2)
        self.searchLabel_complemento.setGeometry(
            QtCore.QRect(10, 160, 111, 20))
        self.searchLabel_complemento.setObjectName("searchLabel_complemento")
        self.searchLabel_nomelocal = QtWidgets.QLabel(self.tab_local_2)
        self.searchLabel_nomelocal.setGeometry(QtCore.QRect(10, 70, 61, 20))
        self.searchLabel_nomelocal.setObjectName("searchLabel_nomelocal")

        self.searchField_complemento = QtWidgets.QLineEdit(self.tab_local_2)
        self.searchField_complemento.setGeometry(
            QtCore.QRect(120, 160, 441, 221))
        self.searchField_complemento.setObjectName("searchField_complemento")

        self.searchField_sigla = QtWidgets.QLineEdit(self.tab_local_2)
        self.searchField_sigla.setGeometry(QtCore.QRect(60, 10, 61, 31))
        self.searchField_sigla.setObjectName("searchField_sigla")
        self.searchField_nomelocal = QtWidgets.QLineEdit(self.tab_local_2)
        self.searchField_nomelocal.setGeometry(QtCore.QRect(70, 50, 191, 81))
        self.searchField_nomelocal.setObjectName("searchField_nomelocal")

        self.submitButton_local = QtWidgets.QPushButton(self.tab_local_2)
        self.submitButton_local.setGeometry(QtCore.QRect(10, 400, 101, 29))
        self.submitButton_local.setObjectName("submitButton_local")
        self.submitButton_local.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_local_2, "")

        self.tab_fonteconfiavel_2 = QtWidgets.QWidget()
        self.tab_fonteconfiavel_2.setObjectName("tab_fonteconfiavel_2")

        self.searchLabel_nomefonte = QtWidgets.QLabel(
            self.tab_fonteconfiavel_2)
        self.searchLabel_nomefonte.setGeometry(QtCore.QRect(20, 30, 61, 20))
        self.searchLabel_nomefonte.setObjectName("searchLabel_nomefonte")
        self.searchLabel_descricaofonte = QtWidgets.QLabel(
            self.tab_fonteconfiavel_2)
        self.searchLabel_descricaofonte.setGeometry(
            QtCore.QRect(10, 120, 81, 20))
        self.searchLabel_descricaofonte.setObjectName(
            "searchLabel_descricaofonte")
        
        self.searchField_nomefonte = QtWidgets.QLineEdit(
            self.tab_fonteconfiavel_2)
        self.searchField_nomefonte.setGeometry(QtCore.QRect(80, 20, 441, 61))
        self.searchField_nomefonte.setObjectName("searchField_nomefonte")

        self.searchField_descricaofonte = QtWidgets.QLineEdit(
            self.tab_fonteconfiavel_2)
        self.searchField_descricaofonte.setGeometry(
            QtCore.QRect(100, 100, 441, 221))
        self.searchField_descricaofonte.setObjectName(
            "searchField_descricaofonte")

        self.submitButton_fonteconfiavel = QtWidgets.QPushButton(
            self.tab_fonteconfiavel_2)
        self.submitButton_fonteconfiavel.setGeometry(
            QtCore.QRect(10, 410, 101, 29))
        self.submitButton_fonteconfiavel.setObjectName(
            "submitButton_fonteconfiavel")
        self.submitButton_fonteconfiavel.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_fonteconfiavel_2, "")

        self.tab_ocupacao_2 = QtWidgets.QWidget()
        self.tab_ocupacao_2.setObjectName("tab_ocupacao_2")

        self.searchLabel_emprego = QtWidgets.QLabel(self.tab_ocupacao_2)
        self.searchLabel_emprego.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.searchLabel_emprego.setObjectName("searchLabel_emprego")
        self.searchLabel_descricaoocupacao = QtWidgets.QLabel(
            self.tab_ocupacao_2)
        self.searchLabel_descricaoocupacao.setGeometry(
            QtCore.QRect(20, 110, 81, 20))
        self.searchLabel_descricaoocupacao.setObjectName(
            "searchLabel_descricaoocupacao")

        self.searchField_descricaoocupacao = QtWidgets.QLineEdit(
            self.tab_ocupacao_2)
        self.searchField_descricaoocupacao.setGeometry(
            QtCore.QRect(100, 90, 441, 221))
        self.searchField_descricaoocupacao.setObjectName(
            "searchField_descricaoocupacao")

        self.searchField_emprego = QtWidgets.QLineEdit(self.tab_ocupacao_2)
        self.searchField_emprego.setGeometry(QtCore.QRect(100, 10, 441, 61))
        self.searchField_emprego.setObjectName("searchField_emprego")

        self.submitButton_ocupacao = QtWidgets.QPushButton(self.tab_ocupacao_2)
        self.submitButton_ocupacao.setGeometry(QtCore.QRect(10, 340, 101, 29))
        self.submitButton_ocupacao.setObjectName("submitButton_ocupacao")
        self.submitButton_ocupacao.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_ocupacao_2, "")

        self.tab_influenciaexterna_2 = QtWidgets.QWidget()
        self.tab_influenciaexterna_2.setObjectName("tab_influenciaexterna_2")

        self.searchLabel_nomeinfluencia = QtWidgets.QLabel(
            self.tab_influenciaexterna_2)
        self.searchLabel_nomeinfluencia.setGeometry(
            QtCore.QRect(10, 10, 61, 20))
        self.searchLabel_nomeinfluencia.setObjectName(
            "searchLabel_nomeinfluencia")

        self.searchField_nomeinfluencia = QtWidgets.QLineEdit(
            self.tab_influenciaexterna_2)
        self.searchField_nomeinfluencia.setGeometry(
            QtCore.QRect(80, 10, 291, 61))
        self.searchField_nomeinfluencia.setObjectName(
            "searchField_nomeinfluencia")

        self.submitButton_influenciaexterna = QtWidgets.QPushButton(
            self.tab_influenciaexterna_2)
        self.submitButton_influenciaexterna.setGeometry(
            QtCore.QRect(10, 90, 101, 29))
        self.submitButton_influenciaexterna.setObjectName(
            "submitButton_influenciaexterna")
        self.submitButton_influenciaexterna.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_influenciaexterna_2, "")

        self.tab_idioma_2 = QtWidgets.QWidget()
        self.tab_idioma_2.setObjectName("tab_idioma_2")

        self.searchLabel_nomeidioma = QtWidgets.QLabel(
            self.tab_idioma_2)
        self.searchLabel_nomeidioma.setGeometry(
            QtCore.QRect(10, 10, 61, 20))
        self.searchLabel_nomeidioma.setObjectName(
            "searchLabel_nomeidioma")

        self.searchField_nomeidioma = QtWidgets.QLineEdit(
            self.tab_idioma_2)
        self.searchField_nomeidioma.setGeometry(
            QtCore.QRect(80, 10, 291, 61))
        self.searchField_nomeidioma.setObjectName(
            "searchField_nomeidioma")

        self.submitButton_idioma = QtWidgets.QPushButton(
            self.tab_idioma_2)
        self.submitButton_idioma.setGeometry(
            QtCore.QRect(10, 90, 101, 29))
        self.submitButton_idioma.setObjectName(
            "submitButton_idioma")
        self.submitButton_idioma.clicked.connect(self.clicksubmitinsert)

        self.tabsInsertion.addTab(self.tab_idioma_2, "")

        _translate = QtCore.QCoreApplication.translate
        self.searchLabel_nomecategorian.setText(
            _translate("MainWindow", "Nome*:"))
        self.searchLabel_descricaocategorian.setText(
            _translate("MainWindow", "Descrição*:"))
        self.submitButton_categorianoticia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.categorianoticia_2), _translate("MainWindow", "Categoria Notícia"))
        self.searchLabel_manchete.setText(
            _translate("MainWindow", "Manchete*:"))
        self.searchLabel_descricaonoticia.setText(
            _translate("MainWindow", "Descrição:"))
        self.searchLabel_consequencia.setText(
            _translate("MainWindow", "Consequência:"))
        self.searchLabel_popularidade.setText(
            _translate("MainWindow", "Popularidade:"))
        self.searchLabel_data.setText(
            _translate("MainWindow", "Data(YYYY/MM/DD):"))
        self.searchLabel_piada.setText(
            _translate("MainWindow", "Foi uma piada?"))
        self.submitButton_noticia.setText(_translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.noticia_2), _translate("MainWindow", "Notícia"))
        self.searchLabel_nomecategoriam.setText(
            _translate("MainWindow", "Nome*:"))
        self.searchLabel_descricaocategoriam.setText(
            _translate("MainWindow", "Descrição*:"))
        self.submitButton_categoriamidia.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_categoriamidia_2), _translate("MainWindow", "Categoria Mídia"))
        self.searchLabel_nomemidia.setText(_translate("MainWindow", "Nome*:"))
        self.searchLabel_descricaomidia.setText(
            _translate("MainWindow", "Descrição:"))
        self.searchLabel_categoriamidia.setText(
            _translate("MainWindow", "Categoria*:"))
        self.submitButton_midia.setText(_translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_midia_2), _translate("MainWindow", "Mídia"))
        self.searchLabel_ocupacao.setText(
            _translate("MainWindow", "Ocupação*:"))
        self.searchLabel_nomepessoa.setText(_translate("MainWindow", "Nome*:"))
        self.searchLabel_idade.setText(_translate("MainWindow", "Idade:"))
        self.submitButton_pessoa.setText(_translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_pessoa_2), _translate("MainWindow", "Pessoa"))
        self.searchLabel_nomepalavra.setText(
            _translate("MainWindow", "Nome*:"))
        self.searchLabel_idioma.setText(_translate("MainWindow", "Idioma*:"))
        self.submitButton_palavraschave.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_palavraschave_2), _translate("MainWindow", "Palavras Chave"))
        self.searchLabel_nomefonte.setText(_translate("MainWindow", "Nome*:"))
        self.searchLabel_descricaofonte.setText(
            _translate("MainWindow", "Descrição:"))
        self.submitButton_fonteconfiavel.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_fonteconfiavel_2), _translate("MainWindow", "Fonte Confiável"))
        self.searchLabel_sigla.setText(_translate("MainWindow", "Sigla*:"))
        self.searchLabel_complemento.setText(
            _translate("MainWindow", "Complemento:"))
        self.searchLabel_nomelocal.setText(_translate("MainWindow", "Nome*:"))
        self.submitButton_local.setText(_translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_local_2), _translate("MainWindow", "Local"))
        self.searchLabel_emprego.setText(_translate("MainWindow", "Emprego*:"))
        self.searchLabel_descricaoocupacao.setText(
            _translate("MainWindow", "Descrição:"))
        self.submitButton_ocupacao.setText(_translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_ocupacao_2), _translate("MainWindow", "Ocupação"))
        self.searchLabel_nomeinfluencia.setText(
            _translate("MainWindow", "Nome*:"))
        self.submitButton_influenciaexterna.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_influenciaexterna_2), _translate("MainWindow", "Influência Externa"))
        self.searchLabel_nomeidioma.setText(
            _translate("MainWindow", "Nome*:"))
        self.submitButton_idioma.setText(
            _translate("MainWindow", "Submit"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(
            self.tab_idioma_2), _translate("MainWindow", "Idioma"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.Full_NoticiaButton.setText(_translate("MainWindow", "Notícia Completa"))
        self.Autor_VitimaButton.setText(_translate("MainWindow", "Autor - Vítima"))
        self.Pessoa_OcupacaoButton.setText(_translate("MainWindow", "Pessoa - Ocupação"))
        self.Midia_CategoriaMButton.setText(_translate("MainWindow", "Mídia - Categoria"))
        self.Noticia_CategoriaNButton.setText(_translate("MainWindow", "Notícia - Categoria"))
        self.Influencia_NoticiaButton.setText(_translate("MainWindow", "Influência - Notícia"))
        self.Midia_NoticiaButton.setText(_translate("MainWindow", "Mídia - Notícia"))
        self.FonteConfiavel_NoticiaButton.setText(_translate("MainWindow", "Fonte - Notícia"))
        self.PalavrasChave_NoticiaButton.setText(_translate("MainWindow", "Chave - Notícia"))
        self.Local_NoticiaButton.setText(_translate("MainWindow", "Local - Notícia"))

        self.refreshButton.setText(_translate("MainWindow", "Atualizar"))
        self.searchButton.setText(_translate("MainWindow", "Buscar"))
        self.normalButton.setText(_translate("MainWindow", "Tabelas Entidades"))
        self.relationalButton.setText(_translate("MainWindow", "Tabelas Relacionais"))
        self.viewsLabel.setText(_translate("MainWindow", "Views"))
        self.searchLabel.setText(_translate("MainWindow", "Digite sua busca por coluna de acordo com a tabela atual"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Selection), _translate("MainWindow", "Selection"))


        self.insertnormalButton.setText(_translate("MainWindow", "Tabelas Entidades"))
        self.insertrelationalButton.setText(_translate("MainWindow", "Tabelas Relacionais"))
        self.instruction.setText(_translate("MainWindow", "Insira de acordo com a tabela atual. Campos com (*) são de preenchimento obrigatório"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Insertion), _translate("MainWindow", "Insertion"))

        self.deletenormalButton.setText(_translate("MainWindow", "Tabelas Entidades"))
        self.deleterelationalButton.setText(_translate("MainWindow", "Tabelas Relacionais"))

        self.instruction_2.setText(_translate("MainWindow", "Será deletado do banco de acordo com o campo de chave primária preenchido"))
        # self.searchLabel_nomecategorian_2.setText(_translate("MainWindow", "Nome:"))
        # self.searchLabel_descricaocategorian_2.setText(_translate("MainWindow", "Descrição:"))
        # self.submitButton_categorianoticia_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.categorianoticia_3), _translate("MainWindow", "Categoria Notícia"))
        # self.searchLabel_manchete_2.setText(_translate("MainWindow", "Manchete:"))
        # self.searchLabel_descricaonoticia_2.setText(_translate("MainWindow", "Descrição:"))
        # self.searchLabel_consequencia_2.setText(_translate("MainWindow", "Consequência:"))
        # self.searchLabel_popularidade_2.setText(_translate("MainWindow", "Popularidade:"))
        # self.searchLabel_data_2.setText(_translate("MainWindow", "Data(YYYY/MM/DD):"))
        # self.searchLabel_piada_2.setText(_translate("MainWindow", "Foi uma piada?"))
        # self.searchLabel_influenciaexterna_2.setText(_translate("MainWindow", "Influência Externa:"))
        # self.submitButton_noticia_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.noticia_3), _translate("MainWindow", "Notícia"))
        # self.searchLabel_nomecategoriam_2.setText(_translate("MainWindow", "Nome:"))
        # self.searchLabel_descricaocategoriam_2.setText(_translate("MainWindow", "Descrição:"))
        # self.submitButton_categoriamidia_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_categoriamidia_3), _translate("MainWindow", "Categoria Mídia"))
        # self.searchLabel_nomemidia_2.setText(_translate("MainWindow", "Nome:"))
        # self.searchLabel_descricaomidia_2.setText(_translate("MainWindow", "Descrição:"))
        # self.searchLabel_categoriamidia_2.setText(_translate("MainWindow", "Categoria:"))
        # self.submitButton_midia_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_midia_3), _translate("MainWindow", "Mídia"))
        # self.searchLabel_ocupacao_2.setText(_translate("MainWindow", "Ocupação:"))
        # self.searchLabel_nomepessoa_2.setText(_translate("MainWindow", "Nome:"))
        # self.searchLabel_idade_2.setText(_translate("MainWindow", "Idade:"))
        # self.submitButton_pessoa_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_pessoa_3), _translate("MainWindow", "Pessoa"))
        # self.searchLabel_nomepalavra_2.setText(_translate("MainWindow", "Nome:"))
        # self.searchLabel_idioma_2.setText(_translate("MainWindow", "Idioma:"))
        # self.submitButton_palavraschave_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_palavraschave_3), _translate("MainWindow", "Palavras Chave"))
        # self.searchLabel_noticia_2.setText(_translate("MainWindow", "Notícia:"))
        # self.searchLabel_nomefonte_2.setText(_translate("MainWindow", "Nome:"))
        # self.searchLabel_descricaofonte_2.setText(_translate("MainWindow", "Descrição:"))
        # self.submitButton_fonteconfiavel_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_fonteconfiavel_3), _translate("MainWindow", "Fonte Confiável"))
        # self.searchLabel_sigla_2.setText(_translate("MainWindow", "Sigla:"))
        # self.searchLabel_complemento_2.setText(_translate("MainWindow", "Complemento:"))
        # self.searchLabel_nomelocal_2.setText(_translate("MainWindow", "Nome:"))
        # self.submitButton_local_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_local_3), _translate("MainWindow", "Local"))
        # self.searchLabel_emprego_2.setText(_translate("MainWindow", "Emprego:"))
        # self.searchLabel_descricaoocupacao_2.setText(_translate("MainWindow", "Descrição:"))
        # self.submitButton_ocupacao_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_ocupacao_3), _translate("MainWindow", "Ocupação"))
        # self.searchLabel_nomeinfluencia_2.setText(_translate("MainWindow", "Nome:"))
        # self.submitButton_influenciaexterna_2.setText(_translate("MainWindow", "Submit"))
        # self.tabsDeletion.setTabText(self.tabsDeletion.indexOf(self.tab_influenciaexterna_3), _translate("MainWindow", "Influência Externa"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Deletion), _translate("MainWindow", "Deletion"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Update), _translate("MainWindow", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QPSQL")
    db.setDatabaseName("Projeto")
    db.setUserName("admin")
    db.setHostName("localhost")
    db.setPassword("123")
    ok = db.open()

    connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

    conn = psycopg2.connect(connect_str)

    if not ok:
        print(db.lastError().text())
        sys.exit(1)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

