'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import time

#from common.client_info import ClientInfo 
from common import cred
from oslo.config import cfg
from oslo import messaging
from threading import Thread

import logging
LOG = logging.getLogger(__name__)

class Publisher(Thread):
    
    ''' Manages ClientsList publishing on the network
    '''

    def __init__(self, clients_list):
        self.clients_list = clients_list
        self.transport = messaging.get_transport(cfg.CONF, url=cred.PUBLISHER_PORT)
        self.notifier = messaging.Notifier(transport=self.transport,
                                           publisher_id=cred.CL_ENDPOINT,
                                           topic=cred.CL_ENDPOINT)
        self._stop = False
        super(Publisher, self).__init__()


    def stop(self):
        self._stop = True

    def run(self):
        ctx = {"application": "oslo.im.server",
               "time": time.ctime(),
               "cast": False}

        while not self._stop:
            payload = self.clients_list.clients.values()
            self.notifier.info(ctx, cred.PUBLISHER_EVENT_TYPE, payload)
            print 'Clients list published on the network ... sleep for 5 seconds ...'
            LOG.debug('Clients list published on the network ... sleep for 5 seconds ...')
            time.sleep(5)