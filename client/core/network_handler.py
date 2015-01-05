'''
Created on Dec 17, 2014

@author: ozamiatin
'''

from oslo.config import cfg
from oslo import messaging

from common import cred

import logging
LOG = logging.getLogger(__name__)


class ClientsListEndpoint(object):
    
    def list_updated(self, *args, **kwargs):
        print ('Updated clients list being received!')
        LOG.debug('Updated clients list being received!')


class ClientsListHandler():
    
    def __init__(self):
        endpoints = [ClientsListEndpoint()]
        target = messaging.Target(topic=cred.CL_ENDPOINT,
                                  server=cred.PUBLISHER_PORT)
        self.transport = messaging.get_transport(cfg.CONF, url=cred.PUBLISHER_PORT)
        self.server = messaging.get_rpc_server(self.transport,
                                               target,
                                               endpoints)

    def stop(self):
        self.server.stop()

    def start(self):
        self.server.start()