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
        print ('Received info ... %s', payload)
        LOG.debug('Received PUBLISHED LIST! %s', payload)


class ClientsListHandler():
    
    def __init__(self):
        endpoints = [ClientsListEndpoint()]
        targets = [messaging.Target(topic=cred.CL_ENDPOINT,
                                    server=cred.CL_ENDPOINT)]
        self.transport = messaging.get_transport(cfg.CONF, url=cred.PUBLISHER_PORT)
        self.server = messaging.get_notification_listener(self.transport,
                                                          targets,
                                                          endpoints,
                                                          executor='eventlet',
                                                          pool='listener-workers')

    def stop(self):
        self.server.stop()

    def start(self):
        self.server.start()


class NetworkHandler():
    
    def handle_notifications(self):
        pass
