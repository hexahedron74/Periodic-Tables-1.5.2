# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_P(object):
    def setupUi(self, P):
        P.setObjectName("P")
        P.resize(798, 483)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        P.setWindowIcon(icon)
        P.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(P)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 20, 141, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 141, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 231, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 120, 391, 271))
        self.label_5.setObjectName("label_5")
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        P.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(P)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        P.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(P)
        self.statusbar.setObjectName("statusbar")
        P.setStatusBar(self.statusbar)

        self.retranslateUi(P)
        QtCore.QMetaObject.connectSlotsByName(P)

    def retranslateUi(self, P):
        _translate = QtCore.QCoreApplication.translate
        P.setWindowTitle(_translate("P", "인"))
        self.label_6.setText(_translate("P", "P"))
        self.label_2.setText(_translate("P", "인"))
        self.label_3.setText(_translate("P", "15."))
        self.label_4.setText(_translate("P", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 15번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : P</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Phosphorus</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 인</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 15개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 15개</span></p></body></html>"))
        self.label_5.setText(_translate("P", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 30.9737(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 2.82(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : 44.15˚C = 111.47˚F = 317.3K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : 281.85˚C = 539.33˚F = 555.0K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    P = QtWidgets.QMainWindow()
    ui = Ui_P()
    ui.setupUi(P)
    P.show()
    sys.exit(app.exec_())
