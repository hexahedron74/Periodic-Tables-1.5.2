# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Be.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Be(object):
    def setupUi(self, Be):
        Be.setObjectName("Be")
        Be.setFixedSize(791, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        Be.setWindowIcon(icon)
        Be.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Be)
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
        self.label_2.setGeometry(QtCore.QRect(310, 40, 321, 81))
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
        self.label_4.setGeometry(QtCore.QRect(50, 130, 231, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 120, 421, 271))
        self.label_5.setObjectName("label_5")
        Be.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Be)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        Be.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Be)
        self.statusbar.setObjectName("statusbar")
        Be.setStatusBar(self.statusbar)

        self.retranslateUi(Be)
        QtCore.QMetaObject.connectSlotsByName(Be)

    def retranslateUi(self, Be):
        _translate = QtCore.QCoreApplication.translate
        Be.setWindowTitle(_translate("Be", "베릴륨"))
        self.label.setText(_translate("Be", "Be"))
        self.label_2.setText(_translate("Be", "베릴륨"))
        self.label_3.setText(_translate("Be", "4."))
        self.label_4.setText(_translate("Be", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 4번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : Be</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Beryllium</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 베릴륨</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 4개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 4개</span></p></body></html>"))
        self.label_5.setText(_translate("Be", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량 : 9.0121(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도 : 1.848(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점 : 1278.0˚C = 2332.4˚F = 1551.15K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점 : 2970.0˚C = 5378.0˚F = 3243.15K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Be = QtWidgets.QMainWindow()
    ui = Ui_Be()
    ui.setupUi(Be)
    Be.show()
    sys.exit(app.exec_())
