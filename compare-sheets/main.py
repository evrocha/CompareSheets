import sys
import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from openpyxl.utils import *
sheets = []
wblist = []
class MainWindow(QDialog):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        super().__init__()
        
        loadUi("C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets\\compare-sheets\\up_file-screen.ui", self)
        self.browse.clicked.connect(self.browsefile_original)
        self.browse2.clicked.connect(self.browsefile2_original)
        self.comparar_btn.clicked.connect(self.comparar)

    def browsefile_original(self):
        initial_version = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets')
        self.filename.setText(initial_version[0]) 
        file_path = (initial_version[0]) 
        initial_sheet = pd.read_excel(file_path)

        wb = load_workbook(file_path)
        wblist.append(wb)

        sheets.append(initial_sheet)
        print(f"{sheets[0]} INICIAL" )
       



    def browsefile2_original(self):
        update_version = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets')
        self.filename2.setText(update_version[0])
        file_path2 = (update_version[0])
        updated_sheet = pd.read_excel(file_path2)
        sheets.append(updated_sheet)
        print(f"{sheets[1]} FINAL" )
        
    def comparar(self):
        old_sheet = sheets[0]
        upd_sheet = sheets[1]

        wb = wblist[0]
        sh = wb.active
        
# iterando sobre a planilha selecionada
        for i in range(1, sh.max_row+1):
            print("\n")
            print("Row ", i, " data :")
            for j in range(1, sh.max_column + 1):
                cell_obj = sh.cell(row=i, column=j)
                print(cell_obj.value, end=" ")
                
               

        # print(sheets[0].equals(sheets[1]))

        # if (sheets[0].equals(sheets[1])) == True:
        #     print("As planilhas sao iguais")

        # elif(sheets[0].equals(sheets[1])) == False:
        #     compare_values = old_sheet.values == upd_sheet.values
        #     print(f"{compare_values} comparacao")

        #     rows, cols = np.where(compare_values == False)
        #     for item in zip(rows, cols):
        #         old_sheet.iloc[item[0], item[1]] = '{} --> {}'.format(upd_sheet.iloc[item[0], item[1]], upd_sheet.iloc[item[0], item[1]])
        #     old_sheet.to_excel('C:\\Users\\Fiscal\\Documents\\GitHub\\CompareSheets\\output.xlsx', index = False, header = True)

        ######

        
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
sys.exit(app.exec_())
