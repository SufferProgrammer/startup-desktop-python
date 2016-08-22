from design import register_ui
from database import dbcontroller
from PyQt4 import QtGui
from PyQt4 import QtCore
from validate_email import validate_email
import login
import sys

class register(QtGui.QWidget,  register_ui.Ui_Form):
    def __init__(self):
        super(register, self).__init__()
        self.setupUi(self)
        self.control()
        
    def control(self):
        self.pushButton.clicked.connect(self.Register)
        self.pushButton_2.clicked.connect(self.cancelAct)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setPlaceholderText("Enter Your's Username")
        self.lineEdit_2.setPlaceholderText("Enter Your's Password")
        self.lineEdit_3.setPlaceholderText("Enter Your's Email")
        
        self.lineEdit.setMaxLength(12)
        self.lineEdit_2.setMaxLength(18)
        self.lineEdit_3.setMaxLength(30)
        
    def Register(self):
        dataValidationUsername = self.lineEdit.text()
        if str(dataValidationUsername) != '':
            dataValidationPasswd = self.lineEdit_2.text()
            if str(dataValidationPasswd) != '':
                dataValidationEmail = validate_email(self.lineEdit_3.text())
                if dataValidationEmail == True:
                    dataGetUname = self.lineEdit.text()
                    dataGetPasswd = self.lineEdit_2.text()
                    dataGetMail = self.lineEdit_3.text()
                    dataAddUser = dbcontroller.DBControl()
                    dataAddUser.addUser(dataGetUname, dataGetPasswd,  dataGetMail)
                    QtGui.QMessageBox.information(self, 'success', 'username has been created')
                    
                    self.backLogin = login.Login()
                    self.backLogin.show()
                    self.backLogin.pushButton_2.setEnabled(False)
                    self.backLogin.pushButton_2.setToolTip('Register is only can be do once. You should login first')
                    self.hide()
                else:
                    QtGui.QMessageBox.warning(self, 'Warning',  'Username, Password, and Email is empty\nor email Pattern is incorrect')
                    pass
            else:
                QtGui.QMessageBox.warning(self, 'Warning',  'Username, Password, and Email is empty\nor email Pattern is incorrect')
                pass
        else:
            QtGui.QMessageBox.warning(self,  'Warning',  'Username, Password, and Email is empty\nor email Pattern is incorrect')
            pass
            
    def cancelAct(self):
        self.backMain = login.Login()
        self.backMain.show()
        self.hide()
