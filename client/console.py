'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import sys

from client.core import controller
from client.core import facade


def main(argv):

    ui_callback = facade.UiCallback({})
    cntrlr = controller.ClientController(ui_callback)

    cntrlr.run()

    f = cntrlr.client_facade
    f.login_click(argv[1])
    
    while True:
        pass

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))