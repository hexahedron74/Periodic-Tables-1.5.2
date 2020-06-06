# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'B.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_B(object):
    def setupUi(self, B):
        B.setObjectName("B")
        B.setFixedSize(791, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        B.setWindowIcon(icon)
        B.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(B)
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
        self.label_4.setGeometry(QtCore.QRect(50, 130, 181, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 120, 411, 271))
        self.label_5.setObjectName("label_5")
        B.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(B)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        B.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(B)
        self.statusbar.setObjectName("statusbar")
        B.setStatusBar(self.statusbar)

        self.retranslateUi(B)
        QtCore.QMetaObject.connectSlotsByName(B)

    def retranslateUi(self, B):
        _translate = QtCore.QCoreApplication.translate
        B.setWindowTitle(_translate("B", "붕소"))
        self.label.setText(_translate("B", "B"))
        self.label_2.setText(_translate("B", "붕소"))
        self.label_3.setText(_translate("B", "5."))
        self.label_4.setText(_translate("B", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 5번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : B</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Boron</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 붕소</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 5개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 5개</span></p></body></html>"))
        self.label_5.setText(_translate("B", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량 : 10.811(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도 : 2.34(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점 : 2075.8˚C = 3768.44˚F = 2348.95K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점 : 3926.8˚C = 7100.24˚F = 4199.95K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    B = QtWidgets.QMainWindow()
    ui = Ui_B()
    ui.setupUi(B)
    B.show()
    sys.exit(app.exec_())
