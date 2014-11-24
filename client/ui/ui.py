'''
Created on Nov 14, 2014

@author: ozamiatin
'''

import sys
from PyQt4.QtGui import QApplication
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    app.exec_()