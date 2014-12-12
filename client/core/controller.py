'''
Created on Dec 12, 2014

@author: ozamiatin
'''

import zmq
from client.core import facade


UI_CONTROLLER_SOCKET = 'inproc://ui_controller'


class ClientController():
    '''
    Controller thread manager.
    
    The thread is responsible for coordination
    between the NetworkHandler and the UIHandler and proper
    data model updates.
    '''

    def __init__(self):
        self.ui_facade = facade.ClientFacade()
        self.ui_callback = facade.UiCallback()
        self.ui_handler = UiHandler(self.ui_callback)
        self.network_handler = NetworkHandler()


    '''
    Start the handling thread.
    
    The handling thread is responsible to process messages
    from UI (e.g. send button clicked) and from the network
    (e.g. receive message from another client or notification
    from the server). Calls to update UI if needed.
    Performs all actions indirectly via corresponding handlers.
    '''
    def run(self):
        pass


class NetworkHandler():
    pass



class UiHandler():
    
    def __init__(self, ui_callback):
        self.ui_callback = ui_callback
        self.context = zmq.Context()        
        self.ui_controller_socket = self.context.socket(zmq.PAIR)
        self.ui_controller_socket.connect(UI_CONTROLLER_SOCKET)