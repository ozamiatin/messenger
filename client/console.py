'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import sys
import traceback

from client.core import controller
from client.core import facade


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
        print 'Quit ...'
        return 0
    except Exception:
        cntrlr.stop()
        print traceback.format_exc()
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))