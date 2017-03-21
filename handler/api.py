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
    def post(self):
        pass
        return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': {}}))



'''
 # @ EchoWebSocket
'''
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    waiters = set()
    waitersHash = {}

    def open(self, room_id):#, nick_name):
        self.room = room_id
        ##self.name = nick_name
        try:
            EchoWebSocket.waitersHash[room_id].add(self)
        except:
            EchoWebSocket.waitersHash[room_id] = set()
            EchoWebSocket.waitersHash[room_id].add(self)

    def on_message(self, message):
        publisher = self
        #EchoWebSocket.reply(message, publisher)
        EchoWebSocket.put_queue(message, publisher)
        EchoWebSocket.run_queue()

    @classmethod
    def run_queue(cls):
        while True:
            if not q.empty():
                EchoWebSocket.pop_queue()
            else:
                break


    @classmethod
    def put_queue(cls, modified, publisher):
        q.put({
            'modified': modified,
            'publisher': publisher
        })


    @classmethod
    def pop_queue(cls):
        o = q.get()
        message = o['modified']
        publisher = o['publisher']
        EchoWebSocket.reply(message, publisher)

    @classmethod
    def reply(cls, modified, publisher):

        room_id = publisher.room
        waiters = cls.waitersHash[room_id]
        onlines = []

        for waiter in waiters:
            try:
                if waiter is not publisher and waiter.room == publisher.room:
                    waiter.write_message(modified)
            except:
                pass
            #在线者
            #onlines.append(waiter.name)

        #把在线者返回
        '''
        waiter.write_message({
            'type': 'online',
            'onlines': onlines
        })
        '''


    def on_close(self):
        room_id = self.room

        EchoWebSocket.waitersHash[room_id].remove(self)
