import sys


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("up_file-screen.ui", self)
        self.browse.clicked.connect(self.browsefile_original)
        self.browse2.clicked.connect(self.browsefile2_original)
    
    def browsefile_original(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\')
        self.filename.setText(file_name[0])
    
    def rowsefile2_original(self):
        file_name2 = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Fiscal\\Desktop\\compare-sheets')
        self.filename2.setText(file_name2[0])

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
sys.exit(app.exec_())
