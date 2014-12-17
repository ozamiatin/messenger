'''
Created on Dec 17, 2014

@author: ozamiatin
'''

import zmq
import time

from client.core import controller
from client.core import registration_proxy


class UiHandler():
    
    def __init__(self,
                 ui_callback,
                 ui_context,
                 reg_proxy):
        self.ui_callback = ui_callback
        self.context = ui_context
        self.ui_controller_socket = self.context.socket(zmq.PAIR)
        self.ui_controller_socket.connect(controller.UI_CONTROLLER_SOCKET)
        self.reg_proxy = reg_proxy
        self._handlers = {'login': self.login,
                          'send_msg': self.send_msg}


    def login(self, client_name):
        self.reg_proxy.register_client(client_name)


    def logout(self, client_name):
        self.reg_proxy.goodbye_client(client_name)
    
    
    def send_msg(self, message):
        pass
        

    def handle_notifications(self):
        try:
            msg = self.ui_controller_socket.recv_pyobj(flags=zmq.NOBLOCK)
            print 'Handled UI notification: ', msg
            self._handlers[msg['msg']](msg['data'])
        except zmq.Again:
            time.sleep(0.01)