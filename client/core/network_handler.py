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
    def info(self, ctxt, publisher_id, event_type, payload, metadata):
        print 'Received info ...', payload
        LOG.debug('Client handling loop entered')


class ClientsListHandler():
    
    def __init__(self):
        self.endpoints = [ClientsListEndpoint()]
        self.targets = [messaging.Target(topic=cred.CLIENT_TOPIC,
                                         server=cred.CL_ENDPOINT)]
        self.transport = messaging.get_transport(cfg.CONF, url=cred.PUBLISHER_PORT)
        self.server = messaging.get_notification_listener(self.transport,
                                                          self.targets,
                                                          self.endpoints,
                                                          executor='eventlet')

    def stop(self):
        self.server.stop()

    def start(self):
        self.server.start()


class NetworkHandler():
    
    def handle_notifications(self):
        pass
