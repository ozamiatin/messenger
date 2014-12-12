'''
Created on Nov 14, 2014

@author: ozamiatin
'''

import sys
from PyQt4.QtGui import QApplication
from client.ui import main_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = main_window()
    wnd.show()
    app.exec_()