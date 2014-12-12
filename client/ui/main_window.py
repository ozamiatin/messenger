'''
Created on Nov 14, 2014

@author: ozamiatin
'''

from PyQt4 import QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QTextEdit
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QDialog
from PyQt4.Qt import QPushButton
from client.ui import users_list
import client.manager


class LoginDialog(QDialog):

    def __init__(self, parent):
        super(LoginDialog, self).__init__(parent)
        layout = QHBoxLayout()
        self.loginButton = QPushButton(self)
        self.loginButton.setText("Login")
        self.nameEdit = QLineEdit(self)
        layout.addWidget(self.nameEdit)
        layout.addWidget(self.loginButton)
        self.setLayout(layout)
        self.connect(self.loginButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("accepted()"))


class MainWindow(QMainWindow):

    def __init__(self):        
        super(MainWindow, self).__init__()
        self.init_ui()
        self.communicator = client.manager.CommunicationManager()
        self.loginDialog.open()


    def init_ui(self):
        centralWidget = QWidget(self)
        self.historyBox = QTextEdit(centralWidget)
        self.messageBox = QTextEdit(centralWidget)
        self.sendButton = QPushButton(centralWidget)
        self.sendButton.setText('Send')
        self.sendButton.setMaximumWidth(100)
        self.sendButton.setEnabled(False)
        self.messageBox.setFocus()

        hlayout = QHBoxLayout()
        hlayout.addStretch(200)
        hlayout.addWidget(self.sendButton)

        layout = QVBoxLayout()
        layout.addWidget(self.historyBox)
        layout.addWidget(self.messageBox)
        layout.addItem(hlayout)

        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)
        self.usersListView = users_list(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.usersListView)
        
        self.loginDialog = LoginDialog(self)
       
        self.connect(self.loginDialog, QtCore.SIGNAL("accepted()"), self.onRegisterUser)

        
    def on_register_user(self):
        self.communicator.sendHere(str(self.loginDialog.nameEdit.text()))
        self.loginDialog.close()
        self.communicator.runListUpdater(self.usersListView)