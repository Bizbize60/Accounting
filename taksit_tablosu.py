# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\lab\TAKSİT TABLOSU1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import mysql.connector as mysql
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql
import girdi
import taksitcikar
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.taksitcikar_window = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 593)
        MainWindow.setStyleSheet("")
        self.mydb=mysql.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="kullanici")
        self.mycursor=self.mydb.cursor()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 951, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setStyleSheet("QTableCornerButton::section { background-color:#232326; }\n"
"QHeaderView::section { color:white; background-color: #2B2B2B; }\n"
"QTableWidget::item{ background-color: #2B2B2B;bordor-color:black;color:white};\n"
"")
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 380, 951, 211))
        self.frame.setStyleSheet("\n"
"\n"
"background-color:#F5F5FA\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif White")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{font: 10pt \"MS Reference Sans Serif\"White;border-radius:10px;border:2px solid #0F0C0C;background-color:#1F1717;color:white}\n"
"QPushButton::hover{background-color:gray;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(190, 140, 231, 31))
        self.lineEdit.setStyleSheet("QLineEdit::focus{\n"
"        border:2px solid rgb(85, 255, 213);\n"
"}\n"
"QLineEdit{ \n"
"border-radius:10px;\n"
"background-color:gray;\n"
"padding:0px 10 px;\n"
"border:0;\n"
"flex:1;\n"
"color:white } ")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(0, 140, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{font: 10pt \"MS Reference Sans Serif\";border-radius:10px;border:2px solid #0F0C0C;background-color:#1F1717;color:white}\n"
"QPushButton::hover{background-color:gray;}")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 140, 31, 31))
        self.pushButton_3.setStyleSheet("QPushButton::hover{background-color:#1F1717;};\n"
"width:30px;\n"
"color:white;\n"
"border-radius:10px;\n"
"background-color:white;\n"
"color:white;\n"
"cursor:pointer;\n"
"")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/PC/Desktop/lab/arama1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame.raise_()
        self.tableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 21))
        self.menubar.setObjectName("menubar")
        self.menuTAKS_T = QtWidgets.QMenu(self.menubar)
        self.menuTAKS_T.setObjectName("menuTAKS_T")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuTAKS_T.addSeparator()
        self.menuTAKS_T.addSeparator()
        self.menubar.addAction(self.menuTAKS_T.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mycursor.execute("select * from taksit ORDER BY tarih ASC")
        results=self.mycursor.fetchall()
        for i in range(len(results)):
            for j in range(9):
                if j==6:
                    fiyat=results[i][4]
                    adet=''
                    for x in results[i][5]:
                        if x.isdigit():
                            adet=adet+'{}'.format(x)
                    int(float(adet))
                    
                    toplam=int(fiyat)*int(adet)
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(toplam)))
                    self.tableWidget.setItem(i,j+1,QTableWidgetItem(str(results[i][j])))
                elif j==7:
                    self.tableWidget.setItem(i,j+1,QTableWidgetItem(str(results[i][j])))
                elif j==8:
                    continue
                else:
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(results[i][j])))
        self.pushButton_3.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.girdi)
        self.pushButton_2.clicked.connect(self.cikar)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BÖLÜM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "KİME?"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MALZEME"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "BİRİM FİYATI"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ADET"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TOPLAM"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "KALAN TAKSİT"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "SON TARİH"))
        self.pushButton_2.setText(_translate("MainWindow", "TAKSİT ÖDE"))
        self.lineEdit.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton.setText(_translate("MainWindow", "GİRDİ"))
        self.menuTAKS_T.setTitle(_translate("MainWindow", "TAKSİT"))
    def search(self):
        
        self.tableWidget.clearSelection()
        matching_items = self.tableWidget.findItems(self.lineEdit.text(), Qt.MatchContains)
        if matching_items:
            
            for item in matching_items:
                item.setSelected(True)
    def girdi(self):
            self.girdi_window =QtWidgets.QMainWindow()
            self.girdi_ui = girdi.Girdi()
            self.girdi_ui.setupUi1(self.girdi_window)
            self.girdi_window.show()
    def cikar(self):
            self.cikti_window=QtWidgets.QMainWindow()
            self.cikartwindow=taksitcikar.cikar()
            self.cikartwindow.setupUi2(self.cikti_window)
            self.cikti_window.show()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
