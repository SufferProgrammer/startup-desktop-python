from PyQt4 import QtGui
from database import dbcontroller
from design.admin import confirm_ui
import admin

class Confirm(QtGui.QWidget, confirm_ui.Ui_Form):
    def __init__(self):
        super(Confirm, self).__init__()
        self.setupUi(self)
        self.control()

    def control(self):
        self.pushButton.clicked.connect(self.suspend)
        self.pushButton_2.clicked.connect(self.goback)
        self.screenControl()

    def goback(self):
        self.hide()

    def suspend(self):
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        if username and email != '':
            dataGetUserLevel = dbcontroller.DBControl()
            dataUserLevel = dataGetUserLevel.getUserLevel(username, email)
            if dataUserLevel != None:
                catchUserLevel = int(''.join(map(str, dataUserLevel)))
                if catchUserLevel == 2:
                    databaseSuspendUser = dbcontroller.DBControl()
                    databaseSuspendUser.adminDelete(username, email)
                    QtGui.QMessageBox.warning(self, 'Success', "Account has been suspended !!")

                elif catchUserLevel == None:
                    QtGui.QMessageBox.critical(self, 'Error', 'Resctricted account !')
                    pass

                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'Resctricted account !')
                    pass
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'Invalid email or username')
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Email and username is empty')

    def screenControl(self):
        setGeometry = self.frameGeometry()
        setWindowsPosition = QtGui.QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(setWindowsPosition)
        self.move(setGeometry.topLeft())