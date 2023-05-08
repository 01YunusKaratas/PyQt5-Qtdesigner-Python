import sys
from PyQt5.QtWidgets import *
from giriş import Login
from anaekran import Ui_MainWindow
from eklenenler import Eklenenler
app = QApplication(sys.argv)

logins = Login()
logins.show()
sys.exit(app.exec_())