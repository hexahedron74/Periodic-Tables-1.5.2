# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ne.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ne(object):
    def setupUi(self, Ne):
        Ne.setObjectName("Ne")
        Ne.setFixedSize(791, 461)
        Ne.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Ne)
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
        self.label_2.setGeometry(QtCore.QRect(330, 40, 411, 81))
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
        Ne.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ne)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        Ne.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ne)
        self.statusbar.setObjectName("statusbar")
        Ne.setStatusBar(self.statusbar)

        self.retranslateUi(Ne)
        QtCore.QMetaObject.connectSlotsByName(Ne)

    def retranslateUi(self, Ne):
        _translate = QtCore.QCoreApplication.translate
        Ne.setWindowTitle(_translate("Ne", "네온"))
        self.label.setText(_translate("Ne", "Ne"))
        self.label_2.setText(_translate("Ne", "네온"))
        self.label_3.setText(_translate("Ne", "10."))
        self.label_4.setText(_translate("Ne", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호  : 10번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호  : Ne</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름  : Neon</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름  : 네온</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자  수   : 10개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수  : 10개</span></p></body></html>"))
        self.label_5.setText(_translate("Ne", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량     : 20.1797(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도       : 0.0009002(g, Cm^3)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점     : -248.6˚C = -415.48˚F = 24.55K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점     : -246.1˚C = -410.98˚F = 27.05K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 기체</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    F = QtWidgets.QMainWindow()
    ui = Ui_Ne()
    ui.setupUi(F)
    F.show()
    sys.exit(app.exec_())
