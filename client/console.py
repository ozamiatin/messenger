'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import sys, socket
from common import cred

def printUsage():
    print 'list - list users to chat with.\n'
    print 'help - show usage help (this info).\n'
    print 'q - terminate application\n'
    print '[nick]: <msg> - pass msg to specified user!\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((cred.HOST, cred.PORT))

if __name__ == '__main__':
    print 'Welcome to messenger!\n'    
    
    while True:
        print 'msg$>'
        msg = sys.stdin.readline()
        s.sendall(msg)