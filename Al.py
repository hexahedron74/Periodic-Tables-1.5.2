# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Al.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Al(object):
    def setupUi(self, Al):
        Al.setObjectName("Al")
        Al.resize(799, 481)
        Al.setMouseTracking(False)
        Al.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Al)
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
        self.label_2.setGeometry(QtCore.QRect(330, 30, 411, 81))
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
        Al.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Al)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        Al.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Al)
        self.statusbar.setObjectName("statusbar")
        Al.setStatusBar(self.statusbar)

        self.retranslateUi(Al)
        QtCore.QMetaObject.connectSlotsByName(Al)

    def retranslateUi(self, Al):
        _translate = QtCore.QCoreApplication.translate
        Al.setWindowTitle(_translate("Al", "알루미늄"))
        self.label.setText(_translate("Al", "Al"))
        self.label_2.setText(_translate("Al", "알루미늄"))
        self.label_3.setText(_translate("Al", "13."))
        self.label_4.setText(_translate("Al", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 13번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : Al</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Aluminium</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 알루미늄</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 13개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 13개</span></p></body></html>"))
        self.label_5.setText(_translate("Al", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 26.9815(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 2.6989(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : 660.0˚C = 1220.0˚F = 933.15K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : 2518.82˚C = 4568.88˚F = 2791.97K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Al = QtWidgets.QMainWindow()
    ui = Ui_Al()
    ui.setupUi(Al)
    Al.show()
    sys.exit(app.exec_())
