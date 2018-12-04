import sys
import psycopg2
import View
from PyQt5 import QtWidgets

def main():
    try:
        connect_str = "dbname='Projeto' user='admin' host='localhost' password='123'"

        conn = psycopg2.connect(connect_str)
        app = QtWidgets.QApplication(sys.argv)
        db = View.QtSql.QSqlDatabase.addDatabase("QPSQL")
        db.setDatabaseName("Projeto")
        db.setUserName("admin")
        db.setHostName("localhost")
        db.setPassword("123")
        ok = db.open()


        if not ok:
            print(db.lastError().text())
            sys.exit(1)

        MainWindow = QtWidgets.QMainWindow()
        ui = View.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        
        conn.commit()
        
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    finally:
        if conn is not None:
            conn.close()
            
if __name__ == "__main__":
    main()
