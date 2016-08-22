# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Member_Form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 531)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName(_fromUtf8("menuAction"))
        self.menuAdvanced = QtGui.QMenu(self.menuAction)
        self.menuAdvanced.setObjectName(_fromUtf8("menuAdvanced"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionForgot_Password = QtGui.QAction(MainWindow)
        self.actionForgot_Password.setObjectName(_fromUtf8("actionForgot_Password"))
        self.actionSee_My_Profile = QtGui.QAction(MainWindow)
        self.actionSee_My_Profile.setObjectName(_fromUtf8("actionSee_My_Profile"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSuspend_My_Account = QtGui.QAction(MainWindow)
        self.actionSuspend_My_Account.setObjectName(_fromUtf8("actionSuspend_My_Account"))
        self.actionEdit_My_Profile = QtGui.QAction(MainWindow)
        self.actionEdit_My_Profile.setObjectName(_fromUtf8("actionEdit_My_Profile"))
        self.menuAdvanced.addAction(self.actionEdit_My_Profile)
        self.menuAdvanced.addSeparator()
        self.menuAdvanced.addAction(self.actionSuspend_My_Account)
        self.menuAction.addAction(self.actionForgot_Password)
        self.menuAction.addAction(self.actionSee_My_Profile)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.menuAdvanced.menuAction())
        self.menuAction.addAction(self.actionExit)
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Member", None))
        self.label.setText(_translate("MainWindow", "Welcome", None))
        self.label_2.setText(_translate("MainWindow", "Member", None))
        self.pushButton.setText(_translate("MainWindow", "Logout", None))
        self.menuAction.setTitle(_translate("MainWindow", "Action", None))
        self.menuAdvanced.setTitle(_translate("MainWindow", "Advanced", None))
        self.actionForgot_Password.setText(_translate("MainWindow", "Forgot Password", None))
        self.actionSee_My_Profile.setText(_translate("MainWindow", "See My Profile", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSuspend_My_Account.setText(_translate("MainWindow", "Suspend My Account", None))
        self.actionEdit_My_Profile.setText(_translate("MainWindow", "Edit My Profile", None))

