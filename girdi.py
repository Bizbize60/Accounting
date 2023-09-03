# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girdi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import  QApplication,QWidget ,QMainWindow, QTableWidget, QTableWidgetItem, QDesktopWidget,QLabel,QPushButton,QLineEdit,QCheckBox,QComboBox

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql
import sys
class Girdi(object):
    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 166)
        MainWindow.setStyleSheet("QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"QLabel {\n"
"background:transparent;\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"};\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"};")
        self.mydb=mysql.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="kullanici")
        self.mycursor=self.mydb.cursor()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bolum = QtWidgets.QLineEdit(self.centralwidget)
        self.bolum.setGeometry(QtCore.QRect(0, 20, 113, 20))
        self.bolum.setObjectName("bolum")
        self.kim = QtWidgets.QLineEdit(self.centralwidget)
        self.kim.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.kim.setObjectName("kim")
        self.malzeme = QtWidgets.QLineEdit(self.centralwidget)
        self.malzeme.setGeometry(QtCore.QRect(250, 20, 113, 20))
        self.malzeme.setObjectName("malzeme")
        self.fiyat = QtWidgets.QLineEdit(self.centralwidget)
        self.fiyat.setGeometry(QtCore.QRect(0, 60, 113, 20))
        self.fiyat.setObjectName("fiyat")
        self.adet = QtWidgets.QLineEdit(self.centralwidget)
        self.adet.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.adet.setObjectName("adet")
        self.taksit = QtWidgets.QLineEdit(self.centralwidget)
        self.taksit.setGeometry(QtCore.QRect(250, 60, 113, 20))
        self.taksit.setObjectName("taksit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 47, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 0, 47, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 47, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 47, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 40, 47, 21))
        self.label_6.setObjectName("label_6")
        self.tarih = QtWidgets.QLineEdit(self.centralwidget)
        self.tarih.setGeometry(QtCore.QRect(0, 100, 113, 20))
        self.tarih.setStyleSheet("QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"};\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"};")
        self.tarih.setObjectName("tarih")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 79, 20))
        self.pushButton.setStyleSheet("QPushButton::hover{background-color:gray;}\n"
"QPushButton{font: 10pt \\\"MS Reference Sans Serif\\\";border-radius:10px;border:2px solid #0F0C0C;background-color:#1F1717;color:white};\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ekle)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName("menubar")
        self.menuG_RD = QtWidgets.QMenu(self.menubar)
        self.menuG_RD.setObjectName("menuG_RD")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuG_RD.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BÖLÜM"))
        self.label_2.setText(_translate("MainWindow", "KİME?"))
        self.label_3.setText(_translate("MainWindow", "MALZEME"))
        self.label_4.setText(_translate("MainWindow", "FİYAT"))
        self.label_5.setText(_translate("MainWindow", "ADET"))
        self.label_6.setText(_translate("MainWindow", "TAKSİT"))
        self.label_7.setText(_translate("MainWindow", "SON TARİH"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.menuG_RD.setTitle(_translate("MainWindow", "GİRDİ"))

    def ekle(self):
        data=(self.bolum.text(),self.kim.text(),self.malzeme.text(),self.fiyat.text(),self.adet.text(),self.taksit.text(),self.tarih.text())
        command="INSERT INTO taksit (bolum,kim,malzeme,birim_fiyati,adet,taksit,tarih) VALUES (%s,%s,%s,%s,%s,%s,STR_TO_DATE(%s,'%Y-%m-%d'))"
        self.mycursor.execute(command,data)
        self.mydb.commit()  
