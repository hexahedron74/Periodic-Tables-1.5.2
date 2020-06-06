# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'He.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os

class Ui_He(object):
    def setupUi(self, He):
        He.setObjectName("He")
        He.setFixedSize(791, 461)
        He.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(He)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 141, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 91, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 181, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 120, 391, 271))
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        He.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(He)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        He.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(He)
        self.statusbar.setObjectName("statusbar")
        He.setStatusBar(self.statusbar)

        self.retranslateUi(He)
        QtCore.QMetaObject.connectSlotsByName(He)

    def retranslateUi(self, He):
        _translate = QtCore.QCoreApplication.translate
        He.setWindowTitle(_translate("He", "헬륨"))
        self.label.setText(_translate("He", "He"))
        self.label_2.setText(_translate("He", "헬륨"))
        self.label_3.setText(_translate("He", "2."))
        self.label_4.setText(_translate("He", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호 : 2번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호 : He</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름 : Helium</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름 : 헬륨</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자 수 : 2개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수 : 2개</span></p></body></html>"))
        self.label_5.setText(_translate("He", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량 : 4.0026(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도 : 0.00017846(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점 : -272.2˚C = -457.96˚F = 0.95K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점 : -268.9˚C = -452.02˚F = 4.25K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 기체</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    He = QtWidgets.QMainWindow()
    ui = Ui_He()
    ui.setupUi(He)
    He.show()
    sys.exit(app.exec_())
