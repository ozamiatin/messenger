'''
Created on Dec 17, 2014

@author: ozamiatin
'''

from server.core import clients_list


class Registrator(object):

    ''' Performs network client registration
    
    Oslo messenger server endpoint for clients registration.
    '''

    def __init__(self, clients_list):
        self.clients_list = clients_list


    def on_here(self, client_name):
        print 'On here server side: ', client_name
        self.clients_list.add_client(client_name)


    def on_leave(self, client_name):
        print 'Client leaves server side: ', client_name
        self.clients_list.goodbye_client(client_name)