# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 487)
        self.pre_Button = QtWidgets.QPushButton(Form)
        self.pre_Button.setGeometry(QtCore.QRect(40, 450, 75, 23))
        self.pre_Button.setObjectName("pre_Button")
        self.next_Button = QtWidgets.QPushButton(Form)
        self.next_Button.setGeometry(QtCore.QRect(280, 450, 75, 23))
        self.next_Button.setObjectName("next_Button")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(-5, 31, 401, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.favorite = QtWidgets.QPushButton(Form)
        self.favorite.setGeometry(QtCore.QRect(160, 450, 75, 23))
        self.favorite.setObjectName("favorite")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户界面"))
        self.pre_Button.setText(_translate("Form", "上一页"))
        self.next_Button.setText(_translate("Form", "下一页"))
        self.favorite.setText(_translate("Form", "收藏"))
