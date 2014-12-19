'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import time
from common.client_info import ClientInfo 

class ClientsList():

    def __init__(self):
        self.clients = {}


    def add_client(self, client_name):
        print 'Adding client server side: ', client_name
        self.clients[client_name] = ClientInfo(client_name,
                                               time.clock(),
                                               True)


    def goodbye_client(self, client_name):
        print 'Removing client server side: ', client_name
        self.clients[client_name].set_status(False)


    def dump_list(self):
        for client in self.clients.values():
            print 'name: ', client.client_name, 'status: ', client.is_online