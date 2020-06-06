# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_K(object):
    def setupUi(self, K):
        K.setObjectName("K")
        K.resize(798, 483)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        K.setWindowIcon(icon)
        K.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(K)
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
        self.label_4.setGeometry(QtCore.QRect(50, 130, 211, 281))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 120, 391, 271))
        self.label_5.setObjectName("label_5")
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        K.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(K)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        K.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(K)
        self.statusbar.setObjectName("statusbar")
        K.setStatusBar(self.statusbar)

        self.retranslateUi(K)
        QtCore.QMetaObject.connectSlotsByName(K)

    def retranslateUi(self, K):
        _translate = QtCore.QCoreApplication.translate
        K.setWindowTitle(_translate("K", "칼슘"))
        self.label_6.setText(_translate("K", "K"))
        self.label_2.setText(_translate("K", "칼륨"))
        self.label_3.setText(_translate("K", "19."))
        self.label_4.setText(_translate("K", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 19번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Potassium</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 칼륨</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 19개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 19개</span></p></body></html>"))
        self.label_5.setText(_translate("K", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 40.078(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 1.55(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : 838.85˚C = 1541.93˚F = 1112.0K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : 1483.85˚C = 2702.93˚F = 1757.0K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 고체</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    K = QtWidgets.QMainWindow()
    ui = Ui_K()
    ui.setupUi(K)
    K.show()
    sys.exit(app.exec_())
