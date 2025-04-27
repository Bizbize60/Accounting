import datetime
import sayac
import xlwt
import mysql.connector
import sys
from PyQt5.QtWidgets import  QApplication,QWidget ,QMainWindow, QTableWidget, QTableWidgetItem, QDesktopWidget,QLabel,QPushButton,QLineEdit,QCheckBox,QComboBox
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtGui,QtCore,uic
import ctypes
import taksit_tablosu
import calisanlar


class button_widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="xxxxx",
            database="xxxx")
        self.mycursor=self.mydb.cursor()
        self.properties()
        self.textures()
        self.input_button.clicked.connect(self.addData)
    def properties(self):
        self.resize(500,30)
        self.move(500,500)
        self.setWindowTitle("Input Screen")
    def textures(self):
        self.cmb=QComboBox(self)
        self.cmb.addItem("ALINACAK")
        self.cmb.addItem("VERİLECEK")
        
        self.input_company=QLineEdit("Şirket",self)
        self.input_company.move(100,0)
        
        self.input_price=QLineEdit("Fiyat",self)
        self.input_price.move(200,0)
        
        self.input_date=QLineEdit("Tarih",self)
        self.input_date.move(300,0)
        
        self.input_button=QPushButton("Ekle",self)
        self.input_button.move(400,0)
    def addData(self):
        data="Insert Into kasa (tip,sirket,fiyat,tarih) VALUES (%s,%s,%s,%s)"
        val=[self.cmb.currentText(),self.input_company.text(),self.input_price.text(),self.input_date.text()]
        self.mycursor.execute(data,val)
        self.mydb.commit()
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="xxxx",
            database="xxxx")
        self.mycursor=self.mydb.cursor()
        self.properties_MainWindow()
        self.textures_MainWindow()
        self.CaseLabel_MainWindow()
        
        
        
        
        self.table_MainWindow()
   
        self.button_MainWindow.clicked.connect(self.input_button)
        self.button_Pdf.clicked.connect(self.case_excel)
        self.counter_button.clicked.connect(self.counter_window)
        self.openerbutton.clicked.connect(self.browser)
        
        self.buttoncounter=0
        
    def properties_MainWindow(self):
        self.resize(1050,750)
        self.move(300,100)
        self.setWindowTitle("Ana Ekran")
        
    def textures_MainWindow(self):
        self.button_MainWindow=QPushButton("Girdi Ekle",self)
        self.button_MainWindow.move(700,300)
        
        self.button_Pdf=QPushButton("EXCEL",self)
        self.button_Pdf.move(600,300)
    
        self.label_MainWindow=QPushButton(self)
        self.label_MainWindow.resize(500,50)
        self.label_MainWindow.setText(self.CaseLabel_MainWindow())
        self.label_MainWindow.move(50,300)
        self.label_MainWindow.setFont(QFont("Arial",26))
       
        self.label_MainWindow.adjustSize()
        
        self.counter_button=QPushButton("Sayaçlar",self)
        self.counter_button.move(500,0)
        
        self.openerbutton=QPushButton(self)
        self.openerbutton.resize(50,750)
        self.openerbutton.setIcon(QIcon("arrow.png"))
        self.openerbutton.setStyleSheet("padding:2 -5 2 2;background-color:	 #AFAFAF")
        self.openerbutton.move(0,50)
        
        self.colorlabel=QLabel(self)
        self.colorlabel.resize(1050,50)
        self.colorlabel.move(0,0)
        self.colorlabel.setStyleSheet("background-color:#E7E6E7")
        
        self.logolabel=QLabel("Bahadırım",self)
        self.logolabel.setPixmap(QPixmap("logos.png").scaled(50,64,Qt.AspectRatioMode.KeepAspectRatio))
        self.logolabel.setStyleSheet("padding:0 -100 0 -100;background-color:#E7E6E7")
        self.logolabel.resize(100,50)
        self.logolabel.move(0,0)
        
        
    def CaseLabel_MainWindow(self):
        self.mycursor.execute("Select fiyat from kasa where tip='alinacak' ")
        self.results=self.mycursor.fetchall()
        self.income_case=0
        for income in self.results:
            self.income_case+=income[0]
        self.mycursor.execute("Select fiyat from kasa where tip='verilecek' ")
        self.results=self.mycursor.fetchall()
        for outcome in self.results:
            self.income_case-=outcome[0]
        return f"Kasa:{self.income_case}"    
    def table_MainWindow(self):
        self.mycursor.execute("Select * from kasa")
        self.results=self.mycursor.fetchall()
      
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.move(50,50)
        self.table.setRowCount(1000)
    
        self.table.resize(1050,750)
       
        self.table.horizontalHeader().setDefaultSectionSize(250)
        self.table.setFont(QFont('Calibri',15))
        self.mycursor.execute("SELECT * from kasa")
        self.results=self.mycursor.fetchall()
        self.results.reverse()
        self.length=len(self.results)  
        for i in range(self.length):
             for j in range(4):
                 self.table.setItem(i,j,QTableWidgetItem(str(self.results[i][j])))
        
    
    def input_button(self):
        self.button_widget=button_widget()
        self.button_widget.show()
        
    def case_excel(self):
        self.create_excel()
                         
    def create_excel(self):
        self.mycursor.execute("Select * from kasa")
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
        workbook.save("Veriler.xls")      
        
    def counter_window(self):
        self.counter_window=sayac.Counter()
        self.counter_window.show()
    def browser(self):
        self.buttoncounter+=1
        if self.buttoncounter % 2 ==1:
            self.resize(1400,750)
            self.table.move(350,50)
            self.colorlabel.resize(1400,50)
            
            self.counter_button.move(50,50)
            self.counter_button.resize(350,50)
            self.counter_button.setStyleSheet("padding:2 100 2 50")
            self.counter_button.setFont(QFont("Arial",12))
            
            self.button_MainWindow.move(50,100)
            self.button_MainWindow.resize(350,50)
            self.button_MainWindow.setStyleSheet("padding:2 100 2 50")
            self.button_MainWindow.setFont(QFont("Arial",12))
            
            self.button_Pdf.move(50,150)
            self.button_Pdf.resize(350,50)
            self.button_Pdf.setStyleSheet("padding:2 100 2 50")
            self.button_Pdf.setFont(QFont("Arial",12))
            
            self.searchbar=QLineEdit(self)
            self.searchbar.move(100,705)
            self.searchbar.resize(200,45)
            self.searchbar.show()
            
            self.searchbarbutton=QPushButton(self)
            self.searchbarbutton.move(300,705)
            self.searchbarbutton.resize(50,45)
            self.searchbarbutton.clicked.connect(self.search)
            self.searchbarbutton.show()
            
            self.searchicon=QLabel(self)
            self.searchicon.setPixmap(QPixmap("arama.png").scaled(50,50,Qt.AspectRatioMode.KeepAspectRatio))
            self.searchicon.setStyleSheet("background:transparent;padding:0 2 0 5")
            self.searchicon.move(50,700)
            self.searchicon.resize(50,50)
            self.searchicon.show()
            
            self.label_MainWindow.resize(350,50)
            self.label_MainWindow.move(50,645)
            self.label_MainWindow.setStyleSheet("padding:0 150 0 0")
            
            self.calisanlarbutton=QPushButton("Çalışanlar",self)
            self.calisanlarbutton.move(50,200)
            self.calisanlarbutton.resize(300,50)
            self.calisanlarbutton.setStyleSheet("padding:2 100 2 90;font-family:Arial")
            self.calisanlarbutton.setFont(QFont("Arial",12))
            self.calisanlarbutton.clicked.connect(self.employees)
            self.calisanlarbutton.show()
           
            self.taksitbutton=QPushButton("Taksit",self)
            self.taksitbutton.move(50,250)
            self.taksitbutton.resize(300,50)
            self.taksitbutton.setStyleSheet("padding:2 100 2 90;font-family:Arial")
            self.taksitbutton.setFont(QFont("Arial",12))
            self.taksitbutton.clicked.connect(self.taksit)
            self.taksitbutton.show()
        else:
            self.resize(1050,750)
            
            self.table.move(50,50)
            
            self.button_MainWindow.move(700,300)
            
            
            self.button_Pdf.move(600,300)
        
            
            self.label_MainWindow.setText(self.CaseLabel_MainWindow())
            self.label_MainWindow.move(50,300)
            self.label_MainWindow.setFont(QFont("Arial",16))
            self.label_MainWindow.adjustSize()
            
         
            self.counter_button.move(500,0)
            
            
            self.openerbutton.resize(50,750)
            self.openerbutton.setIcon(QIcon("arrow.png"))
            self.openerbutton.setStyleSheet("padding:2 -5 2 2;background-color:	 #AFAFAF")
            self.openerbutton.move(0,50)
            
            
            self.colorlabel.resize(1050,50)
            self.colorlabel.move(0,0)
            self.colorlabel.setStyleSheet("background-color:#E7E6E7")
            
            self.logolabel=QLabel("Bahadırım",self)
            self.logolabel.setPixmap(QPixmap("logos.png").scaled(50,64,Qt.AspectRatioMode.KeepAspectRatio))
            self.logolabel.setStyleSheet("padding:0 -100 0 -100;background-color:#E7E6E7")
            self.logolabel.resize(100,50)
            self.logolabel.move(0,0)
            
            
            self.searchicon.hide()
            self.searchbarbutton.hide()
            self.searchbar.hide()
            self.taksitbutton.hide()
            self.calisanlarbutton.hide()
    def search(self):
        self.mycursor.execute("Select * from kasa")
        self.results=self.mycursor.fetchall()
        self.results.reverse()
        self.length=len(self.results)  
        for i in range(self.length):
             for j in range(4):
                 self.table.setItem(i,j,QTableWidgetItem(str(self.results[i][j])))
        self.command="Select sirket From kasa"
        self.mycursor.execute(self.command)
        self.results=self.mycursor.fetchall()
        self.results.reverse()
        for dx,i in enumerate(self.results):
            if self.searchbar.text()==i[0]:
             for j in range(4):              
                 self.table.item(dx,j).setBackground(QColor(128, 128, 128))
    def employees(self):
        
       self.calisanwindow=calisanlar.Employee()
       self.calisanwindow.show()
       
    def taksit(self):
        self.calisanekran=QMainWindow()
        self.calisanui=taksit_tablosu.Ui_MainWindow()
        self.calisanui.setupUi(self.calisanekran)
        self.calisanekran.show()
                                 
