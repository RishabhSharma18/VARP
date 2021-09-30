# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'varpUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1121, 871))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("resorce.rec/background1.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
        self.startbutton.setGeometry(QtCore.QRect(80, 710, 91, 41))
        self.startbutton.setAutoFillBackground(False)
        self.startbutton.setStyleSheet("color: white; \n"
                                       "font: 8pt \"MS Shell Dlg 2\";\n"
                                       "font: 75 26pt \"Times New Roman\";\n"
                                       "background-color: rgb(0, 0, 127);")
        self.startbutton.setObjectName("startbutton")
        self.roundlabel = QtWidgets.QLabel(self.centralwidget)
        self.roundlabel.setGeometry(QtCore.QRect(450, 280, 571, 321))
        self.roundlabel.setText("")
        self.roundlabel.setPixmap(QtGui.QPixmap("resorce.rec/center2.gif"))
        self.roundlabel.setObjectName("roundlabel_2")
        self.linelabel = QtWidgets.QLabel(self.centralwidget)
        self.linelabel.setGeometry(QtCore.QRect(70, 290, 571, 301))
        self.linelabel.setText("")
        self.linelabel.setPixmap(QtGui.QPixmap("resorce.rec/center.gif"))
        self.linelabel.setObjectName("linelabel")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 120, 491, 81))
        self.textBrowser.setStyleSheet(" \n"
                                       "font: 75 28pt \"Iceland\";\n"
                                       "color: #4542fc;\n"
                                       "text-align:right ;\n"
                                       "background-color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(570, 120, 301, 81))
        self.textBrowser_2.setStyleSheet(" font: 75 28pt \"Iceland\";\n"
                                         "color: #4542fc;\n"
                                         "text-align: right;\n"
                                         "background-color: rgb(0, 0, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(170, 710, 91, 41))
        self.exitbutton.setAutoFillBackground(False)
        self.exitbutton.setStyleSheet("color: white; \n"
                                      "font: 75 26pt \"Times New Roman\";\n"
                                      "background-color: rgb(255, 0, 0);\n"
                                      " ")
        self.exitbutton.setObjectName("exitbutton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startbutton.setText(_translate("MainWindow", "I"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Sitka Heading\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#ffffff;\">  </span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Sitka Heading\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#ffffff;\"> </span></p></body></html>"))
        self.exitbutton.setText(_translate("MainWindow", "O"))


import rec_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
