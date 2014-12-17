'''
Created on Dec 12, 2014

@author: ozamiatin
'''

import zmq
from client.core import ui_handler


class ClientFacade():
    '''
    Responsible to provide messages to the controller thread.
    Each method of the facade performs call to the controller thread
    via zmq message interface. This kind of inter-threading communication
    was chosen for the sake of synchronization and to avoid standard
    mess with synchronization primitives like mutexes and others.  
    '''

    def __init__(self, ui_context):
        self.context = ui_context
        self.controller_socket = self.context.socket(zmq.PAIR)
        self.controller_socket.bind(ui_handler.UI_CONTROLLER_SOCKET)


    def login_click(self, client_name):
        self.controller_socket.send_pyobj({"msg": "login",
                                           "data": client_name})


    def send_msg_click(self, message):
        pass



class UiCallback():
    '''
    Reads messages from the controller thread communication interface.
    Should be updated in UI main thread events loop.
    '''
    
    def __init__(self, main_window):
        self.main_window = main_window


    def update_clients(self, clients_list):
        pass


    def update_history(self, message):
        pass