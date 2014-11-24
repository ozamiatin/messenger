'''
Created on Nov 19, 2014

@author: ozamiatin
'''

import zmq
import socket
from common import cred
import threading
import time

class Communicator(object):
    
    def sendObject(self, msg):
        pass
    
    def receiveObject(self):
        pass

    def receiveString(self):
        pass

    def getAddress(self):
        pass


class ZeroMqUsersListUpdater(threading.Thread):
    
    def __init__(self, usersListView, context):
        super(ZeroMqUsersListUpdater, self).__init__()
        self.usersListView = usersListView
        self.context = context
        self.users_list_socket = self.context.socket(zmq.SUB)
        self.users_list_socket.connect(cred.PUBLISHER_PORT)
        self.users_list_socket.setsockopt(zmq.SUBSCRIBE, '')        

    def run(self):
        while True:
            print 'Waiting for list publishing ...'
            usersList = self.users_list_socket.recv_pyobj()
            print usersList
            self.usersListView.clear()
            for name in usersList.keys():
                print name
                self.usersListView.addUser(usersList[name]['name'],
                                           usersList[name]['online'])


class ZeroMqCommunicator(Communicator):

    def __init__(self, port):
        self.messaging_port = port
        self.context = zmq.Context()
        self.server_socket = self.context.socket(zmq.REQ)
        self.server_socket.connect(cred.REGISTER_PORT)

    def sendObject(self, msg):
        self.server_socket.send_pyobj(msg)
        
    def receiveObject(self):
        return self.users_list_socket.recv_pyobj()

    def receiveString(self):
        return self.server_socket.recv_string()

    def getAddress(self):
        return "tcp://" + socket.gethostbyname(socket.getfqdn()) + ":" + self.messaging_port