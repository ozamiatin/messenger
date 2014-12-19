'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import eventlet
import time

from oslo import messaging
from oslo.config import cfg
from common import cred

import registrator
import publisher
from server.core import clients_list



class ClientsListManager(object):

    ''' Manages clients list
    '''

    def __init__(self):
        self._transport = messaging.get_transport(cfg.CONF,
                                                  url=cred.REGISTER_PORT)
        self._target = messaging.Target(topic=cred.CLIENT_TOPIC,
                                        server=cred.SERVER)
        self.clients_list = clients_list.ClientsList()
        self.publisher = publisher.Publisher(self._transport,
                                             self.clients_list)
        self.registrator = registrator.Registrator(self.clients_list)
        self._endpoints = [self.registrator]
        self.server = messaging.get_rpc_server(self._transport,
                                               self._target,
                                               self._endpoints)

    def stop(self):
        self.publisher.stop()
        self.server.stop()


    def run(self):
        print 'Starting server ...'
        self.publisher.start()
        self.server.start()