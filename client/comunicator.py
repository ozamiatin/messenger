'''
Created on Nov 19, 2014

@author: ozamiatin
'''

import abc
import socket
import threading

import zmq

from common import cred


class Communicator(object):
    """Base client object.

    Provides minimal functionality responsible for network socket
    communication. Requesting server and handling responses.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def send_object(self, msg):
        """Send Python object to server."""
        pass

    @abc.abstractmethod
    def receive_object(self):
        """Receive python object sent from server as response."""
        pass

    @abc.abstractmethod
    def receive_string(self):
        """Receive string (mostly JSON) from server as response."""
        pass

    @abc.abstractmethod
    def get_address(self):
        """Get a binded sockets addresses."""
        pass


class ZeroMqUsersListUpdater(threading.Thread):
    """Client worker."""

    def __init__(self, users_list_view, context):
        super(ZeroMqUsersListUpdater, self).__init__()
        self.users_list_view = users_list_view
        self.context = context
        self.users_list_socket = self.context.socket(zmq.SUB)
        self.users_list_socket.connect(cred.PUBLISHER_PORT)
        self.users_list_socket.setsockopt(zmq.SUBSCRIBE, '')

    def run(self):
        while True:
            print 'Waiting for list publishing ...'
            users_list = self.users_list_socket.recv_pyobj()
            print users_list
            self.users_list_view.clear()
            for user in users_list.values():
                self.users_list_view.add_user(user['name'], user['online'])


class ZeroMqCommunicator(Communicator):

    def __init__(self, port):
        self.messaging_port = port
        self.context = zmq.Context()
        self.server_socket = self.context.socket(zmq.REQ)
        self.server_socket.connect(cred.REGISTER_PORT)

    def send_object(self, msg):
        self.server_socket.send_pyobj(msg)

    def receive_object(self):
        # FIXME: there is no users_list_socket member.
        # TODO: if we need it, where to get it?
        # If we don't need it, we should delete from the parent class.
        return self.users_list_socket.recv_pyobj()

    def receive_string(self):
        return self.server_socket.recv_string()

    def get_address(self):
        tmpl = "tcp://%s:%s"
        return tmpl % (socket.gethostbyname(socket.getfqdn()),
                       self.messaging_port)
