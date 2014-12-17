'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import time


class ClientInfo():
    
    def __init__(self,
                 client_name,
                 reg_time,
                 is_online):
        self.client_name = client_name
        self.reg_time = reg_time
        self.is_online = is_online


    def set_status(self, is_online):
        self.is_online = is_online



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