'''
Created on Dec 12, 2014

@author: ozamiatin
'''

import zmq

from client.core import facade
from client.core import network_handler
from client.core import ui_handler
from client.core.registration_proxy import RegistrationProxy

from threading import Thread

import logging
LOG = logging.getLogger(__name__)


class ClientController(Thread):
    '''
    Controller thread manager.
    
    The thread is responsible for coordination
    between the NetworkHandler and the UIHandler and proper
    data model updates.
    '''

    def __init__(self, ui_callback):
        self.context = zmq.Context()
        self.client_facade = facade.ClientFacade(self.context)
        self._ui_callback = ui_callback
        self._network_handler = network_handler.NetworkHandler()
        self._clients_list_handler = network_handler.ClientsListHandler()
        self._registration_proxy = RegistrationProxy()
        self._stop = False
        super(ClientController, self).__init__()

    
    def stop(self):
        self._stop = True


    def run(self):
        '''
        Start the handling thread.
        
        The handling thread is responsible to process messages
        from UI (e.g. send button clicked) and from the network
        (e.g. receive message from another client or notification
        from the server). Calls to update UI if needed.
        Performs all actions indirectly via corresponding handlers.
        '''
        self._ui_handler = ui_handler.UiHandler(self._ui_callback,
                                                self.context,
                                                self._registration_proxy)
        self._clients_list_handler.start()
        
        print 'Client handling loop entered'
        LOG.debug('Client handling loop entered')
        while not self._stop:
            self._ui_handler.handle_notifications()
            self._network_handler.handle_notifications()
