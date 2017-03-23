import tornado.web
import tornado.websocket
from .base import BaseHandler
from lib.diff import merger

import json
import re
import queue
import redis


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
class ApiNewNoteHandler(ApiHandler):
    def post(self):
        '''
        #redis get id
        '''
        sessid = self.get_secure_cookie('sessid').decode()
        id = self.redis_object().get(sessid).decode()
        if id:
            nm = self.note_model()
            nm.create_note_object('我的笔记', id, 1, '这个文档是不支持中文多人协同编辑的\n但是是支持中文的版本记录\n')
            return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': {}}))
        else:
            return self.write(json.dumps({'code': 1, 'msg': 'error', 'data': {}}))


'''
 # @ ApiGetNoteHandler
'''
class ApiGetNoteHandler(ApiHandler):
    def get(self):

        hash_id = self.get_argument("hash_id", None)
        if hash_id:
            nt = self.note_model()
            nid = nt.clear_hash(hash_id)
            note = nt.get_note(nid)
            if note:
                return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': note}))
            else:
                return self.write(json.dumps({'code': 2, 'msg': 'no this note', 'data': {}}))

        else:
            return self.write(json.dumps({'code': 1, 'msg': 'error', 'data': {}}))



'''
 # @ ApiDeleteNoteHandler
'''
class ApiDeleteNoteHandler(ApiHandler):
    def post(self):
        hash_id = self.get_argument("hash_id", None)
        '''
        #redis get id
        '''
        sessid = self.get_secure_cookie('sessid').decode()
        id = self.redis_object().get(sessid).decode()
        if nid and uid:
            um = self.user_model()
            nt = self.note_model()
            #clear hash
            nid = nt.clear_hash(hash_id)
            if um.has_this_note(uid, nid):
                nm = self.note_model()
                nm.delete_note(nid)
                return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': {}}))
            else:
                return self.write(json.dumps({'code': 2, 'msg': 'no permission', 'data': {}}))

        else:
            return self.write(json.dumps({'code': 1, 'msg': 'error', 'data': {}}))


'''
 # @ ApiHeartbeatHandler
'''
class ApiHeartbeatHandler(ApiHandler):
    def post(self):
        hash_id = self.get_argument("hash_id", None)
        nt = self.note_model()
        # clear hash
        nid = nt.clear_hash(hash_id)
        #reverse hash
        name = self.get_argument("name", None)
        sub = self.get_argument("sub", None)

        if name and sub:
            nm = self.note_model()
            nm.update_note(nid, name, sub)
            return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': {}}))
        else:
            return self.write(json.dumps({'code': 1, 'msg': 'faild', 'data': {}}))


'''
 # @ ApiPushHistoryHandler
'''
class ApiPushHistoryHandler(ApiHandler):
    def post(self):
        hash_id = self.get_argument("hash_id", None)
        nt = self.note_model()
        # clear hash
        nid = nt.clear_hash(hash_id)
        #reverse hash

        if nid is not None:
            nm = self.note_model()
            nm.push_history(nid)
            return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': {}}))
        else:
            return self.write(json.dumps({'code': 1, 'msg': 'faild', 'data': {}}))






'''
 # @ EchoWebSocket
'''
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    waiters = set()
    waitersHash = {}

    def open(self, room_id):
        self.room = room_id

        self.push_history(room_id)

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
    def push_history(self, room):
        nm = ApiHandler.note_model(self)
        nid = nm.clear_hash(room)
        nm.push_history(nid)
        print('先存历史')

    def on_close(self):
        room_id = self.room

        EchoWebSocket.waitersHash[room_id].remove(self)
