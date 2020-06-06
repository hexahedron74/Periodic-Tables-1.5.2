from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_H(object):
    def setupUi(self, H):
        H.setObjectName("H")
        H.setFixedSize(791, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        H.setWindowIcon(icon)
        H.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(H)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 61, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 211, 71))
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
        self.label_5.setGeometry(QtCore.QRect(300, 120, 401, 271))
        self.label_5.setObjectName("label_5")
        H.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(H)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        H.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(H)
        self.statusbar.setObjectName("statusbar")
        H.setStatusBar(self.statusbar)

        self.retranslateUi(H)
        QtCore.QMetaObject.connectSlotsByName(H)

    def retranslateUi(self, H):
        _translate = QtCore.QCoreApplication.translate
        H.setWindowTitle(_translate("H", "수소"))
        self.label.setText(_translate("H", "H"))
        self.label_2.setText(_translate("H", "수소"))
        self.label_3.setText(_translate("H", "1."))
        self.label_4.setText(_translate("H", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자 번호 : 1번</span></p><p><span style=\" font-size:14pt; font-weight:600;\">원자 기호 : H</span></p><p><span style=\" font-size:14pt; font-weight:600;\">영어 이름 : Hydrogen</span></p><p><span style=\" font-size:14pt; font-weight:600;\">한글 이름 : 수소</span></p><p><span style=\" font-size:14pt; font-weight:600;\">전자 수 : 1개</span></p><p><span style=\" font-size:14pt; font-weight:600;\">양성자 수 : 1개</span></p></body></html>"))
        self.label_5.setText(_translate("H", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">원자량 : 1.0079(g/mol)</span></p><p><span style=\" font-size:14pt; font-weight:600;\">밀도 : 0.0000899(g, Cm^3</span></p><p><span style=\" font-size:14pt; font-weight:600;\">녹는점 : -259.1˚C = -434.38˚F = 14.05K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">끓는점 : -252.9˚C = -423.22˚F = 20.25K</span></p><p><span style=\" font-size:14pt; font-weight:600;\">물질의 상태: 기체</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    H = QtWidgets.QMainWindow()
    ui = Ui_H()
    ui.setupUi(H)
    H.show()
    sys.exit(app.exec_())
