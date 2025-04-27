import xlwt
import mysql.connector
import sys
from PyQt5.QtWidgets import QWidget,QMainWindow,QLabel,QLineEdit,QTableWidget,QTableWidgetItem,QApplication,QPushButton
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Counter(QWidget):
    def __init__(self):
        super().__init__()
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="xxxxx",
            database="xxxxxxx")
        self.mycursor=self.mydb.cursor()
        self.properties()
        self.textures()
        self.reload_button.clicked.connect(self.reload)
        self.load_button.clicked.connect(self.load)
        self.change_button.clicked.connect(self.change)
        self.info_button.clicked.connect(self.go)
        self.excel_button.clicked.connect(self.excel)        
        
    def properties(self):
        self.resize(960,500)
        self.move(600,100)
        self.setWindowTitle("Sayaç")
        
        
        
    def textures(self):
        self.table=QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setRowCount(500)
        self.table.setMinimumHeight(500)
        self.table.setMinimumWidth(700)
        self.table.setStyleSheet("selection-background-color : blue")
                
        
        
       
        
        self.reload_button=QPushButton("Yenile",self)
        self.reload_button.move(700,0)
        self.reload_button.resize(100,25)
        
        self.input_no=QLineEdit("Sayaç No",self)
        self.input_company=QLineEdit("Merkez",self)
        self.input_indate=QLineEdit("Geliş Tarihi",self)
        self.input_outdate=QLineEdit("Çıkış Tarihi",self)
        self.input_inprice=QLineEdit("Geliş Fiyatı",self)
        self.input_outprice=QLineEdit("Çıkış Fiyatı",self)
        
        self.input_no.move(700,25)
        self.input_company.move(800,25)
        
        self.input_indate.move(700,50)
        self.input_outdate.move(800,50)
        
        self.input_inprice.move(700,75)
        self.input_outprice.move(800,75)
        
        self.load_button=QPushButton("Ekle",self)
        self.load_button.move(700,95)
        
        self.input_change_no=QLineEdit("Hangi Sayaç",self)
        self.input_change_outdate=QLineEdit("Çıkış Tarihi",self)
        self.input_change_outprice=QLineEdit("Çıkış Fiyatı",self)
        
        self.input_change_no.move(700,150)
        self.input_change_outdate.move(800,150)
        self.input_change_outprice.move(700,170)
        self.input_change_outprice.resize(101,20)
        
        self.change_button=QPushButton("Değiştir",self)
        self.change_button.move(801,170) 
        
        self.input_info=QLineEdit("Sayaç Bilgi",self)
        self.input_info.move(700,200)
        self.input_info.resize(100,20)
        
        self.info_button=QPushButton("Görüntüle",self)
        self.info_button.move(800,199)
        
        self.excel_button=QPushButton("Excel",self)
        self.excel_button.move(700,220)
       
        
    def reload(self):
        self.mycursor.execute("Select * From sayac")
        results=self.mycursor.fetchall()
        for i in range(len(results)):
            for j in range(6):
                if i%2==0:
                    self.table.setItem(i,j,QTableWidgetItem(str(results[i][j])))
                    self.table.item(i,j).setBackground(QColor(128, 128, 128))
                else:
                    self.table.setItem(i,j,QTableWidgetItem(str(results[i][j])))
    def load(self):
        val=(self.input_no.text(), self.input_company.text(), self.input_indate.text(), self.input_outdate.text(), self.input_inprice.text(), self.input_outprice.text())
        data="Insert Into sayac Values (%s,%s,%s,%s,%s,%s)"
        self.mycursor.execute(data,val)
        self.mydb.commit()  
    def change(self):
        data="Update sayac SET gidis_tarihi=(%s), gidis_fiyati=(%s) Where sayac_no=(%s)"
        val=(self.input_change_outdate.text(),self.input_change_outprice.text(),self.input_change_no.text())
        self.mycursor.execute(data,val)
        self.mydb.commit()           
    def go(self):
        counter=0
        data="Select sayac_no from sayac"
        val=self.input_info.text()
        self.mycursor.execute(data)
        results=self.mycursor.fetchall()
        for x in results:
            if x[0]==int(val):
                column = 0
                index = self.table.model().index(counter, column)
                self.table.scrollTo(index)
            else:
                counter+=1
        
    def excel(self):
        self.mycursor.execute("Select * from sayac")
        results=self.mycursor.fetchall()
        #Creating Excel
        workbook=xlwt.Workbook(encoding="utf-8")
        worksheet=workbook.add_sheet("Veriler")
        #Heads
        columns=[i[0] for i in self.mycursor.description]
        for i , column in enumerate(columns):
            worksheet.write(0,i,column)
        #Inserting    
        for row_idx, row in enumerate(results, start=1):
            for col_idx, cell_value in enumerate(row):
                worksheet.write(row_idx,col_idx,cell_value)
        workbook.save("Sayac.xls")
    
        
