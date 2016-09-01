from PyQt4 import QtCore
from PyQt4 import QtGui
from controller import controller
from database import dbcontroller
from design import forgot_ui
from validate_email import validate_email
import login

class ForgotPw(QtGui.QWidget, forgot_ui.Ui_Form):
    def __init__(self):
        super(ForgotPw, self).__init__()
        self.setupUi(self)
        self.control()

    def control(self):
        self.pushButton.clicked.connect(self.ForgotPasswd)
        self.pushButton_2.clicked.connect(self.backToLogin)
        self.screenControl()

    def ForgotPasswd(self):
        emailAddr = self.lineEdit.text()
        username = self.lineEdit_2.text()
        validateMail = validate_email(emailAddr)
        if validateMail == True:
            if username and emailAddr != '':
                dataGetPasswdWithUnameDetailed = dbcontroller.DBControl()
                dataFetchDBRes = dataGetPasswdWithUnameDetailed.forgetPasswdUserSpecified(str(username), str(emailAddr))
                if dataFetchDBRes != None:
                    passwd = ''.join(dataFetchDBRes)
                    emailSendPasswdBot = controller.Controller()
                    emailSendPasswdBot.sendMailController(str(emailAddr), passwd)

                    QtGui.QMessageBox.information(self, 'Success', "Password has been sent to email, please check your's mailbox")

                    self.login = login.Login()
                    self.login.show()
                    self.hide()
                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'Invalid email or username')
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'Email and username is empty')
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Email pattern is invalid !!')

    def backToLogin(self):
        self.login = login.Login()
        self.login.show()
        self.hide()

    def screenControl(self):
        setGeometry = self.frameGeometry()
        setWindowsPosition = QtGui.QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(setWindowsPosition)
        self.move(setGeometry.topLeft())