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
from server.core import clients_list
LOG = logging.getLogger(__name__)


class PublisherProxy(messaging.RPCClient):
    
    def __init__(self, clients_list):
        self.clients_list = clients_list
        transport = messaging.get_transport(cfg.CONF, url=cred.PUBLISHER_PORT)
        target = messaging.Target(topic=cred.CL_ENDPOINT,
                                  server=cred.PUBLISHER_PORT)
        super(PublisherProxy, self).__init__(transport, target)


    def publish(self):
        if self.clients_list.clients:
            ctx = {"application": "oslo.im.server.publisher",
                   "cast": False}
            self.cast(ctx, 'list_updated',
                      **{'clients_list': self.clients_list.clients.values()})
            print 'Clients list published on the network ... sleep for 5 seconds ...'
            LOG.debug('Clients list published on the network ... sleep for 5 seconds ...')
        else:
            print 'Clients list is empty ... sleep for 5 seconds ...'
            LOG.debug('Clients list is empty ... sleep for 5 seconds ...')
        time.sleep(5)
            


class Publisher(Thread):
    
    ''' Manages ClientsList publishing on the network
    '''

    def __init__(self, clients_list):
        self._pub_proxy = PublisherProxy(clients_list)
        self._stop = False
        super(Publisher, self).__init__()


    def stop(self):
        self._stop = True


    def run(self):
        while not self._stop:
            self._pub_proxy.publish()
