import sys
from PyQt5.QtWidgets import *
from eklenenler_python import Ui_Form

class Eklenenler(QWidget):

    def __init__(self):
        super().__init__()
        self.eklenenqui = Ui_Form()
        self.eklenenqui.setupUi(self)

        self.eklenen_degerler = []

    def ekle(self, deger, deger1, deger2):
        self.eklenen_degerler.append((deger, deger1, deger2))  # Değeri eklenenler listesine ekle
        self.goster()

    def goster(self):
        self.eklenenqui.listWidget.clear()  # Listeyi temizle
        for deger in self.eklenen_degerler:
            self.eklenenqui.listWidget.addItem(f"Name: {deger[0]}, Amount: {deger[1]}, Comment: {deger[2]}")



    def Yazdır(self):
        for i in self.eklenen_degerler:
            print(i)





