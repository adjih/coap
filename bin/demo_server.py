
import os
import sys
here = sys.path[0]
sys.path.insert(0, os.path.join(here,'..'))

import threading
from   coap   import    coap,                    \
                        coapResource,            \
                        coapDefines as d
import logging_setup

#---------------------------------------------------------------------------

class MessageManager:
    def __init__(self):
        pass
    
    def receive(self, srcAddr, msg):
        #print srcAddr, msg
        print srcAddr, msg["options"]

messageManager = MessageManager()

#---------------------------------------------------------------------------

# open
c = coap.coap(ipAddress='::', callback=messageManager.receive)


for t in threading.enumerate():
    print t.name


#---------------------------------------------------------------------------

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

app = make_app()
app.listen(8888)
tornado.ioloop.IOLoop.current().start()

#---------------------------------------------------------------------------

# let the server run
raw_input('\n\nServer running. Press Enter to close.\n\n')

# close
c.close()
