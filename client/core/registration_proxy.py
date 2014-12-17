'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import eventlet
from oslo import messaging


class RegistrationProxy(messaging.RPCClient):
    
    ''' Interface to a server Registrator entity
    '''

    def __init__(self, context):
        self.context = context


    def register_client(self, client_name):
        rep = self.call(self.context, 'on_here', client_name)
        print 'Here sent, reply: ', rep


    def goodbye_client(self, client_name):
        rep = self.call(self.context, 'on_leave', client_name)
        print 'Goodbye sent, reply: ', rep