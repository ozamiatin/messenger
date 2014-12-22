'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import sys
import traceback
import logging

from server.core import manager

logging.basicConfig(filename='oslo.im-server.log',
                    level=logging.DEBUG)

import logging
LOG = logging.getLogger(__name__)

def main(argv):

    try:
        mgr = manager.ClientsListManager()
        mgr.run()
    except KeyboardInterrupt:
        mgr.stop()
        print 'Quit ... Ctr+C'
        LOG.debug('Quit ... Ctr+C')
        return 0
    except Exception:
        mgr.stop()
        print traceback.format_exc()
        LOG.debug(traceback.format_exc())
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))