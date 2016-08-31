from PyQt4 import QtCore
from PyQt4 import QtGui
from database import dbcontroller
from design.admin import admin_ui
from controller import controller
import login
import reg_min
import sys


class Admin(QtGui.QMainWindow, admin_ui.Ui_MainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        self.setupUi(self)
        self.controller()

    def controller(self):
        self.pushButton_2.clicked.connect(self.logOut)
        self.pushButton.clicked.connect(self.test)
        self.actionExit_3.setStatusTip('Exit admin session')
        self.actionExit_3.triggered.connect(self.exit)
        self.actionAdd_New_User.setStatusTip('Add new user in admin mode')
        self.actionAdd_new_user.triggered.connect(self.makeNewUsr)
        self.tabListViewConfig()
        self.screenControl()

    def logOut(self):
        closeConnection = dbcontroller.DBControl()
        closeConnection.connectionClose()
        self.close = login.Login()
        self.close.show()
        self.hide()

    def makeNewUsr(self):
        self.regist = reg_min.Register()
        self.regist.show()
        self.hide()

    def exit(self):
        closeDBConnection = dbcontroller.DBControl()
        closeDBConnection.connectionClose()
        QtCore.QCoreApplication.instance().quit()

    def tabListViewConfig(self):
        dataGetData = dbcontroller.DBControl()
        resRowFetchRow = dataGetData.adminViewListRow()
        dataServedToListView = dataGetData.adminGetAllData()
        self.tableWidget.setRowCount(len(resRowFetchRow))
        self.tableWidget.setColumnCount(4)
        # self.tableWidget.horizontalHeader().setStretch(True)
        self.tableWidget.setHorizontalHeaderLabels(['Username', 'Password', 'Email', 'user_level'])
        for i, item  in enumerate(dataServedToListView):
            Uname = QtGui.QTableWidgetItem(str(item[1]))
            passwd = QtGui.QTableWidgetItem(str(item[2]))
            email = QtGui.QTableWidgetItem(str(item[3]))
            uLevel = QtGui.QTableWidgetItem(str(item[4]))

            self.tableWidget.setItem(i, 0, Uname)
            self.tableWidget.setItem(i, 1, passwd)
            self.tableWidget.setItem(i, 2, email)
            self.tableWidget.setItem(i, 3, uLevel)

            dataCloseToRefresh = dbcontroller.DBControl()
            dataCloseToRefresh.connectionClose()

        # QtCore.QTimer.singleShot(1000, self.tabListViewConfig)
        # self.tableWidget.selectedItems()

    def screenControl(self):
        setGeometry = self.frameGeometry()
        setWindowsPosition = QtGui.QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(setWindowsPosition)
        self.move(setGeometry.topLeft())

    def test(self):
        for data in enume
        self.tableWidget.removeRow(0)