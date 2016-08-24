from PyQt4 import QtCore
from PyQt4 import QtGui
from controller import controller
from database import dbcontroller
from design import forgot_ui
import login
import os

class ForgotPw(QtGui.QWidget, forgot_ui.Ui_Form):
    def __init__(self):
        super(ForgotPw, self).__init__()
        self.setupUi(self)
        self.control()

    def control(self):
        self.pushButton.clicked.connect(self.ForgotPasswd)
        self.pushButton_2.clicked.connect(self.backToLogin)

    def ForgotPasswd(self):
        emailAddr = self.lineEdit.text()
        username = self.lineEdit_2.text()
        if username and emailAddr != '':
            dataGetPasswdWithUnameDetailed = dbcontroller.DBControl()
            dataFetchDBRes = dataGetPasswdWithUnameDetailed.forgetPasswdUserSpecified(str(username), str(emailAddr))
            password = ''.join(dataFetchDBRes)
            mailMessage = "Hai Client, this is from your's apps developer. You have been forgot password and your's password is '%s' for now" %(password)
            emailSendPasswdBot = controller.Controller()
            emailSendPasswdBot.sendMailController(str(emailAddr), mailMessage)

            QtGui.QMessageBox.information(self, 'Success', "Password has been sent to email, please check your's mailbox")
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Email and username is empty')

    def backToLogin(self):
        self.login = login.Login()
        self.login.show()
        self.hide()