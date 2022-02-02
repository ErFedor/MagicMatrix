import sys
import sqlite3

from PySide2.QtWidgets import QApplication, QWidget, QFileDialog

from ui.reg_win import Ui_reg_form
from ui.main_win import Ui_main_win
from ui.aut_win import Ui_aut_form

from matrix_gen import result_matrix
# file = open("matrix.txt", "r")

__author__ = "Erin Fedor"
# =============================================================================
conn = sqlite3.connect("log_pas.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS log_pas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL,
                password TEXT NOT NULL)""")

# cursor.execute('SELECT login FROM log_pas WHERE login = ?')
# =============================================================================
# class MainWindow(QWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('MainWindow')
#
#     def show_window_1(self):
#         self.w1 = Reg_Win()
#         self.w1.button.clicked.connect(self.show_window_2)
#         self.w1.button.clicked.connect(self.w1.close)
#         self.w1.show()
#
#     def show_window_2(self):
#         self.w2 = Window2()
#         self.w2.show()



class Reg_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.reg_but.clicked.connect(self.save_data)

    def save_data(self):
        login = self.ui.lg_edit.text()
        password = self.ui.pw_edit.text()
        data = (login, password)
        cursor.executemany("INSERT INTO log_pas(login, password) VALUES(?,?)", (data,))
        self.close()
        win2.mainloop()
        # msg = QWidget()
        # but = ('Hello', msg)
        # msg.show()
        # sys.exit(app.exec_())



class Main_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_main_win()
        self.ui.setupUi(self)
        self.ui.gen_but.clicked.connect(self.gen_mat)
        self.ui.dwld_but.clicked.connect(self.save_pic)


    def save_pic(self):
        # image = QImage(self.webView.mainFrame.contentsSize(), QImage.Format_ARGB32)
        # painter = QPainter(image)
        # self.webView.mainFrame.render(painter)
        # painter.end()

        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        img, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo",
                                             filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            self.preview_screen.save(img, "png")
        elif img[-3:] == "jpg":
            self.preview_screen.save(img, "jpg")
        return

    def gen_mat(self):
        N = int(self.ui.n_edit.text())
        result_matrix(N)
        file = open("matrix.txt", "r")
        self.ui.res_edit.setPlainText(file.read())
        file.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # win1 = Reg_Win()
    # win1.show()
    win2 = Main_Win()
    win2.show()
    sys.exit(app.exec_())

    