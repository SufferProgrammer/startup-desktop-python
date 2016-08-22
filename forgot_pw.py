from PyQt4 import QtCore
from PyQt4 import QtGui
from controller import controller
from database import dbcontroller
from design import forgot_ui

class ForgotPw(QtGui.QWidget, forgot_ui.Ui_Form):
    def __init__(self):
        super(ForgotPw, self).__init__()
        self.setupUi(self)