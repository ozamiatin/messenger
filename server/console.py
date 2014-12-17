'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import sys
import traceback

from server.core import manager



def main(argv):

    try:
        mgr = manager.ClientsListManager()
        mgr.run()
    except Exception:
        print traceback.format_exc()
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))