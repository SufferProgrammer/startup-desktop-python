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
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        dataGetUserLevel = dbcontroller.DBControl()
        dataUserLevel = dataGetUserLevel.getUserLevel(username, email)
        catchUserLevel = int(''.join(map(str, dataUserLevel)))
        if catchUserLevel == 2:
            databaseSuspendUser = dbcontroller.DBControl()
            databaseSuspendUser.suspendUser(username, email)
            databaseSuspendUser.connectionClose()
            QtGui.QMessageBox.warning(self, 'Success', "Your's account has been suspended !!")
            self.returnLogin = login.Login()
            self.returnLogin.show()
            self.hide()
        elif catchUserLevel == None:
            QtGui.QMessageBox.critical(self, 'Error', 'Resctricted account !')
            pass

        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Resctricted account !')
            pass

