from design.admin import register_ui
from validate_email import validate_email
from database import dbcontroller
from PyQt4 import QtCore
from PyQt4 import QtGui
import admin
import sys

class Register(QtGui.QWidget, register_ui.Ui_Form):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.control()

    def control(self):
        self.pushButton.clicked.connect(self.crtUser)
        self.pushButton_2.clicked.connect(self.quitMe)
        self.screenControl()

    def crtUser(self):
        dataWriteInfo = dbcontroller.DBControl()
        uname = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        firstAuth = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        if uname or passwd or passwd or firstAuth or email != '':
            if passwd == firstAuth:
                secondAuth = validate_email(email)
                if secondAuth == True:
                    confirmationUserLevelAdmin = self.radioButton
                    confirmationUserLevelMember = self.radioButton_2
                    if confirmationUserLevelAdmin.isChecked():
                        dataWriteInfo.addUserLevelAdmin(uname, passwd, email)

                        QtGui.QMessageBox.information(self, 'Success', 'User with admin level has added')
                        self.backToMe = admin.Admin()
                        self.backToMe.show()
                        self.hide()

                    elif confirmationUserLevelMember.isChecked():
                        dataWriteInfo.addUser(uname, passwd, email)

                        QtGui.QMessageBox.information(self, 'Success', 'User with member level has added')
                        self.backToAdmin = admin.Admin()
                        self.backToAdmin.show()
                        self.hide()
                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'Email pattern is not valid !!')
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'Password not match')
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Form should not be empty')
    def quitMe(self):
        self.goback = admin.Admin()
        self.goback.show()
        self.hide()

    def screenControl(self):
        setGeometry = self.frameGeometry()
        setWindowsPosition = QtGui.QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(setWindowsPosition)
        self.move(setGeometry.topLeft())