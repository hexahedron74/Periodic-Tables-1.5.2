# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_F(object):
    def setupUi(self, F):
        F.setObjectName("F")
        F.setFixedSize(791, 461)
        F.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(F)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 411, 81))
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
        self.label_4.setGeometry(QtCore.QRect(50, 130, 241, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 120, 411, 271))
        self.label_5.setObjectName("label_5")
        F.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(F)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        F.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(F)
        self.statusbar.setObjectName("statusbar")
        F.setStatusBar(self.statusbar)

        self.retranslateUi(F)
        QtCore.QMetaObject.connectSlotsByName(F)

    def retranslateUi(self, F):
        _translate = QtCore.QCoreApplication.translate
        F.setWindowTitle(_translate("F", "플루오린"))
        self.label.setText(_translate("F", "F"))
        self.label_2.setText(_translate("F", "플루오린"))
        self.label_3.setText(_translate("F", "9."))
        self.label_4.setText(_translate("F", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 9번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : F</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Fluorine</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 플루오린</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 9개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 9개</span></p></body></html>"))
        self.label_5.setText(_translate("F", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 18.9984(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 0.001696(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : -219.7˚C = -363.46˚F = 53.45K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : -188.1˚C = -306.58˚F = 85.05K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 기체</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    F = QtWidgets.QMainWindow()
    ui = Ui_F()
    ui.setupUi(F)
    F.show()
    sys.exit(app.exec_())
