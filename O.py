# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'O.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_O(object):
    def setupUi(self, O):
        O.setObjectName("O")
        O.setFixedSize(791, 461)
        O.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(O)
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
        O.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(O)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        O.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(O)
        self.statusbar.setObjectName("statusbar")
        O.setStatusBar(self.statusbar)

        self.retranslateUi(O)
        QtCore.QMetaObject.connectSlotsByName(O)

    def retranslateUi(self, O):
        _translate = QtCore.QCoreApplication.translate
        O.setWindowTitle(_translate("O", "산소"))
        self.label.setText(_translate("O", "O"))
        self.label_2.setText(_translate("O", "산소"))
        self.label_3.setText(_translate("O", "8."))
        self.label_4.setText(_translate("O", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 8번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : O</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Oxygen</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 산소</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 8개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 8개</span></p></body></html>"))
        self.label_5.setText(_translate("O", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 15.9994(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 0.00142897(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : -218.4˚C = -361.12˚F = 54.75K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : -182.9˚C = -297.22˚F = 90.25K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 기체</span></p></body></html>"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    O = QtWidgets.QMainWindow()
    ui = Ui_O()
    ui.setupUi(O)
    O.show()
    sys.exit(app.exec_())
