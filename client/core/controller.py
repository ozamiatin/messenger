'''
Created on Dec 12, 2014

@author: ozamiatin
'''

import zmq
import traceback
import time

from client.core import facade
from client.core import network_handler
from client.core import registration_proxy
from client.core import ui_handler

from threading import Thread

UI_CONTROLLER_SOCKET = 'inproc://ui_controller'


class ClientController():
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
        self._registration_proxy = registration_proxy.RegistrationProxy()
        self._controller_thread = Thread(target=self._handling_loop)


    def _handling_loop(self):
        self._ui_handler = ui_handler.UiHandler(self._ui_callback,
                                                self.context,
                                                self._registration_proxy)
        print 'Client handling loop entered'
        while True:
            self._ui_handler.handle_notifications()
            self._network_handler.handle_notifications()


    '''
    Start the handling thread.
    
    The handling thread is responsible to process messages
    from UI (e.g. send button clicked) and from the network
    (e.g. receive message from another client or notification
    from the server). Calls to update UI if needed.
    Performs all actions indirectly via corresponding handlers.
    '''
    def run(self):
        if not self._controller_thread.is_alive():
            self._controller_thread.start()