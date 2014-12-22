'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import eventlet
import time
import logging

from oslo import messaging
from oslo.config import cfg
from common import cred
from server.core import clients_list

import registrator
import publisher

LOG = logging.getLogger(__name__)


class ClientsListManager(object):

    ''' Manages clients list
    '''

    def __init__(self):
        LOG.debug('ClientsListManager __init__')
        self._transport = messaging.get_transport(cfg.CONF,
                                                  url=cred.REGISTER_PORT)
        self._target = messaging.Target(topic=cred.CLIENT_TOPIC,
                                        server=cred.SERVER)
        self.clients_list = clients_list.ClientsList()
        self.publisher = publisher.Publisher(self.clients_list)
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
        LOG.debug('Starting server ...')
        self.publisher.start()
        self.server.start()