'''
Created on Dec 1, 2014

@author: ozamiatin
'''

import sys
import threading
import uuid, time
from common import cred

import eventlet

from oslo import messaging
from oslo.config import cfg


class Enpoint(object):
    
    def methodA(self, *args, **kwargs):
        print 'Method A is called on an end point'
        
    def methodB(self, *args, **kwargs):
        print 'Method B is called on an end point'


def main(argv):
    transport = messaging.get_transport(cfg.CONF, url=cred.REGISTER_PORT)
    target = messaging.Target(topic='om-client', server="127.0.0.1")
    endpoints = [Enpoint()]
    server = messaging.get_rpc_server(transport, target, endpoints, executor='blocking')
    print "Starting server"
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
    print "Quitting ..."
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))