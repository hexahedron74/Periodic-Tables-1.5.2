# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ar.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ar(object):
    def setupUi(self, Ar):
        Ar.setObjectName("Ar")
        Ar.setFixedSize(791, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        Ar.setWindowIcon(icon)
        Ar.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Ar)
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
        self.label_2.setGeometry(QtCore.QRect(370, 20, 301, 101))
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
        Ar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        Ar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ar)
        self.statusbar.setObjectName("statusbar")
        Ar.setStatusBar(self.statusbar)

        self.retranslateUi(Ar)
        QtCore.QMetaObject.connectSlotsByName(Ar)

    def retranslateUi(self, Ar):
        _translate = QtCore.QCoreApplication.translate
        Ar.setWindowTitle(_translate("Ar", "아르곤"))
        self.label_6.setText(_translate("Ar", "Ar"))
        self.label_2.setText(_translate("Ar", "아르곤"))
        self.label_3.setText(_translate("Ar", "18."))
        self.label_4.setText(_translate("Ar", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 18번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : Ar</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Argon</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 아르곤</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 18개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 18개</span></p></body></html>"))
        self.label_5.setText(_translate("Ar", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 39.948(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 0.001784(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : -189.35˚C = -308.83˚F = 83.8K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : -185.85˚C = -302.53˚F = 87.3K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 기체</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ar = QtWidgets.QMainWindow()
    ui = Ui_Ar()
    ui.setupUi(Ar)
    Ar.show()
    sys.exit(app.exec_())
