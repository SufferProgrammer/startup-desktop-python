from PyQt4 import QtCore
from PyQt4 import QtGui
from design import member_ui
from database import dbcontroller
import confirm_suspend
import login
import forgot_pw
import edit
import os


class Member(QtGui.QMainWindow, member_ui.Ui_MainWindow):
    def __init__(self):
        super(Member, self).__init__()
        self.setupUi(self)
        self.controller()

    def controller(self):
        self.pushButton.clicked.connect(self.logOut)
        self.actionForgot_Password.triggered.connect(self.ForgotPasswd)
        self.actionForgot_Password.setStatusTip('I forgot my password')
        self.actionExit.triggered.connect(self.exit)
        self.actionExit.setStatusTip('Exit application')
        self.actionEdit_My_Profile.triggered.connect(self.editProfile)
        self.actionEdit_My_Profile.setStatusTip('Edit my Profile')
        self.actionSuspend_My_Account.triggered.connect(self.suspendMe)
        self.actionSuspend_My_Account.setStatusTip('Suspend my account')
        self.screenControl()

        getTempEmail = open('/tmp/project/user_email.enc', 'r')
        email = getTempEmail.read()
        getTempUname = open('/tmp/project/user_name.enc', 'r')
        Uname = getTempUname.read()
        self.Username.setText(str(Uname))
        self.Email.setText(str(email))

    def ForgotPasswd(self):
        self.Forgot = forgot_pw.ForgotPw()
        self.Forgot.show()
        self.hide()

    def suspendMe(self):
        databaseOperation = dbcontroller.DBControl()
        databaseOperation.suspendUser()
        databaseOperation.connectionClose()

        QtGui.QMessageBox.warning(self, 'Success', "Your's account has been suspended")
        self.goLogin = login.Login()
        self.goLogin.show()
        self.hide()

    def exit(self):
        os.system('rm -r /tmp/project')
        dbClose = dbcontroller.DBControl()
        dbClose.connectionClose()
        QtCore.QCoreApplication.instance().quit()

    def editProfile(self):
        self.editProfile = edit.Edit()
        self.editProfile.show()
        self.hide()

    def logOut(self):
        os.system('rm -r /tmp/project')
        disconnectDB = dbcontroller.DBControl()
        disconnectDB.connectionClose()
        self.logout = login.Login()
        self.logout.show()
        self.hide()

    def screenControl(self):
        setGeometry = self.frameGeometry()
        setWindowsPosition = QtGui.QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(setWindowsPosition)
        self.move(setGeometry.topLeft())