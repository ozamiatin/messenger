'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import time
from common.client_info import ClientInfo 

import logging
LOG = logging.getLogger(__name__)

class ClientsList():

    def __init__(self):
        self.clients = {}


    def add_client(self, client_name):
        print 'Adding client server side: %s', client_name
        LOG.debug('Adding client server side: %s', client_name)
        self.clients[client_name] = ClientInfo(client_name,
                                               time.clock(),
                                               True)


    def goodbye_client(self, client_name):
        print 'Removing client server side: %s', client_name
        LOG.debug('Removing client server side: %s', client_name)
        self.clients[client_name].set_status(False)


    def dump_list(self):
        for client in self.clients.values():
            print 'name: %s, status: %s', client.client_name, client.is_online
            LOG.debug('name: %s, status: %s', client.client_name, client.is_online)