import tornado.web
from .base import BaseHandler
from lib.diff import merger

import json
import re

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
        '''
        m = merger()
        r = re.compile('(.*?\n)')
        title = 'melo的笔记'
        source = r.findall('1.我的笔记主要内容\nmelo的笔记\n')
        snote = r.findall('1.我的笔记主要内容\nmelo的笔记\nooo\nmmmmm')
        onote = r.findall(self.get_argument('note') + '\n')
        print(source) 
        print(snote) 
        print(onote) 
        note = m.merge(source ,snote, onote)
        '''
        note = self.get_argument('note')
        return self.write(json.dumps({'code': 200, 'msg': 'ok', 'data': {'title': title, 'note': note}}))