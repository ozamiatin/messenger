'''
Created on Nov 20, 2014

@author: ozamiatin
'''

import random
from client.comunicator import ZeroMqCommunicator
from client.comunicator import ZeroMqUsersListUpdater

class CommunicationManager(object):
    """Routing service."""

    def __init__(self):
        messaging_port = str(random.randint(5000, 5999))
        self.communicator = ZeroMqCommunicator(messaging_port)

    def send_here(self, name):
        """Route socket to the given socket."""
        self.userName = name
        msg = {"kind": "here",
               "name": name,
               "address": self.communicator.get_address()}
        self.communicator.send_object(msg)
        rep = self.communicator.receive_string()
        if (rep != "registered"):
            raise Exception("Not registered!")

    # TODO: why do we need to start a handler here?
    # Maybe better to send a signal to a handler.
    def run_handler(self, users_list_view):
        self.listUpdater = ZeroMqUsersListUpdater(users_list_view,
                                                  self.communicator.context)
        # FIXME: there is no such a member.
        self.list_updater.start()
