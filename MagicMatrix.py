import sys
import sqlite3


from PySide2.QtWidgets import QApplication, QWidget, QFileDialog

from ui.reg_win import Ui_reg_form
from ui.main_win import Ui_main_win
from ui.aut_win import Ui_aut_form

from ui.error1 import Ui_error1
from ui.error2 import Ui_error2

from matrix_gen import result_matrix

__author__ = "Erin Fedor"

# =============================================================================
global db
global sql

db = sqlite3.connect('data.db')
sql = db.cursor()

# Создание таблицы
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT )""")

# =============================================================================



class Aut_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_aut_form()
        self.ui.setupUi(self)
        self.ui.aut_but.clicked.connect(self.aut_data)
        self.ui.aut_but_2.clicked.connect(self.reg_user)

    def reg_user(self):
        self.hide()
        win2.show()

    def aut_data(self):
        user_login = self.ui.lg_edit.text()
        user_password = self.ui.pw_edit.text()
        ok = True
        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if sql.fetchone() is None:
            err1.show()
            return
        elif sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'") != sql.fetchone() is None:
            ok = True
        sql.execute(f"SELECT password FROM users WHERE password = '{user_password}'")
        if sql.fetchone() is None:
            ok =False
        elif sql.execute(f"SELECT password FROM users WHERE password = '{user_password}'") != sql.fetchone() is None:
            ok = True
        if ok == True:
            self.hide()
            win3.show()

class Reg_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_reg_form()
        self.ui.setupUi(self)
        self.ui.reg_but.clicked.connect(self.save_data)

    def save_data(self):
        login = self.ui.lg_edit.text()
        pw1 = self.ui.pw_edit.text()
        pw2 = self.ui.pw_edit_2.text()

        if pw1 == pw2:
            data = (login, pw1)
            sql.executemany("INSERT INTO users(login, password) VALUES(?,?)", (data,))
            self.close()
            win1.show()
            db.commit()
        else:
            err2.show()

class Main_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_main_win()
        self.ui.setupUi(self)
        self.ui.gen_but.clicked.connect(self.gen_mat)
        self.ui.dwld_but.clicked.connect(self.save_pic)

    def save_pic(self):
        grab = self.grab()
        img, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo",
                                             filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            grab.save(img, "png")
        elif img[-3:] == "jpg":
            grab.save(img, "jpg")
        return

    def gen_mat(self):
        N = int(self.ui.n_edit.text())
        result_matrix(N)
        file = open("matrix.txt", "r")
        self.ui.res_edit.setPlainText(file.read())
        file.close()
        return

class Err_Win1(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_error1()
        self.ui.setupUi(self)
class Err_Win2(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_error2()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win1 = Aut_Win()
    # win1 = Main_Win()
    win1.show()
    win2 = Reg_Win()
    win3 = Main_Win()
    err1 = Err_Win1()
    err2 = Err_Win2()
    sys.exit(app.exec_())