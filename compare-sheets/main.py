import sys
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        super().__init__()
        

        loadUi("D:\\Programação\\CompareSheets\\compare-sheets\\up_file-screen.ui", self)
        self.browse.clicked.connect(self.browsefile_original)
        self.browse2.clicked.connect(self.browsefile2_original)

    def browsefile_original(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\Programação\\CompareSheets\\compare-sheets')
        self.filename.setText(file_name[0]) 
        file_path = (file_name[0]) 
        
        wb = load_workbook(file_path) #area d  trabalho
        ws = wb.active#planilhas
       
        for row in range(1, 7):
            for col in range(1,6):
                char = get_column_letter(col)
                print(ws[char + str(row).value])


    def browsefile2_original(self):
        file_name2 = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Downloads')
        self.filename2.setText(file_name2[0])
        file_path2 = (file_name2[0])
    # def teste():
    #     print(arquivo)
    # teste()
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
sys.exit(app.exec_())
