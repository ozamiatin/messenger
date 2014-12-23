'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import sys
import traceback
import logging

from client.core import controller
from client.core import facade

logging.basicConfig(filename='oslo.im-client.log',
                    level=logging.DEBUG)

LOG = logging.getLogger(__name__)

def main(argv):

    try:
        ui_callback = facade.UiCallback({})
        cntrlr = controller.ClientController(ui_callback)
    
        cntrlr.start()

        f = cntrlr.client_facade
        f.login_click(argv[1])

        while True:
            cntrlr.join(timeout=1)

    except KeyboardInterrupt:
        cntrlr.stop()
        LOG.debug('Quit ... Ctrl+C')
        return 0
    except Exception:
        cntrlr.stop()
        LOG.debug(traceback.format_exc())
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))