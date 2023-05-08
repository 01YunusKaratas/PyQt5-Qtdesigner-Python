import sys
from PyQt5.QtWidgets import *
from anaekran_python import Ui_MainWindow
from eklenenler import Eklenenler

class AnaEkran(QMainWindow):

    def __init__(self):
        super().__init__()
        self.anaqui = Ui_MainWindow() #always use two code block
        self.anaqui.setupUi(self)
        self.eklenenqui = Eklenenler()

        self.anaqui.actionShow_Products.triggered.connect(self.Goster)
        self.anaqui.pushButton.clicked.connect(self.Bilgi)


    def Goster(self):
        self.eklenenqui.show()

    def Bilgi(self):
        self.amount = self.anaqui.lineEdit.text()
        self.name = self.anaqui.lineEdit_2.text()
        self.comment  =self.anaqui.textEdit.toPlainText()  #toPlainText methodu  text edit içeriğini almamızı sağlar

        self.eklenenqui.ekle(self.name,self.amount,self.comment)
































