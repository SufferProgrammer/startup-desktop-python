from PyQt4 import QtCore
from PyQt4 import QtGui
from database import dbcontroller
from design import admin_ui
from controller import controller
import sys
import login

class Admin(QtGui.QMainWindow, admin_ui.Ui_MainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        self.setupUi(self)
        self.controller()

    def controller(self):
        self.pushButton_2.clicked.connect(self.logOut)

    def logOut(self):
        closeConnection = dbcontroller.DBControl()
        closeConnection.connectionClose()
        self.close = login.Login()
        self.close.show()
        self.hide()