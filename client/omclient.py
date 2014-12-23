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
        self.call(context, 'methodA')
        
    def castB(self, context, args):
        self.cast(context, 'methodB')
    

def main(argv):
    client = OMClient(transport, target)

    test_context = {"application": "oslo.messenger-server",
                    "time": time.ctime(),
                    "cast": False}

    for i in range(1, 20):
        client.castB(test_context, {})

        
    for i in range(1, 20):
        try:
            print 'Client call: ', i
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