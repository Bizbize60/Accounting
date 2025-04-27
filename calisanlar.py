# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 20:45:04 2023

@author: BBS
"""
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import mysql.connector
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
class Employee(QWidget):
    def __init__(self):
        super().__init__()
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="xxxxxx",
            database="xxxxxx")
        self.mycursor=self.mydb.cursor()
        self.resize(800,500)
        self.layoutmain=QHBoxLayout(self)
        self.setLayout(self.layoutmain)
        self.setWindowTitle("Çalışanlar")
        self.toolbox=QToolBox(self)
        self.layoutmain.addWidget(self.toolbox)
        self.setWindowIcon(QIcon("mavi.png"))

        
       
    #Çalışanlar Bilgi
        self.w1=QWidget(self)
        self.layout1=QVBoxLayout(self)
        
        self.table1=QTableWidget(self)
        self.table1.setRowCount(50)
        self.table1.setColumnCount(4)
        self.table1.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        self.table1.setHorizontalHeaderItem(1, QTableWidgetItem("Ad"))
        self.table1.setHorizontalHeaderItem(2, QTableWidgetItem("Soyad"))
        self.table1.setHorizontalHeaderItem(3, QTableWidgetItem("Gorev"))
        self.table1.resize(800,500)
        
        
        
        self.layout1.addWidget(self.table1)
        self.w1.setLayout(self.layout1)
        
        self.show_employee()
        
        
        
        self.toolbox.addItem(self.w1,"Çalışanlar")
        
        #ÇALIŞAN EKLE BIRAK
        #2.sayfanın main layoutu
        self.layout2main=QVBoxLayout(self)
        
        self.w2=QWidget(self)
        
        
        self.layout2_1=QGridLayout(self)
        
        self.name=QLineEdit("AD",self)
        self.layout2_1.addWidget(self.name,0,0)
        
        #layout2_1
        self.surname=QLineEdit("SOYAD",self)
        self.layout2_1.addWidget(self.surname,0,1)
        
        self.tc=QLineEdit("TC",self)
        self.layout2_1.addWidget(self.tc,0,2)
        
        self.position=QLineEdit("Görev",self)
        self.layout2_1.addWidget(self.position,1,0)
        
        self.phone=QLineEdit("Telefon",self)
        self.layout2_1.addWidget(self.phone,1,1)
        
        self.address=QLineEdit("Adress",self)
        self.layout2_1.addWidget(self.address,1,2)

        self.loadbutton=QPushButton("Ekle",self)
        self.loadbutton.clicked.connect(self.insert_data)
        
        
        self.layout2_1.addWidget(self.loadbutton,2,0)
        self.layout2main.addLayout(self.layout2_1)
        #layout2_2
        
        self.layout2_2=QGridLayout(self)
        
        self.infoinput=QLineEdit(self)
        self.layout2_2.addWidget(self.infoinput,0,0)
        
        self.infobutton=QPushButton("Tc Ya da Id",self)
        self.layout2_2.addWidget(self.infobutton,0,1)
        
        self.infolabel=QLabel(self)
        self.layout2_2.addWidget(self.infolabel,1,0)
        
        self.deleteinput=QLineEdit(self)
        self.layout2_2.addWidget(self.deleteinput,4,0)
        
        self.deletebutton=QPushButton("Sil",self)
        self.layout2_2.addWidget(self.deletebutton,4,1)   
        
        self.imageinput=QLineEdit("Fotoğraf Eklemek İçin Id Girin",self)
        self.layout2_2.addWidget(self.imageinput,2,0)
        
        self.imagebutton=QPushButton(self)
        self.layout2_2.addWidget(self.imagebutton,2,1)
        
        self.retrieveimage=QLineEdit("Fotoğraf İçin Id Girin",self)
        self.layout2_2.addWidget(self.retrieveimage,3,0)
        
        
        self.retrieveimagebutton=QPushButton(self)
        self.layout2_2.addWidget(self.retrieveimagebutton,3,1)
        
        self.layout2main.addLayout(self.layout2_2) 
        
        self.infobutton.clicked.connect(self.show_info)
        self.deletebutton.clicked.connect(self.delete)        
        self.imagebutton.clicked.connect(self.browsersearch)
        self.retrieveimagebutton.clicked.connect(self.retrieve)
        
        self.w2.setLayout(self.layout2main)
        #
        self.toolbox.addItem(self.w2,"Çalışan Ekle Bırak")
    #Çalışanları Ekle-Bırak  
       

    def show_employee(self):
        self.mycursor.execute("SELECT * FROM calisanlar")
        results=self.mycursor.fetchall()
        for i in range (len(results)):
            for j in range (4):
                self.table1.setItem(i,j,QTableWidgetItem(str(results[i][j])))
                self.table1.horizontalHeader().setSectionResizeMode(j,QHeaderView.Stretch)


    def insert_data(self):
        data="Insert Into calisanlar (ad,soyad,pozisyon) VALUES (%s,%s,%s)"
        val=(self.name.text(),self.surname.text(),self.position.text())
        self.mycursor.execute(data,val)
        self.mydb.commit()
        self.mycursor.execute(f"Select Calisan_id from calisanlar where ad='{self.name.text()}' and soyad='{self.surname.text()}'")
        number=self.mycursor.fetchall()
        data="Insert Into calisan_bilgi VALUES (%s,%s,%s,%s)"
        val=(self.tc.text(),self.phone.text(),self.address.text(),number[0][0])
        self.mycursor.execute(data,val)  
        self.mydb.commit()

    def show_info(self):
        
        val=(self.infoinput.text())
        if len(str(val)) == 11:
            data="Select * From calisan_bilgi Where tc=(%s)"
            my_list=[val]
            self.mycursor.execute(data,my_list)
            string=""
            results=self.mycursor.fetchall()
            for x in results:
                string+=str(x)
            
            self.infolabel.setText(string)
            self.infolabel.setStyleSheet("font-family:'Times New Roman', Times, serif,font:bold 14px")
            self.infolabel.adjustSize()
        else:
            data="Select * From Calisan_bilgi where id=(%s)"
            my_list=[val]
            self.mycursor.execute(data,my_list)
            
            string=""
            results=self.mycursor.fetchall()
            for x in results:
                string+=str(x)
            self.infolabel.setText(string) 
            
            self.infolabel.adjustSize()
        
    def delete(self):
        command="Delete  From calisan_bilgi Where Id=(%s)"
        val=[self.deleteinput.text()]
        self.mycursor.execute(command,val)
        self.mydb.commit()
        command="Delete from Calisanlar where Calisan_id=(%s)"
        self.mycursor.execute(command,val)
        self.mydb.commit()
    def browsersearch(self):
        def files():
            Id=self.imageinput.text()
            self.root.filenames=filedialog.askopenfilenames(initialdir=r"",title="Seç",filetypes=[("All Files","*.*")])
            self.files = self.root.tk.splitlist(self.root.filenames)
            self.counter="photo0"
            self.images=[]
            self.s=""
            for i in range(len(self.files)):
                               
                with open(self.files[i],"rb") as file:
                    if i==0:
                            self.images.append(file.read())
                            self.s+="%s"
                    else:
                           self.images.append(file.read())
                           self.counter+=f",photo{i}"
                           self.s+=",%s"
            command=f"Insert Into images (id,{self.counter}) VALUES ({self.imageinput.text()},{self.s})"
            data=self.images
            self.mycursor.execute(command,data)
            self.mydb.commit()      
            
        self.root=Tk()
        self.root.title("Calisan Bilgi")
        self.root.geometry("500x50")
        self.b1=Button(self.root,text="Fotoğraf Sec", command=files)
        self.b1.pack()

        self.root.mainloop()  
    def retrieve(self):
        Statement=f"Select * From Images Where id ={self.retrieveimage.text()}"
        self.mycursor.execute(Statement)
        results=self.mycursor.fetchone()
        counter=0
        for i in range (len(results)):
            if results[i]==None or str(results[i]).isnumeric():
                continue
            else:
                path=""
                with open (path,"wb") as file:
                    file.write(results[i])
                    file.close()
                                                                          
                
            
                
            
            
