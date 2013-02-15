# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service.ui'
#
# Created by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(471, 265)
        self.ciLineEdit = QtGui.QLineEdit(Form)
        self.ciLineEdit.setGeometry(QtCore.QRect(10, 20, 113, 31))
        self.ciLineEdit.setObjectName(_fromUtf8("ciLineEdit"))
        self.monitorLineEdit = QtGui.QLineEdit(Form)
        self.monitorLineEdit.setGeometry(QtCore.QRect(10, 60, 113, 31))
        self.monitorLineEdit.setObjectName(_fromUtf8("monitorLineEdit"))
        self.bolLineEdit = QtGui.QLineEdit(Form)
        self.bolLineEdit.setGeometry(QtCore.QRect(10, 100, 113, 31))
        self.bolLineEdit.setObjectName(_fromUtf8("bolLineEdit"))
        self.ciLabel = QtGui.QLabel(Form)
        self.ciLabel.setGeometry(QtCore.QRect(130, 30, 57, 14))
        self.ciLabel.setObjectName(_fromUtf8("ciLabel"))
        self.monitorLabel = QtGui.QLabel(Form)
        self.monitorLabel.setGeometry(QtCore.QRect(130, 64, 281, 20))
        self.monitorLabel.setObjectName(_fromUtf8("monitorLabel"))
        self.bolLabel = QtGui.QLabel(Form)
        self.bolLabel.setGeometry(QtCore.QRect(130, 110, 131, 16))
        self.bolLabel.setObjectName(_fromUtf8("bolLabel"))
        self.ipLineEdit = QtGui.QLineEdit(Form)
        self.ipLineEdit.setGeometry(QtCore.QRect(10, 140, 113, 31))
        self.ipLineEdit.setObjectName(_fromUtf8("ipLineEdit"))
        self.ipLabel = QtGui.QLabel(Form)
        self.ipLabel.setGeometry(QtCore.QRect(130, 150, 131, 16))
        self.ipLabel.setObjectName(_fromUtf8("ipLabel"))
        self.createButton = QtGui.QPushButton(Form)
        self.createButton.setGeometry(QtCore.QRect(10, 220, 79, 31))
        self.createButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ciLabel.setText(QtGui.QApplication.translate("Form", "CI Name", None, QtGui.QApplication.UnicodeUTF8))
        self.monitorLabel.setText(QtGui.QApplication.translate("Form", "Monitor CI = MONITORED / NOT_MONITORED", None, QtGui.QApplication.UnicodeUTF8))
        self.bolLabel.setText(QtGui.QApplication.translate("Form", "useIP=True / False", None, QtGui.QApplication.UnicodeUTF8))
        self.ipLabel.setText(QtGui.QApplication.translate("Form", "IP Address", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("Form", "Create", None, QtGui.QApplication.UnicodeUTF8))

