'''
Created on Nov 12, 2014

@author: ozamiatin
'''

import socket
import sys

from common import cred


def print_usage():
    print '\n'.join('list - list users to chat with.',
                    'help - show usage help (this info).',
                    'q - terminate application',
                    '[nick]: <msg> - pass msg to specified user!')


STREAM_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
STREAM_SOCKET.connect((cred.HOST, cred.PORT))


if __name__ == '__main__':
    print 'Welcome to messenger!\n'

    while True:
        print 'msg$>'
        msg = sys.stdin.readline()
        STREAM_SOCKET.sendall(msg)
