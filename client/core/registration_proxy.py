'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import eventlet
import time

from oslo import messaging
from oslo.config import cfg
from common import cred

import logging
LOG = logging.getLogger(__name__)


class RegistrationProxy(messaging.RPCClient):
    
    ''' Interface to a server Registrator entity
    '''

    def __init__(self):
        transport = messaging.get_transport(cfg.CONF,
                                            url=cred.REGISTER_PORT)
        target = messaging.Target(topic=cred.CLIENT_TOPIC,
                                  server=cred.SERVER)
        super(RegistrationProxy, self).__init__(transport, target)


    def register_client(self, client_name):
        ctx = {"application": "oslo.im.client",
               "client_name": client_name,
               "time": time.ctime(),
               "cast": False}
        rep = self.call(ctx, 'on_here', **{'client_name': client_name})
        print 'Here sent, reply: ', rep
        LOG.debug('Here sent, reply: %s', rep)      


    def goodbye_client(self, client_name):
        ctx = {"application": "oslo.im.client",
               "client_name": client_name,
               "time": time.ctime(),
               "cast": False}
        rep = self.call(ctx, 'on_leave', **{'client_name': client_name})
        print 'Goodbye sent, reply: ', rep
        LOG.debug('Goodbye sent, reply: %s', rep)