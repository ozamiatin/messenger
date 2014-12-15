'''
Created on Dec 12, 2014

@author: ozamiatin
'''

import zmq
import threading
from client.core import facade


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
        self._network_handler = NetworkHandler()
        self._controller_thread = threading.Thread(target=self._handling_loop)


    def _handling_loop(self):
        self._ui_handler = UiHandler(self._ui_callback, self.context)
        print 'Client handling loop entered'
        while True:
            print 'waiting ...'
            self._ui_handler.handle_notifications()
            print 'UI notification done.'
            self._network_handler.handle_notifications()
            print 'Network notification done.'


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



class NetworkHandler():
    
    def handle_notifications(self):
        pass



class UiHandler():
    
    def __init__(self, ui_callback, ui_context):
        self.ui_callback = ui_callback
        self.context = ui_context
        self.ui_controller_socket = self.context.socket(zmq.PAIR)
        self.ui_controller_socket.connect(UI_CONTROLLER_SOCKET)

    def handle_notifications(self):
        msg = self.ui_controller_socket.recv_pyobj()        
        print 'Handled UI notification: ', msg