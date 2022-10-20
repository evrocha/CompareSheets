from cgi import print_form
from math import nan
from operator import index
from turtle import pen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys;
import pandas as pd
import numpy as np

sheet1 = []
sheet2 = []
wblist = []
paths = []
list_qtd = []
list_cod = []
list_qtd2 = []
list_cod2 = []
output_cod = []
output_qtd = []
output = []
rows = []
#                                                 --- PANDAS VERSION
class MainWindow(QDialog):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        super().__init__()
        
        loadUi("C:\\Users\\Saulo\\Documents\\GitHub\\CompareSheets\\compare-sheets\\up_file-screen.ui", self)
        # loadUi("D:\\Programação\\CompareSheets\\compare-sheets\\up_file-screen.ui", self)
        self.browse.clicked.connect(self.get_first_sheet)
        self.browse2.clicked.connect(self.get_sec_sheet)
        self.comparar_btn.clicked.connect(self.comparar)

    def get_first_sheet(self):
        get_version_old = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Saulo\\Documents\\GitHub\\CompareSheets\\compare-sheets')         # pega o arquivo
        # get_version_old = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\Programação\\CompareSheets\\compare-sheets') 
        self.filename.setText(get_version_old[0])  
        file_path = (get_version_old[0]) # caminho 

        paths.append(file_path)

        initial_sheet = pd.read_excel(file_path) 
        sheet1.append(initial_sheet)
        
        lista_colunas_s1 = initial_sheet.columns.tolist()

        cod1 = (lista_colunas_s1[3]) # codigo
        qtd1 = (lista_colunas_s1[1]) # quantidade
        
        for index, row in initial_sheet.iterrows():
            list_qtd.append(row[qtd1])
            list_cod.append(row[cod1])

    def get_sec_sheet(self):
        get_version_new = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets\\compare-sheets') # pega o arquivo
        # get_version_new = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\Programação\\CompareSheets\\compare-sheets')
        self.filename2.setText(get_version_new[0])

        file_path2 = (get_version_new[0])
        paths.append(file_path2)

        updated_sheet = pd.read_excel(file_path2)
        sheet2.append(updated_sheet) 

        lista_colunas_s2 = updated_sheet.columns.to_list()
        cod2 = (lista_colunas_s2[3])
        qtd2 = (lista_colunas_s2[1])

        
        for index, row in updated_sheet.iterrows():

            list_qtd2.append(row[qtd2])
            list_cod2.append(row[cod2])

        
    def comparar(self):
        df1 = pd.read_excel(paths[0])
        df2 = pd.read_excel(paths[1])

        df1.reset_index(drop=True, inplace=True)
        df2.reset_index(drop=True, inplace=True)

        coluna_qtd01 = pd.read_excel(paths[0], index_col=None, na_values=['NA'], usecols= [df1.columns.to_list()[0]])
        coluna_cod01 = pd.read_excel(paths[1], index_col=None, na_values=['NA'], usecols= [df1.columns.to_list()[2]])

        coluna_qtd02 = pd.read_excel(paths[0], index_col=None, na_values=['NA'], usecols= [df2.columns.to_list()[0]])
        coluna_cod02 = pd.read_excel(paths[1], index_col=None, na_values=['NA'], usecols= [df2.columns.to_list()[2]])

        planilha_01_two_cols = pd.concat([coluna_qtd01, coluna_cod01], axis=1)
        planilha_02_two_cols = pd.concat([coluna_qtd01, coluna_cod02], axis=1)
    
                        # dá um resultado boolean.
                        # retorna True se for igual, e False se for diferente

                        # Objetivo: transformar esse valor de boolean no valor original novamente
                        # talvez o problema sea q eu to pegando o 'diferentes', eu tenho q pegar o 'i' no np.where

        diferentes = [i for i in planilha_02_two_cols.values ==  planilha_01_two_cols.values]

        # print(planilha_02_two_cols.values[9][1]) # se for mudar só o segundo -> pega só qtd / se mudar só p primeiro pega o cod/ se só dxr um pega os dois
      
        for x in range(len(diferentes)):
            # print(x)
            # print(diferentes[x])
           
            # print(planilha_02_two_cols)

                    # aparentemente dando certo a parte do cdigo
            if diferentes[x][0] == False: # se o codgo for !=
                vlr = planilha_02_two_cols.values[x][0] # to pegando apenas o valor da quantidade
                # print(vlr)
                if vlr != '':
                    vlr = planilha_02_two_cols.values[x]
                    output_qtd.append(vlr)

                    # com erro
            # if diferentes[0][x] == False:
            #     vlr2 = planilha_02_two_cols[0][x]
            #     if vlr2 !='':
            #         vlr2 = planilha_02_two_cols[0][x]
            #         output_cod.append(vlr2)

        df3 = pd.DataFrame(data=output_cod)
        df3.to_excel('data13.xlsx')

        print(type(diferentes))








        # print(diferentes)
        # for x in diferentes:
        #     indie_w_f = np.column_stack(np.where(x[0] == False)) # pegando o indice de quando o valor é falso, ou seja, diferente entre as planilhas
            
        #     output.append(indie_w_f)
        # print(indie_w_f)
        # for y in planilha_02_two_cols:
        #     print(y[indie_w_f])   

        
        # for y in planilha_01_two_cols.values:
        #     print(y[0])

        # print(output_qtd)

        # df3 = pd.DataFrame(data=output_qtd)
        # df3.to_excel('data2.xlsx')


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
sys.exit(app.exec_())