'''
Created on Dec 17, 2014

@author: ozamiatin
'''

from server.core import clients_list

import logging
LOG = logging.getLogger(__name__)


class Registrator(object):

    ''' Performs network client registration
    
    Oslo messenger server endpoint for clients registration.
    '''

    def __init__(self, clients_list):
        self.clients_list = clients_list


    def on_here(self, *args, **kwargs):
        client_name = kwargs.get('client_name', None)
        print 'On here server side: %s' % client_name
        LOG.debug('On here server side: %s' % client_name)
        self.clients_list.add_client(client_name)
        self.clients_list.dump_list()


    def on_leave(self, *args, **kwargs):
        client_name = kwargs.get('client_name', None)
        print 'Client leaves server side: %s', client_name
        LOG.debug('Client leaves server side: %s', client_name)
        self.clients_list.goodbye_client(client_name)
        self.clients_list.dump_list()