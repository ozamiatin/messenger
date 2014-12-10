'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import threading
import time
import zmq

from common import cred


INPROC_NOTIFY_SOCKET = "inproc://publisher"


class User(object):

    def __init__(self, name, address, timestamp):
        self.name = name
        self.address = address
        self.timestamp = timestamp
        self.online = False


# TODO: inherit from UserDict and override __setitem__
class UsersList(object):
    """User instances collection."""

    def __init__(self):
        self.users = {}

    def register_user(self, name, address):
        user = None
        if self.users.has_key(name):
            user = self.users[name]
        else:
            self.users[name] = User(name, address, time.time())
        user.online = True

    def user_offline(self, name):
        if self.users.has_key(name):
            raise Exception("Unregistered user!")
        self.users[name].online = False

    def print_users(self):
        print(self.users)


class ListUpdater(threading.Thread):
    """Server side handler."""

    def __init__(self, users_list, context):
        super(ListUpdater, self).__init__()
        self.users = users_list
        self.context = context

    def run(self):
        reg_socket = self.context.socket(zmq.PAIR)
        reg_socket.connect(INPROC_NOTIFY_SOCKET)
        while True:
            new_user = reg_socket.recv_pyobj()
            if new_user['online']:
                print 'LIST_UPDATER: new user comes ', new_user
                self.users.register_user(new_user['name'], '')
            else:
                self.users.user_offline(new_user['name'])

        reg_socket.close()


class Publisher(threading.Thread):
    """Send messages to registered clients."""

    def __init__(self, context):
        super(Publisher, self).__init__()
        self.users = UsersList()
        self.context = context

    def create_list_pack(self):
        pack = {}
        for user in self.users.users.values():
            pack[user.name] = {'name': user.name, 'online': user.online}
        return pack

    def run(self):
        updater = ListUpdater(self.users, self.context)
        updater.start()
        pub_socket = self.context.socket(zmq.PUB)
        pub_socket.bind(cred.PUBLISHER_PORT)
        while True:
            print 'PUBLISHER: List is going to be published ...'
            pub_socket.send_pyobj(self.createListPack())
            print 'PUBLISHER: List is published ... 10 sec wait'
            time.sleep(10)

        pub_socket.close()


class Registrator(threading.Thread):
    """Control registered and register new clients."""

    def __init__(self, context):
        super(Registrator, self).__init__()
        self.context = context

    def run(self):
        clients_socket = self.context.socket(zmq.REP)
        clients_socket.bind(cred.REGISTER_PORT)
        users_socket = self.context.socket(zmq.PAIR)
        users_socket.bind(INPROC_NOTIFY_SOCKET)

        def on_here(name):
            users_socket.send_pyobj({'name': name, 'online': True})

        def on_out(name):
            users_socket.send_pyobj({'name': name, 'online': False})

        handlers = {'here': on_here,
                    'out': on_out}

        while True:
            print 'Running server. Waiting for messages ...'
            msg = clients_socket.recv_pyobj()
            print 'Received: ', msg
            handlers[msg['kind']](msg['name'])
            if msg['kind'] == 'here':
                clients_socket.send(b"registered")
        users_socket.close()
        clients_socket.close()


class Server(object):
    """Run threads."""

    def __init__(self):
        self.zmq_context = zmq.Context()
        self.registration_thread = Registrator(self.zmq_context)
        self.publisher_thread = Publisher(self.zmq_context)

    def __exit__(self, exception_type, exception_val, trace):
        self.zmq_context.close()

    def run(self):
        self.registration_thread.start()
        self.publisher_thread.start()
