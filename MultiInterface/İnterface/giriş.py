import sys
from PyQt5.QtWidgets import *
from giriş_python import Ui_Form
from anaekran import AnaEkran

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.qui= Ui_Form() #always working this two code block
        self.qui.setupUi(self)
        self.anaekranqui = AnaEkran()
        self.name = "yunus emre" #example
        self.password = "yunus123"
        self.hak = 3
        # called

        self.qui.pushButton.clicked.connect(self.giris)



    def giris(self):

        if(self.qui.lineEdit.text() ==self.name  and self.qui.lineEdit_2.text() == self.password):

            print("Login is succesfully")
            self.hide()  #goals became so interface closed
            self.anaekranqui.show()


        else:
            self.hak-=1
            print("Try Again!!!!")
            if(self.hak ==0):
                print("You have entered too many incorrect entries, the process is being terminated. Have a nice day")
                self.close()
