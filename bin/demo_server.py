#! /usr/bin/python

import os
import sys
here = sys.path[0]
sys.path.insert(0, os.path.join(here,'..'))
sys.path.insert(0, os.path.join(here,'../../tools'))

import threading
from   coap   import    coap,                    \
                        coapResource,            \
                        coapDefines as d
import nologging_setup

#---------------------------------------------------------------------------

class MessageManager:
    def __init__(self):
        pass
    
    def receive(self, srcAddr, msg):
        #print srcAddr, msg
        print srcAddr, msg["options"], "".join((chr(x) for x in msg["payload"]))

messageManager = MessageManager()

#---------------------------------------------------------------------------

import ServerGui

serverGui = ServerGui.ServerGui()

# open
c = coap.coap(ipAddress='::', callback=serverGui.receiveCoap)

for t in threading.enumerate():
    print t.name

#---------------------------------------------------------------------------

# let the server run
serverGui.run()

raw_input('\n\nServer running. Press Enter to close.\n\n')

# close
c.close()
