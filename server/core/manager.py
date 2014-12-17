'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import eventlet
from oslo import messaging
from oslo.config import cfg
from common import cred

import registrator
import publisher
import clients_list



class ClientsListManager(object):

    ''' Manages clients list
    '''

    def __init__(self):
        self.clients_list = clients_list.ClientsList()
        self.registrator = registrator.Registrator(self.clients_list)
        self.publisher = publisher.Publisher()
        self._transport = messaging.get_transport(cfg.CONF,
                                                  url=cred.REGISTER_PORT)
        self._target = messaging.Target(topic='oslo.im.client',
                                        server='oslo.im.server')
        self._endpoints = [self.registrator]
        self.server = messaging.get_rpc_server(self._transport,
                                               self._target,
                                               self._endpoints)


    def run(self):
        print 'Starting server ...'
        self.server.start()