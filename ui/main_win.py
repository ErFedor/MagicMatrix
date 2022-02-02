# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_win(object):
    def setupUi(self, main_win):
        if not main_win.objectName():
            main_win.setObjectName(u"main_win")
        main_win.resize(317, 407)
        main_win.setMaximumSize(QSize(317, 407))
        self.gridLayout = QGridLayout(main_win)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label4 = QLabel(main_win)
        self.label4.setObjectName(u"label4")

        self.horizontalLayout.addWidget(self.label4)

        self.n_edit = QLineEdit(main_win)
        self.n_edit.setObjectName(u"n_edit")

        self.horizontalLayout.addWidget(self.n_edit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 2, 2)

        self.res_edit = QTextEdit(main_win)
        self.res_edit.setObjectName(u"res_edit")

        self.gridLayout.addWidget(self.res_edit, 3, 0, 1, 2)

        self.dwld_but = QPushButton(main_win)
        self.dwld_but.setObjectName(u"dwld_but")

        self.gridLayout.addWidget(self.dwld_but, 4, 0, 1, 2)

        self.gen_but = QPushButton(main_win)
        self.gen_but.setObjectName(u"gen_but")

        self.gridLayout.addWidget(self.gen_but, 2, 0, 1, 1)


        self.retranslateUi(main_win)

        QMetaObject.connectSlotsByName(main_win)
    # setupUi

    def retranslateUi(self, main_win):
        main_win.setWindowTitle(QCoreApplication.translate("main_win", u"MagicMatrix", None))
        self.label4.setText(QCoreApplication.translate("main_win", u"\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u0420\u0410\u0417\u041c\u0415\u0420 \u041c\u0410\u0413\u0418\u0427\u0415\u0421\u041a\u041e\u0413\u041e \u041a\u0412\u0410\u0414\u0420\u0410\u0422\u0410:", None))
        self.dwld_but.setText(QCoreApplication.translate("main_win", u"\u0421\u041a\u0410\u0427\u0410\u0422\u042c", None))
        self.gen_but.setText(QCoreApplication.translate("main_win", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

