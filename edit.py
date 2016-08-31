from PyQt4 import QtGui
from PyQt4 import QtCore
from database import dbcontroller
from design import editProf_ui
from validate_email import validate_email
import member
import admin
import login

class Edit(QtGui.QWidget, editProf_ui.Ui_Form):
    def __init__(self):
        super(Edit, self).__init__()
        self.setupUi(self)
        self.control()

    def control(self):
        self.pushButton_2.clicked.connect(self.EditmyProfile)
        self.pushButton.clicked.connect(self.cancelAndBack)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        self.screenControl()

    def EditmyProfile(self):
        dataChange = dbcontroller.DBControl()
        dataUname = self.lineEdit.text()
        dataPasswd = self.lineEdit_2.text()
        dataPasswdConfirmPasswd = self.lineEdit_3.text()
        dataEmail = self.lineEdit_4.text()
        dataEmailValidation = validate_email(dataEmail)
        if dataUname and dataPasswd and dataPasswdConfirmPasswd and dataEmail != '':
            if dataPasswd == dataPasswdConfirmPasswd:
                if dataEmailValidation == True:
                    dbToolsChangeData = dbcontroller.DBControl()
                    dbToolsChangeData.ChangeUserStatus(dataUname, dataPasswd, dataEmail)
                    QtGui.QMessageBox.information(self, 'Success', 'Change has been save !!')
                    self.Back = login.Login()
                    self.Back.show()
                    self.hide()

                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'Email address is invalid')
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'Password do not match !!')
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'You must fill all form !!')

    def cancelAndBack(self):
        self.backToMain = member.Member()
        self.backToMain.show()
        self.hide()


    def screenControl(self):
        setGeometry = self.frameGeometry()
        setWindowsPosition = QtGui.QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(setWindowsPosition)
        self.move(setGeometry.topLeft())