# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Li.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os

class Ui_Li(object):
    def setupUi(self, Li):
        Li.setObjectName("Li")
        Li.setFixedSize(791, 461)
        Li.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Li)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 20, 141, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
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
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        Li.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Li)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        Li.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Li)
        self.statusbar.setObjectName("statusbar")
        Li.setStatusBar(self.statusbar)

        self.retranslateUi(Li)
        QtCore.QMetaObject.connectSlotsByName(Li)

    def retranslateUi(self, Li):
        _translate = QtCore.QCoreApplication.translate
        Li.setWindowTitle(_translate("Li", "리튬"))
        self.label_6.setText(_translate("Li", "Li"))
        self.label_2.setText(_translate("Li", "리튬"))
        self.label_3.setText(_translate("Li", "3."))
        self.label_4.setText(_translate("Li", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 3번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : Li</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Lithium</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 리튬</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 3개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 3개</span></p></body></html>"))
        self.label_5.setText(_translate("Li", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 6.941(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 0.534(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : 180.5˚C = 356.9˚F = 453.65K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : 1342.0˚C = 2447.6˚F = 1615.15K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Li = QtWidgets.QMainWindow()
    ui = Ui_Li()
    ui.setupUi(Li)
    Li.show()
    sys.exit(app.exec_())
