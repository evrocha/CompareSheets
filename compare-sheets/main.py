import sys; import os;
import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from openpyxl.utils import *
sheet1 = []
sheet2 = []
wblist = []
class MainWindow(QDialog):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        super().__init__()
        
        loadUi("C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets\\compare-sheets\\up_file-screen.ui", self)
        self.browse.clicked.connect(self.get_first_sheet)
        self.browse2.clicked.connect(self.get_sec_sheet)
        self.comparar_btn.clicked.connect(self.comparar)

    def get_first_sheet(self):
        get_version_old= QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets')         # pega o arquivo
        self.filename.setText(get_version_old[0])  
        file_path = (get_version_old[0]) # caminho 
        initial_sheet = pd.read_excel(file_path) 
        sheet1.append(initial_sheet)
        print(f"{sheet1[0]} INICIAL" )

    def get_sec_sheet(self):
        get_version_new = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets') # pega o arquivo
        self.filename2.setText(get_version_new[0])
        file_path2 = (get_version_new[0])
        updated_sheet = pd.read_excel(file_path2)
        sheet2.append(updated_sheet)
        print(f"{sheet2[0]} FINAL" )
        
    def comparar(self):
        finalList = []

        # fileone = sheet1[0].readlines() --- # exemplo

        lines = []
        lines2 =[]

        # linhas planiilhas s
        for line in sheet1[0]:
            lines.append((lines.iloc[0,0]))
            print(type(line))
        # linhas planilhas 2
        for line2 in sheet2[0]:
            lines2.append((lines2.iloc[0,0]))

        for lineTotal in lines2:
            if lineTotal not in lines:
                writer = pd.ExcelWriter('output.xlsx', engine ='xlsxwriter')
                writer.save()
                # escrever a nova planilha com as diferenças
               

        # pegar linha por linha do arquivo
        



    #  equivalente a readline 

#      lines = []

#     In [387]: for line in pd.read_csv('./data_sample.tsv', encoding='utf-8', header=None, chunksize=1):
#     lines.append(line.iloc[0,0])


        
# iterando sobre a planilha selecionada

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
sys.exit(app.exec_())
