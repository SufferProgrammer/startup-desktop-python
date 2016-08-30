from PyQt4 import QtCore
from PyQt4 import QtGui
from database import dbcontroller
from design.admin import admin_ui
from controller import controller
import login
import reg_min
import sys


class Admin(QtGui.QMainWindow, admin_ui.Ui_MainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        self.setupUi(self)
        self.controller()

    def controller(self):
        self.pushButton_2.clicked.connect(self.logOut)
        self.actionExit_3.setStatusTip('Exit admin session')
        self.actionExit_3.triggered.connect(self.exit)
        self.actionAdd_New_User.setStatusTip('Add new user in admin mode')
        self.actionAdd_new_user.triggered.connect(self.makeNewUsr)

    def logOut(self):
        closeConnection = dbcontroller.DBControl()
        closeConnection.connectionClose()
        self.close = login.Login()
        self.close.show()
        self.hide()

    def makeNewUsr(self):
        self.regist = reg_min.Register()
        self.regist.show()
        self.hide()

    def exit(self):
        closeDBConnection = dbcontroller.DBControl()
        closeDBConnection.connectionClose()
        QtCore.QCoreApplication.instance().quit()