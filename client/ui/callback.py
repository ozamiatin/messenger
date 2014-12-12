'''
Created on Dec 12, 2014

@author: ozamiatin
'''

from client.core import facade


class UiCallbackQt(facade.UiCallback):
    '''
    Implemented using QT Event Loop and Qt Events system
    '''

    def __init__(self, main_window, application):
        self.main_window = main_window
        self.application = application


    def update_history(self):
        pass