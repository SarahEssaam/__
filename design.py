# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 47, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(330, 90, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(420, 90, 75, 23))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 130, 701, 231))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.textEdit_data = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_data.setGeometry(QtCore.QRect(40, 370, 701, 91))
        self.textEdit_data.setObjectName("textEdit_data")
        self.textEdit_hex = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_hex.setGeometry(QtCore.QRect(40, 470, 701, 91))
        self.textEdit_hex.setObjectName("textEdit_hex")
        self.textEdit_filter = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_filter.setGeometry(QtCore.QRect(153, 40, 411, 31))
        self.textEdit_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_filter.setObjectName("textEdit_filter")
        self.pushButton_filter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_filter.setGeometry(QtCore.QRect(580, 40, 75, 23))
        self.pushButton_filter.setObjectName("pushButton_filter")
        self.pushButton_filterRemove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_filterRemove.setGeometry(QtCore.QRect(670, 40, 75, 23))
        self.pushButton_filterRemove.setObjectName("pushButton_filterRemove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Capture"))
        self.label_2.setText(_translate("MainWindow", "Using Filter :"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_filter.setText(_translate("MainWindow", "Apply"))
        self.pushButton_filterRemove.setText(_translate("MainWindow", "Remove"))

