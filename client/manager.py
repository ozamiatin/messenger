'''
Created on Nov 20, 2014

@author: ozamiatin
'''

import random
from client.comunicator import ZeroMqCommunicator
from client.comunicator import ZeroMqUsersListUpdater

class CommunicationManager(object):
    
    def __init__(self):
        messaging_port = str(random.randint(5000, 5999))
        self.communicator = ZeroMqCommunicator(messaging_port) 

    def sendHere(self, name):
        self.userName = name
        msg = {"kind": "here",
               "name": name,
               "address": self.communicator.getAddress()}
        self.communicator.sendObject(msg)
        rep = self.communicator.receiveString()
        if (rep != "registered"):
            raise Exception("Not registered!")

    def runListUpdater(self, usersListView):
        self.listUpdater = ZeroMqUsersListUpdater(usersListView,
                                                  self.communicator.context)
        self.listUpdater.start()