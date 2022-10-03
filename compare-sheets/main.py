
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys;
import pandas as pd

sheet1 = []
sheet2 = []
wblist = []
paths = []
list_qtd = []
list_cod = []
list_qtd2 = []
list_cod2 = []
output_cod = ['', '']
output_qtd = []
#                                                 --- PANDAS VERSION
class MainWindow(QDialog):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        super().__init__()
        
        loadUi("C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets\\compare-sheets\\up_file-screen.ui", self)
        self.browse.clicked.connect(self.get_first_sheet)
        self.browse2.clicked.connect(self.get_sec_sheet)
        self.comparar_btn.clicked.connect(self.comparar)

    def get_first_sheet(self):
        get_version_old = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets\\compare-sheets')         # pega o arquivo
        self.filename.setText(get_version_old[0])  
        file_path = (get_version_old[0]) # caminho 

        paths.append(file_path)

        initial_sheet = pd.read_excel(file_path) 
        sheet1.append(initial_sheet)

        planilha01 = pd.read_excel(file_path)
        planilha01 = planilha01.reset_index()
        
        lista_colunas_s1 = planilha01.columns.tolist()

        cod1 = (lista_colunas_s1[3]) # codigo
        qtd1 = (lista_colunas_s1[1]) # quantidade
        
        for index, row in planilha01.iterrows():
            list_qtd.append(row[qtd1])
            list_cod.append(row[cod1])

    def get_sec_sheet(self):
        get_version_new = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets\\compare-sheets') # pega o arquivo
        self.filename2.setText(get_version_new[0])
        file_path2 = (get_version_new[0])
        paths.append(file_path2)
        updated_sheet = pd.read_excel(file_path2)
        sheet2.append(updated_sheet)
        planilha02 = pd.read_excel(file_path2)
        planilha02 = planilha02.reset_index()
        lista_colunas_s2 = planilha02.columns.to_list()
        cod2 = (lista_colunas_s2[3])
        qtd2 = (lista_colunas_s2[1])

        for index, row in planilha02.iterrows():
            list_qtd2.append(row[qtd2])
            list_cod2.append(row[cod2])
        
    def comparar(self):
        
        # for cod in list_cod:
        #     if cod in list_cod2:
        #         # if cod in sheet1:
        #         print(f"{cod} - - - - -Ele é igual")
        #     else:
        #         print("Ele nao é igual")
        #         #     output.append(sheet1[])
        #         output.append(cod)

# vendo qual das duas planilhas é maior, para se ter como  base no for

    # comparando estritamente a questao do codigo das planilhas
        if len(sheet1[0]) > len(sheet2[0]):
            for cod in list_cod:
                if cod in list_cod2:
                    print(f"{cod} - - - - -Ele é igual")
                else:
                    print("Ele nao é igual")
    # comparando estritamente a quantidade 
            for qtd in list_qtd:
                if qtd in list_qtd:
                    print(f"{qtd}  - - - - -É igual")
                else:
                    print(f"{qtd}  - - - - -NAO É IGUAL")

        # comparando estritamente a questao do codigo das planilhas
        elif len(sheet2[0]) > len(sheet1[0]):
            for cod2 in list_cod2:
                if cod2 in list_cod:
                    print(f"{cod2} - - - - --  É IGUAL")
                    output[0].append
                else:
                    print(f"{cod2} - - - - --  NAO É igual")

    # comparando estritamente a quantidade         
            for qtd2 in list_qtd:
                if qtd2 in list_qtd:
                    print(f"{qtd2}  - - - - -É igual")
                else:
                    print(f"{qtd2}  - - - - -NAO É IGUAL")
        print(len(sheet2[0]))
        print(len(sheet1[0]))

            # for y in list_qtd2:
            #     if i == y:
            #         print(f"{i} é igual a {y} - -- -São iguais")
            #     else:
            #         print(f"{i} NAO é igual a {y} - -- - NAO São iguais")
        print("Saiu do loop")
       
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
sys.exit(app.exec_())
