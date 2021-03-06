from PyQt4 import QtCore
from PyQt4 import QtGui
from database import dbcontroller
from design import login_ui
import register
import admin
import member
import forgot_pw
import os

class Login(QtGui.QWidget, login_ui.Ui_Form):
    def __init__(self):
        super(Login,  self).__init__()
        self.setupUi(self)
        self.control()
        
    def control(self):
        self.pushButton.clicked.connect(self.Login)
        self.pushButton_2.clicked.connect(self.Reg)
        self.pushButton_3.clicked.connect(self.forgotPwd)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText("Enter Username")
        self.lineEdit.setPlaceholderText("Enter password")
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit.setMaxLength(18)

        self.screenControl()

    def Login(self):
        dataUname = self.lineEdit_2.text()
        dataPasswd = self.lineEdit.text()
        if dataUname and dataPasswd != '':
            dataAuth = dbcontroller.DBControl()
            dataUnameAuthRes = dataAuth.loginUnameAuthenticator(dataUname)
            dataPasswdAuthRes = dataAuth.loginPasswdAutenticator(dataPasswd)
            if dataUnameAuthRes != None:
                dataUser = self.lineEdit_2.text()
                os.system('mkdir /tmp/project/')
                dataCreateTempFileUname = open('/tmp/project/user_name.enc', 'w')
                dataCreateTempFileUname.write(dataUser)
                dataCreateTempFileUname.close()
                dataPasswd = self.lineEdit.text()

                dataHookMailAddr = dbcontroller.DBControl()
                data = dataHookMailAddr.hookEmailAddr()
                toText = ''.join(map(str, data))
                emailHookToTemp = open('/tmp/project/user_email.enc', 'w')
                emailHookToTemp.write(toText)
                emailHookToTemp.close()

                if dataPasswdAuthRes != None:
                    dataUserLevelAuth = dbcontroller.DBControl()
                    dataRes = dataUserLevelAuth.userlevelAuthenticator(dataUname, dataPasswd)
                    dataAuthRes = int(''.join(map(str, dataRes)))
                    if dataAuthRes == 1:
                        self.Admin = admin.Admin()
                        self.Admin.show()
                        self.hide()
                    else:
                        self.Member = member.Member()
                        self.Member.show()
                        self.hide()
                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'Invalid username or password')
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'Invalid username or password')
        elif dataPasswd == '':
            QtGui.QMessageBox.critical(self, 'Error', 'Username and password is empty')
        elif dataUname == '':
            QtGui.QMessageBox.critical(self, 'Error', 'Username and password is empty')
        else:
            pass


    def Reg(self):
        self.regFormShow = register.register()
        self.regFormShow.show()
        self.hide()

    def userInfo(self):
        return self.lineEdit_2.text()

    def forgotPwd(self):
        self.ForgotForm = forgot_pw.ForgotPw()
        self.ForgotForm.show()
        self.hide()

    def screenControl(self):
        setGeometry = self.frameGeometry()
        setWindowsPosition = QtGui.QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(setWindowsPosition)
        self.move(setGeometry.topLeft())