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
    waitersHash = {}

    def open(self, room_id):
        self.room = room_id
        #EchoWebSocket.waiters.add(self)
        try:
            EchoWebSocket.waitersHash[room_id].add(self)
        except:
            EchoWebSocket.waitersHash[room_id] = set()
            EchoWebSocket.waitersHash[room_id].add(self)

    def on_message(self, message):
        publisher = self
        EchoWebSocket.reply(message, publisher)

    @classmethod
    def reply(cls, modified, publisher):

        print(cls.waitersHash)

        room_id = publisher.room
        waiters = cls.waitersHash[room_id]

        for waiter in waiters:
            try:
                if waiter is not publisher and waiter.room == publisher.room:
                    waiter.write_message(modified)
            except:
                pass

    def on_close(self):
        room_id = self.room
        print('close{id}'.format(id=room_id))

        EchoWebSocket.waitersHash[room_id].remove(self)
