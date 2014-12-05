'''
Created on Dec 4, 2014

@author: ozamiatin
'''

import eventlet
from oslo import messaging
from oslo.config import cfg
import sys
import time
from common import cred


class OMClient(messaging.RPCClient):
    
    def __init__(self, transport, target):
        super(OMClient, self).__init__(transport, target)

    def callA(self, context, args):
        print 'Call methodA client side'
        self.call(context, 'methodA')
    

def main(argv):
    transport = messaging.get_transport(cfg.CONF, url=cred.REGISTER_PORT)
    target = messaging.Target(topic='om-client',
                              server='127.0.0.1')
    client = OMClient(transport, target)

    test_context = {"application": "oslo.messenger-server",
                    "time": time.ctime(),
                    "cast": False}

    for i in range(1, 10):
        try:
            print 'Client call'
            client.callA(test_context, {})
        except KeyboardInterrupt:
            break
        except Exception as e:
            print e
            raise
    print 'Client Quitting ...'
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))