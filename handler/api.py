import tornado.web
import tornado.websocket
from .base import BaseHandler
from lib.diff import merger

import json
import re
import queue
import redis

#conn = redis.Redis(host='127.0.0.1', port=6379)
#conn.set('147', 1)
#/usr/local/bin/redis-server /etc/redis.conf

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
        self.room = '130'
        EchoWebSocket.waiters.add(self)

    def on_message(self, message):
        #self.write_message(u"You said: " + message)
        publisher = self
        publisher.room = '147'
        #EchoWebSocket.waiters.remove(self)
        #EchoWebSocket.waiters.add(publisher)

        EchoWebSocket.reply(message, publisher)

    @classmethod
    def reply(cls, modified, publisher):
        print(cls.waiters)
        for waiter in cls.waiters:
            try:
                if waiter is not publisher and waiter.room == '147':
                    waiter.write_message(modified)
            except:
                pass

    def on_close(self):
        EchoWebSocket.waiters.remove(self)
        #print("WebSocket closed")