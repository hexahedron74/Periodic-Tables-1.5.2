# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Si.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Si(object):
    def setupUi(self, Si):
        Si.setObjectName("Si")
        Si.setFixedSize(791, 461)
        Si.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Si)
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
        Si.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Si)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        Si.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Si)
        self.statusbar.setObjectName("statusbar")
        Si.setStatusBar(self.statusbar)

        self.retranslateUi(Si)
        QtCore.QMetaObject.connectSlotsByName(Si)

    def retranslateUi(self, Si):
        _translate = QtCore.QCoreApplication.translate
        Si.setWindowTitle(_translate("Si", "규소"))
        self.label_6.setText(_translate("Si", "Si"))
        self.label_2.setText(_translate("Si", "규소"))
        self.label_3.setText(_translate("Si", "14."))
        self.label_4.setText(_translate("Si", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 14번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : Si</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Silicon</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 규소</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 14개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 14개</span></p></body></html>"))
        self.label_5.setText(_translate("Si", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 28.0855(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 2.33(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : 1414.85˚C = 2578.73˚F = 1688.0K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : 2899.8˚C = 5251.64˚F = 3172.95K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Si = QtWidgets.QMainWindow()
    ui = Ui_Si()
    ui.setupUi(Si)
    Si.show()
    sys.exit(app.exec_())
