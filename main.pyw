from PyQt5 import QtCore, QtGui, QtWidgets
from table import Ui_Table
from release import Ui_releasenote
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
class Ui_PeriodicTables152(object):
    def table(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Table()
        self.ui.setupUi(self.window)
        PeriodicTables152.hide()
        self.window.show()
    def releasenote(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_releasenote()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, PeriodicTables152):
        PeriodicTables152.setObjectName("PeriodicTables152")
        PeriodicTables152.setFixedSize(791, 461)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        PeriodicTables152.setFont(font)
        PeriodicTables152.setStyleSheet("background: rgb(74, 129, 124)")
        self.centralwidget = QtWidgets.QWidget(PeriodicTables152)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 561, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background:rgb(74, 129, 124)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 360, 581, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:rgb(74, 129, 124)")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(270, 220, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.table)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 100, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1_2.setGeometry(QtCore.QRect(270, 290, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn1_2.setFont(font)
        self.btn1_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.btn1_2.setObjectName("btn1_2")
        self.btn1_2.clicked.connect(self.releasenote)
        PeriodicTables152.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PeriodicTables152)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        PeriodicTables152.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PeriodicTables152)
        self.statusbar.setObjectName("statusbar")
        PeriodicTables152.setStatusBar(self.statusbar)

        self.retranslateUi(PeriodicTables152)
        QtCore.QMetaObject.connectSlotsByName(PeriodicTables152)

    def retranslateUi(self, PeriodicTables152):
        _translate = QtCore.QCoreApplication.translate
        PeriodicTables152.setWindowTitle(_translate("PeriodicTables152", "Periodic Table 1.5.2"))
        self.label.setText(_translate("PeriodicTables152", "Periodic Table"))
        self.label_2.setText(_translate("PeriodicTables152", "Copyright ⓒ JWare Soft Development Team 2019-2020"))
        self.btn1.setText(_translate("PeriodicTables152", "START PROGRAM"))
        self.label_3.setText(_translate("PeriodicTables152", "Version 1.5.2"))
        self.btn1_2.setText(_translate("PeriodicTables152", "RELEASE NOTE"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PeriodicTables152 = QtWidgets.QMainWindow()
    ui = Ui_PeriodicTables152()
    ui.setupUi(PeriodicTables152)
    PeriodicTables152.show()
    sys.exit(app.exec_())
