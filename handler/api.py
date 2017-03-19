import tornado.web
import tornado.websocket
from .base import BaseHandler
from lib.diff import merger

import json
import re
import queue

q = queue.Queue()
#queue

'''
 #
 #
 # ApiHandler
 #
 # BaseHandler来自./base.py文件
 #
 #
'''

class ApiHandler(BaseHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


'''
 # @ ApiHeartbeatHandler
'''
class ApiHeartbeatHandler(ApiHandler):
    def get(self):
        o = q.get()
        return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': o}))


'''
 # @ ApiPutModifiedHandler
'''
class ApiPutModifiedHandler(ApiHandler):
    def post(self):
        modified = self.get_argument("modified", {})
        q.put(modified)
        return self.write(json.dumps({'code': 200, 'msg': 'success', 'data': {}}))


'''
 # @ EchoWebSocket
'''
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    waiters = set()

    def open(self):
        EchoWebSocket.waiters.add(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        EchoWebSocket.reply(message)

    @classmethod
    def reply(cls, modified):
        print(cls.waiters)
        for waiter in cls.waiters:
            try:
                waiter.write_message(modified)
            except:
                pass

    def on_close(self):
        EchoWebSocket.waiters.remove(self)
        print("WebSocket closed")