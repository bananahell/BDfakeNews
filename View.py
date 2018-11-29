# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import Controller
from PyQt5.QtCore import Qt

table_columns_tabs = {0: "categorianoticia",
                      1: "noticia"}

table_columns_view = {0: ("ID", "Nome", "Descrição"),
                 1: ("ID", "Manchete", "Descrição", "Consequência", "Popularidade", "Data", "Piada", "InfluenciaId")}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.modesTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.modesTabs.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.modesTabs.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.modesTabs.setTabPosition(QtWidgets.QTabWidget.West)
        self.modesTabs.setObjectName("modesTabs")

        self.Selection = QtWidgets.QWidget()
        self.Selection.setObjectName("Selection")
        self.tabsSelection = QtWidgets.QTabWidget(self.Selection)
        self.tabsSelection.setGeometry(QtCore.QRect(10, 130, 761, 421))
        self.tabsSelection.setObjectName("tabsSelection")

        self.tab_categorianoticia = QtWidgets.QWidget()
        self.tab_categorianoticia.setEnabled(True)
        self.tab_categorianoticia.setObjectName("tab_categorianoticia")

        self.tab_categorianoticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.tab_categorianoticia.model.setTable("categorianoticia")
        self.tab_categorianoticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.tab_categorianoticia.model.select()
        self.tab_categorianoticia.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.tab_categorianoticia.model.setHeaderData(
            1, Qt.Horizontal, "Nome")
        self.tab_categorianoticia.model.setHeaderData(
            2, Qt.Horizontal, "Descrição")

        self.table_categorianoticia = QtWidgets.QTableView(self.tab_categorianoticia)
        self.table_categorianoticia.setGeometry(QtCore.QRect(0, 0, 751, 381))
        self.table_categorianoticia.setObjectName("table_categorianoticia")
        self.table_categorianoticia.setModel(self.tab_categorianoticia.model)

        self.tabsSelection.addTab(self.tab_categorianoticia, "")

        self.tab_noticia = QtWidgets.QWidget()
        self.tab_noticia.setObjectName("tab_noticia")

        self.tab_noticia.model = QtSql.QSqlTableModel(
            db=QtSql.QSqlDatabase.database())
        self.tab_noticia.model.setTable("noticia")
        self.tab_noticia.model.setEditStrategy(
            QtSql.QSqlTableModel.OnManualSubmit)
        self.tab_noticia.model.select()
        self.tab_noticia.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.tab_noticia.model.setHeaderData(1, Qt.Horizontal, "Manchete")
        self.tab_noticia.model.setHeaderData(2, Qt.Horizontal, "Descrição")
        self.tab_noticia.model.setHeaderData(3, Qt.Horizontal, "Consequência")
        self.tab_noticia.model.setHeaderData(4, Qt.Horizontal, "Popularidade")
        self.tab_noticia.model.setHeaderData(5, Qt.Horizontal, "Data")
        self.tab_noticia.model.setHeaderData(6, Qt.Horizontal, "Piada")
        self.tab_noticia.model.setHeaderData(7, Qt.Horizontal, "InfluenciaId")


        self.table_noticia = QtWidgets.QTableView(self.tab_noticia)
        self.table_noticia.setGeometry(QtCore.QRect(0, 0, 751, 381))
        self.table_noticia.setObjectName("table_noticia")
        self.table_noticia.setModel(self.tab_noticia.model)
        self.table_noticia.resizeRowsToContents()

        self.tabsSelection.addTab(self.tab_noticia, "")

        self.refreshButton = QtWidgets.QPushButton(self.Selection)
        self.refreshButton.setGeometry(QtCore.QRect(480, 80, 101, 29))
        self.refreshButton.setObjectName("refreshButton")

        self.searchButton = QtWidgets.QPushButton(self.Selection)
        self.searchButton.setGeometry(QtCore.QRect(370, 80, 101, 29))
        self.searchButton.setObjectName("searchButton")

        self.searchField = QtWidgets.QLineEdit(self.Selection)
        self.searchField.setGeometry(QtCore.QRect(10, 40, 571, 29))
        self.searchField.setObjectName("searchField")

        self.searchLabel = QtWidgets.QLabel(self.Selection)
        self.searchLabel.setGeometry(QtCore.QRect(10, 20, 391, 17))
        self.searchLabel.setObjectName("searchLabel")
        
        self.modesTabs.addTab(self.Selection, "")
        self.Insertion = QtWidgets.QWidget()
        self.Insertion.setObjectName("Insertion")
        self.tabsInsertion = QtWidgets.QTabWidget(self.Insertion)
        self.tabsInsertion.setGeometry(QtCore.QRect(10, 50, 761, 421))
        self.tabsInsertion.setObjectName("tabsInsertion")

        self.tab_categorianoticia_insertion = QtWidgets.QWidget()
        self.tab_categorianoticia_insertion.setEnabled(True)
        self.tab_categorianoticia_insertion.setObjectName(
            "tab_categorianoticia_insertion")

        self.table_noticia_3 = QtWidgets.QTableView(self.tab_categorianoticia_insertion)
        self.table_noticia_3.setGeometry(QtCore.QRect(0, 0, 751, 381))
        self.table_noticia_3.setObjectName("table_noticia_3")


        self.SubmitButtoncategorianoticia = QtWidgets.QPushButton(self.tab_categorianoticia_insertion)
        self.SubmitButtoncategorianoticia.setGeometry(QtCore.QRect(20, 340, 101, 29))
        self.SubmitButtoncategorianoticia.setObjectName("SubmitButtoncategorianoticia")

        self.searchLabel_IDEmployee = QtWidgets.QLabel(self.tab_categorianoticia_insertion)
        self.searchLabel_IDEmployee.setGeometry(QtCore.QRect(10, 10, 31, 20))
        self.searchLabel_IDEmployee.setObjectName("searchLabel_IDEmployee")
        self.searchField_IDEmployee = QtWidgets.QLineEdit(
            self.tab_categorianoticia_insertion)
        self.searchField_IDEmployee.setGeometry(QtCore.QRect(40, 10, 191, 29))
        self.searchField_IDEmployee.setObjectName("searchField_IDEmployee")

        self.searchField_FnameEmployee = QtWidgets.QLineEdit(
            self.tab_categorianoticia_insertion)
        self.searchField_FnameEmployee.setGeometry(QtCore.QRect(70, 60, 231, 29))
        self.searchField_FnameEmployee.setObjectName("searchField_FnameEmployee")
        self.searchLabel_FnameEmployee = QtWidgets.QLabel(
            self.tab_categorianoticia_insertion)
        self.searchLabel_FnameEmployee.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.searchLabel_FnameEmployee.setObjectName("searchLabel_FnameEmployee")
        self.searchField_LnameEmployee = QtWidgets.QLineEdit(
            self.tab_categorianoticia_insertion)
        self.searchField_LnameEmployee.setGeometry(QtCore.QRect(70, 120, 231, 29))
        self.searchField_LnameEmployee.setObjectName("searchField_LnameEmployee")
        self.searchLabel_5 = QtWidgets.QLabel(self.tab_categorianoticia_insertion)
        self.searchLabel_5.setGeometry(QtCore.QRect(10, 120, 61, 20))
        self.searchLabel_5.setObjectName("searchLabel_5")
        self.tabsInsertion.addTab(self.tab_categorianoticia_insertion, "")
        self.tab_noticia_insertion = QtWidgets.QWidget()
        self.tab_noticia_insertion.setObjectName("tab_noticia_insertion")
        self.table_noticia_insertion = QtWidgets.QTableView(
            self.tab_noticia_insertion)
        self.table_noticia_insertion.setGeometry(QtCore.QRect(0, 0, 751, 381))
        self.table_noticia_insertion.setObjectName("table_noticia_insertion")
        self.searchField_NameClients = QtWidgets.QLineEdit(
            self.tab_noticia_insertion)
        self.searchField_NameClients.setGeometry(QtCore.QRect(70, 60, 231, 29))
        self.searchField_NameClients.setObjectName("searchField_NameClients")
        self.searchLabel_NameClients = QtWidgets.QLabel(
            self.tab_noticia_insertion)
        self.searchLabel_NameClients.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.searchLabel_NameClients.setObjectName("searchLabel_NameClients")
        self.SubmitButton_Clients = QtWidgets.QPushButton(self.tab_noticia_insertion)
        self.SubmitButton_Clients.setGeometry(QtCore.QRect(20, 340, 101, 29))
        self.SubmitButton_Clients.setObjectName("SubmitButton_Clients")
        self.searchField_IDClients = QtWidgets.QLineEdit(
            self.tab_noticia_insertion)
        self.searchField_IDClients.setGeometry(QtCore.QRect(40, 10, 191, 29))
        self.searchField_IDClients.setObjectName("searchField_IDClients")
        self.searchLabel_IDClients = QtWidgets.QLabel(self.tab_noticia_insertion)
        self.searchLabel_IDClients.setGeometry(QtCore.QRect(10, 10, 31, 20))
        self.searchLabel_IDClients.setObjectName("searchLabel_IDClients")
        self.tabsInsertion.addTab(self.tab_noticia_insertion, "")
        self.instruction = QtWidgets.QLabel(self.Insertion)
        self.instruction.setGeometry(QtCore.QRect(10, 20, 591, 17))
        self.instruction.setObjectName("instruction")
        self.modesTabs.addTab(self.Insertion, "")
        self.Deletion = QtWidgets.QWidget()
        self.Deletion.setObjectName("Deletion")
        self.modesTabs.addTab(self.Deletion, "")
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.modesTabs.addTab(self.Update, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.modesTabs.setCurrentIndex(1)
        self.tabsSelection.setCurrentIndex(1)
        self.tabsInsertion.setCurrentIndex(0)
        self.searchButton.clicked.connect(self.clicksearch)
        self.refreshButton.clicked.connect(self.clickrefresh)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicksearch(self):
        searchText = self.searchField.text()
        Controller.CheckField(searchText)
        self.statusbar.showMessage("Carregando...")

        model = Controller.ControllerButton(table_columns_tabs[self.tabsSelection.currentIndex()], searchText)
        columns = table_columns_view[self.tabsSelection.currentIndex()]

        for i in range(0, len(columns)):
            model.setHeaderData(i, Qt.Horizontal, columns[i])

        whichtable = table_columns_tabs[self.tabsSelection.currentIndex()]
        if whichtable is "categorianoticia":
            self.table_categorianoticia.setModel(model)
        elif whichtable is "noticia":
            self.table_noticia.setModel(model)

        self.statusbar.showMessage("Ready")

    def clickrefresh(self):
        self.statusbar.showMessage("Carregando...")
        whichtable = table_columns_tabs[self.tabsSelection.currentIndex()]
        if whichtable is "categorianoticia":
            self.table_categorianoticia.setModel(self.tab_categorianoticia.model)
        elif whichtable is "noticia":
            self.table_noticia.setModel(self.tab_noticia.model)

        self.statusbar.showMessage("Ready")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(self.tab_categorianoticia), _translate("MainWindow", "Categoria da Notícia"))
        self.tabsSelection.setTabText(self.tabsSelection.indexOf(self.tab_noticia), _translate("MainWindow", "Notícia"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.searchLabel.setText(_translate("MainWindow", "Digite sua busca por coluna de acordo com a tabela atual"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Selection), _translate("MainWindow", "Selection"))
        self.SubmitButtoncategorianoticia.setText(
            _translate("MainWindow", "Submit"))
        self.searchLabel_IDEmployee.setText(_translate("MainWindow", "ID*:"))
        self.searchLabel_FnameEmployee.setText(_translate("MainWindow", "Fname*:"))
        self.searchLabel_5.setText(_translate("MainWindow", "Lname*:"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(self.tab_categorianoticia_insertion), _translate("MainWindow", "Categoria da Notícia"))
        self.searchLabel_NameClients.setText(_translate("MainWindow", "Name*:"))
        self.SubmitButton_Clients.setText(_translate("MainWindow", "Submit"))
        self.searchLabel_IDClients.setText(_translate("MainWindow", "ID*:"))
        self.tabsInsertion.setTabText(self.tabsInsertion.indexOf(self.tab_noticia_insertion), _translate("MainWindow", "Notícia"))
        self.instruction.setText(_translate("MainWindow", "Insira de acordo com a tabela atual. Campos com (*) são de preenchimento obrigatório"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Insertion), _translate("MainWindow", "Insertion"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Deletion), _translate("MainWindow", "Deletion"))
        self.modesTabs.setTabText(self.modesTabs.indexOf(self.Update), _translate("MainWindow", "Update"))


