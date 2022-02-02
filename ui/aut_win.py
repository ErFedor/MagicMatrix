# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aut_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_aut_form(object):
    def setupUi(self, aut_form):
        if not aut_form.objectName():
            aut_form.setObjectName(u"aut_form")
        aut_form.resize(260, 122)
        aut_form.setMaximumSize(QSize(260, 122))
        self.gridLayout = QGridLayout(aut_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_1 = QLabel(aut_form)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 3)

        self.label_2 = QLabel(aut_form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lg_edit = QLineEdit(aut_form)
        self.lg_edit.setObjectName(u"lg_edit")

        self.verticalLayout.addWidget(self.lg_edit)

        self.pw_edit = QLineEdit(aut_form)
        self.pw_edit.setObjectName(u"pw_edit")

        self.verticalLayout.addWidget(self.pw_edit)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 2)

        self.label_3 = QLabel(aut_form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.aut_but = QPushButton(aut_form)
        self.aut_but.setObjectName(u"aut_but")

        self.gridLayout.addWidget(self.aut_but, 3, 1, 1, 1)

        self.aut_but_2 = QPushButton(aut_form)
        self.aut_but_2.setObjectName(u"aut_but_2")

        self.gridLayout.addWidget(self.aut_but_2, 3, 2, 1, 1)


        self.retranslateUi(aut_form)

        QMetaObject.connectSlotsByName(aut_form)
    # setupUi

    def retranslateUi(self, aut_form):
        aut_form.setWindowTitle(QCoreApplication.translate("aut_form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_1.setText(QCoreApplication.translate("aut_form", u"\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041b\u041e\u0413\u0418\u041d \u0418 \u041f\u0410\u0420\u041e\u041b\u042c \u0414\u041b\u042f \u0420\u0415\u0413\u0418\u0421\u0422\u0420\u0410\u0426\u0418\u0418:", None))
        self.label_2.setText(QCoreApplication.translate("aut_form", u"\u041b\u041e\u0413\u0418\u041d:", None))
        self.label_3.setText(QCoreApplication.translate("aut_form", u"\u041f\u0410\u0420\u041e\u041b\u042c:", None))
        self.aut_but.setText(QCoreApplication.translate("aut_form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.aut_but_2.setText(QCoreApplication.translate("aut_form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

