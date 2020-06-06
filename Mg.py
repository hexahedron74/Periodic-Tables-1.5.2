# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mg.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mg(object):
    def setupUi(self, Mg):
        Mg.setObjectName("Mg")
        Mg.setFixedSize(791, 461)
        Mg.setMouseTracking(False)
        Mg.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Mg)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 50, 411, 81))
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
        self.label_4.setGeometry(QtCore.QRect(50, 130, 241, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 120, 411, 271))
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        Mg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        Mg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mg)
        self.statusbar.setObjectName("statusbar")
        Mg.setStatusBar(self.statusbar)

        self.retranslateUi(Mg)
        QtCore.QMetaObject.connectSlotsByName(Mg)

    def retranslateUi(self, Mg):
        _translate = QtCore.QCoreApplication.translate
        Mg.setWindowTitle(_translate("Mg", "마그네슘"))
        self.label.setText(_translate("Mg", "Mg"))
        self.label_2.setText(_translate("Mg", "마그네슘"))
        self.label_3.setText(_translate("Mg", "12."))
        self.label_4.setText(_translate("Mg", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 12번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : Mg</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Magnesium</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 마그네슘</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 12개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 12개</span></p></body></html>"))
        self.label_5.setText(_translate("Mg", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 24.3050(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 1.738(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : 650.0˚C = 1202.0˚F = 923.15K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : 1090.0˚C = 1994.0˚F = 1363.15K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mg = QtWidgets.QMainWindow()
    ui = Ui_Mg()
    ui.setupUi(Mg)
    Mg.show()
    sys.exit(app.exec_())
