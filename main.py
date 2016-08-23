from PyQt4 import QtCore
from PyQt4 import QtGui
from database import dbcontroller
import register
import login
import sys

class Main(QtGui.QWidget):
    def __init__(self):
        super(Main,  self).__init__()
        self.Login = login.Login()
        self.Login.show()

if __name__=='__main__':
    App = QtGui.QApplication(sys.argv)
    Gui = Main()
    Gui.Login.show()
    sys.exit(App.exec_())
