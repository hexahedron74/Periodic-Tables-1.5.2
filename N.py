# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'N.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_N(object):
    def setupUi(self, N):
        N.setObjectName("N")
        N.setFixedSize(791, 461)
        N.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(N)
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
        self.label_2.setGeometry(QtCore.QRect(250, 40, 321, 81))
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
        self.label_4.setGeometry(QtCore.QRect(50, 130, 211, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 120, 411, 271))
        self.label_5.setObjectName("label_5")
        N.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(N)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        N.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(N)
        self.statusbar.setObjectName("statusbar")
        N.setStatusBar(self.statusbar)

        self.retranslateUi(N)
        QtCore.QMetaObject.connectSlotsByName(N)

    def retranslateUi(self, N):
        _translate = QtCore.QCoreApplication.translate
        N.setWindowTitle(_translate("N", "질소"))
        self.label.setText(_translate("N", "N"))
        self.label_2.setText(_translate("N", "질소"))
        self.label_3.setText(_translate("N", "7."))
        self.label_4.setText(_translate("N", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 7번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : N</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Nitrogen</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 질소</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 7개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 7개</span></p></body></html>"))
        self.label_5.setText(_translate("N", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 14.0067(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 0.001251(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : -209.9˚C = -345.82˚F = 63.25K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : -195.8˚C = -320.44˚F = 77.35K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 기체</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    N = QtWidgets.QMainWindow()
    ui = Ui_N()
    ui.setupUi(N)
    N.show()
    sys.exit(app.exec_())
