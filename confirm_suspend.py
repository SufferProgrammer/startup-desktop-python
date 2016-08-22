from PyQt4 import QtGui
from PyQt4 import QtCore
from design import confirm_ui
from database import dbcontroller
import login
import member


class Confirm(QtGui.QWidget, confirm_ui.Ui_Form):
    def __init__(self):
        super(Confirm, self).__init__()
        self.setupUi(self)
        self.control()

    def control(self):
        self.pushButton.clicked.connect(self.suspend)
        self.pushButton_2.clicked.connect(self.goback)

    def goback(self):
        self.home = member.Member()
        self.home.show()
        self.hide()

    def suspend(self):
        databaseSuspendUser = dbcontroller.DBControl()
        username = self.lineEdit.text()
        databaseSuspendUser.suspendUser(username)
        databaseSuspendUser.connectionClose()
        self.returnLogin = login.Login()
        self.returnLogin.show()
        self.hide()

