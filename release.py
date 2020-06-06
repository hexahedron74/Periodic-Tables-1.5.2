# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'release.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os

class Ui_releasenote(object):
    def setupUi(self, releasenote):
        releasenote.setObjectName("releasenote")
        releasenote.setFixedSize(791, 461)
        releasenote.setStyleSheet("background: rgb(74, 129, 124)")
        self.centralwidget = QtWidgets.QWidget(releasenote)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, -10, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 70, 731, 341))
        self.textBrowser.setStyleSheet("background: rgb(255, 255, 255)")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.raise_()
        self.label.raise_()
        releasenote.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(releasenote)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 25))
        self.menubar.setObjectName("menubar")
        releasenote.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(releasenote)
        self.statusbar.setObjectName("statusbar")
        releasenote.setStatusBar(self.statusbar)

        self.retranslateUi(releasenote)
        QtCore.QMetaObject.connectSlotsByName(releasenote)

    def retranslateUi(self, releasenote):
        _translate = QtCore.QCoreApplication.translate
        releasenote.setWindowTitle(_translate("releasenote", "RELEASE NOTE V1.5.2"))
        self.label.setText(_translate("releasenote", "RELEASE NOTE V1.5.2"))
        self.textBrowser.setHtml(_translate("releasenote", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">PERIODIC TABLE VERSION 1.5.2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">*Updated Items*</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\"> -20 elements for Beta Version</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\"> -The new GUI Screen</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">*Manual*</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\"> -Press Start Button to Start!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\"> -Click the button in Periodic Table.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">  Then you can see the informations of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">  elements that you chose.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">*Copyright*</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Copyright ⓒ JWare Soft Development Team 2019-2020</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    releasenote = QtWidgets.QMainWindow()
    ui = Ui_releasenote()
    ui.setupUi(releasenote)
    releasenote.show()
    sys.exit(app.exec_())
