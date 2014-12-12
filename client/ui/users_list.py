'''
Created on Nov 14, 2014

@author: ozamiatin
'''

from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QDockWidget
from PyQt4.QtGui import QListWidgetItem


class UsersList(QDockWidget):

    def __init__(self, parent):
        super(UsersList, self).__init__('Users', parent)
        self.usersList = QListWidget(self)
        self.setWidget(self.usersList)

    def addUser(self, name, online):
        self.usersList.addItem(QListWidgetItem(name))
        
    def clear(self):
        self.usersList.clear()