class FirstPage(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="xxxxx"
            )
        self.today=datetime.date.today()
        self.mycursor=self.mydb.cursor()
        self.properties_FirsPage()
        self.textures_FirstPage()
        self.FirstPageButton.clicked.connect(self.login)
        
    def properties_FirsPage(self):
        self.resize(450,240)
        self.move(600,300)
        self.setWindowIcon(QIcon("mavi.png"))
        
        
        
       
        
        self.setWindowTitle("Giriş Ekranı")
        self.setStyleSheet("background-color:white")
        self.firstpagephoto=QLabel(self)
        self.firstpagephoto.setStyleSheet("background-color:white")
        self.firstpagephoto.resize(450,250)
        
        self.show()        

    def textures_FirstPage(self):
        
        
        
        
        
        
        self.username=QLineEdit(self)
        self.username.move(100,70)
        self.username.setStyleSheet("border:none;outline:none;color:black;background-color:gray;background:transparent;border-bottom:1px solid black")
        
        self.username.show()
        
        self.usernamelabel=QLabel("Kullanıcı Adı",self)
        self.usernamelabel.move(100,50)
        self.usernamelabel.setStyleSheet("font-family:Arial Black")
        
        self.usernamelabel.show()
        
        
        
        
        
        self.password=QLineEdit(self)
        self.password.move(100,120)
        self.password.setStyleSheet("border:none;border-bottom:1px solid black ;color:black;background:transparent")
        self.password.show()
        
        self.passwordlabel=QLabel("Şifre",self)
        self.passwordlabel.move(100,100)
        self.passwordlabel.setStyleSheet("font-family:Arial Black")
        self.passwordlabel.show()
        
        self.loginicon=QLabel(self)
        self.loginicon.setPixmap(QPixmap("user.png").scaled(30,30,Qt.AspectRatioMode.KeepAspectRatio))
        self.loginicon.setStyleSheet("padding:2 2 2 2;background:transparent")
        self.loginicon.resize(35,30)
        self.loginicon.move(65,70)
        self.loginicon.show()
        
        self.passwordicon=QLabel(self)
        self.passwordicon.setPixmap(QPixmap("sifre.png").scaled(32,32,Qt.AspectRatioMode.KeepAspectRatio))
        self.passwordicon.setStyleSheet("background:transparent")
        self.passwordicon.resize(30,30)
        self.passwordicon.move(65,120)
     
        self.passwordicon.show()
        
        
             
        self.FirstPageButton=QPushButton("Giriş",self)
        self.FirstPageButton.resize(100,30)
        self.FirstPageButton.move(100,160)
        self.FirstPageButton.setIcon(QIcon('tik.png'))
        self.FirstPageButton.setStyleSheet("""
                                           QPushButton {
                                               border-radius:8px;
                                               border: 1px solid black;
                                               background:transparent;
                                               color:black;
                                               }
                                           QPushButton:hover {
                                               background-color: gray;
                                               }
                                           QPushButton:pressed {
                                               color:red;
                                               }
                                           """)
        
        
        self.FirstPageButton.show()
        
        self.FirstPageLabel=QLabel(self)
        self.FirstPageLabel.setPixmap(QPixmap("logo.png").scaled(240,240,Qt.AspectRatioMode.KeepAspectRatio))
        self.FirstPageLabel.setStyleSheet("background:transparent")
        
                                      
        
        self.FirstPageLabel.move(240,0)
        self.FirstPageLabel.adjustSize()
        self.FirstPageLabel.show()
        
        self.enterlabel=QLabel(self)
        self.enterlabel.move(100,30)
        self.enterlabel.setStyleSheet("background:transparent;color:darkred;font-size:6")
        self.enterlabel.show()
        
        self.copylabel=QLabel("@Copyright Mavi-Bilisim",self)
        self.copylabel.move(0,225)
        self.copylabel.adjustSize()
        self.copylabel.setStyleSheet("background:transparent;color:black")
        self.copylabel.setFont(QFont("Uni Sans Heavy Italic",8))
        self.copylabel.show()
        
        self.datelabel=QLabel(self)
        self.datelabel.setText(f"{self.today}")
        self.datelabel.move(380,0)
        self.datelabel.setStyleSheet("color:black;background:transparent;font-size:12px")
        
        self.datelabel.setFont(QFont("Uni Sans Heavy Italic",8))
        self.datelabel.show()
              
    def login(self):
        self.mycursor.execute("USE kullanici")
        if  self.username.text()=="" or self.password.text()=="":
            self.enterlabel.setText("Kullanici Adi Ve Şifre Girin")
            self.enterlabel.adjustSize()
            
        else:
            self.mycursor.execute("SELECT * FROM users")
            self.results=self.mycursor.fetchall()
            for x in self.results:
                if self.username.text()==x[0] and self.password.text()==x[1]:
                    self.FirstPageLabel.setText("Giriş Yapıldı")
                    self.hide()
                    self.MainWindow=MainWindow()
                    self.MainWindow.show()
                else:
                   self.enterlabel.setText("Yanlış Kullanıcı Adı / Şifre")
                   self.enterlabel.adjustSize()

app=QApplication(sys.argv)
window=FirstPage() 
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

sys.exit(app.exec_())
