'''
Created on Nov 14, 2014

@author: ozamiatin
'''

import sys
from PyQt4.QtGui import QApplication
from client.core.controller import ClientController
from client.core.facade import UiCallback
from client.ui.main_window import MainWindow


def main(argv):

    app = QApplication(sys.argv)
    wnd = MainWindow()
    ui_callback = UiCallback(wnd)
    cntrlr = ClientController(ui_callback)

    wnd.set_client_facade(cntrlr.client_facade)

    wnd.show()
    cntrlr.run()

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))