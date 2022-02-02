# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_reg_form(object):
    def setupUi(self, reg_form):
        if not reg_form.objectName():
            reg_form.setObjectName(u"reg_form")
        reg_form.resize(260, 150)
        reg_form.setMaximumSize(QSize(260, 150))
        self.gridLayout = QGridLayout(reg_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_1 = QLabel(reg_form)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 3)

        self.label_2 = QLabel(reg_form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lg_edit = QLineEdit(reg_form)
        self.lg_edit.setObjectName(u"lg_edit")

        self.verticalLayout.addWidget(self.lg_edit)

        self.pw_edit = QLineEdit(reg_form)
        self.pw_edit.setObjectName(u"pw_edit")

        self.verticalLayout.addWidget(self.pw_edit)

        self.pw_edit_2 = QLineEdit(reg_form)
        self.pw_edit_2.setObjectName(u"pw_edit_2")

        self.verticalLayout.addWidget(self.pw_edit_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 3, 1)

        self.label_3 = QLabel(reg_form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(reg_form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)

        self.reg_but = QPushButton(reg_form)
        self.reg_but.setObjectName(u"reg_but")

        self.gridLayout.addWidget(self.reg_but, 4, 1, 1, 2)


        self.retranslateUi(reg_form)

        QMetaObject.connectSlotsByName(reg_form)
    # setupUi

    def retranslateUi(self, reg_form):
        reg_form.setWindowTitle(QCoreApplication.translate("reg_form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_1.setText(QCoreApplication.translate("reg_form", u"\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041b\u041e\u0413\u0418\u041d \u0418 \u041f\u0410\u0420\u041e\u041b\u042c \u0414\u041b\u042f \u0420\u0415\u0413\u0418\u0421\u0422\u0420\u0410\u0426\u0418\u0418:", None))
        self.label_2.setText(QCoreApplication.translate("reg_form", u"\u041b\u041e\u0413\u0418\u041d:", None))
        self.label_3.setText(QCoreApplication.translate("reg_form", u"\u041f\u0410\u0420\u041e\u041b\u042c:", None))
        self.label_4.setText(QCoreApplication.translate("reg_form", u"\u041f\u0410\u0420\u041e\u041b\u042c \u0415\u0429\u0415 \u0420\u0410\u0417:", None))
        self.reg_but.setText(QCoreApplication.translate("reg_form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

