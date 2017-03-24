import tornado.web
import tornado.gen
from .base import BaseHandler

'''
 #
 #
 # HistoryHandler
 #
 # BaseHandler来自./base.py文件
 #
 #
'''

class HistoryHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, hash_id):
        #print('====start====')

        if hash_id:
            sessid = self.get_secure_cookie('sessid').decode()
            uid = self.redis_object().get(sessid).decode()
            um = self.user_model()
            nt = self.note_model()
            nid = nt.clear_hash(hash_id)

            ifHas = um.has_this_note(uid, nid)

            ''''''
            #print('fetching')
            http_client = tornado.httpclient.AsyncHTTPClient()
            note = yield tornado.gen.Task(nt.get_note, nid)
            diff = yield tornado.gen.Task(nt.fetch_diff, nid)
            #response = yield http_client.fetch("https://translate.google.cn")
            #print(diff)
            '''
            异步响应成功:

            fetching
            fetching
            ['- @0 \n', '+ @0 这个文档是不支持中文多人协同编辑的\n', '+ @0 但是是支持中文的版本记录\n', '- @1 \n']
            [I 170324 14:52:50 web:1946] 200 GET /history/NA==/ (10.0.121.113) 701.95ms
            ['- @0 \n', '+ @0 这个文档是不支持中文多人协同编辑的\n', '+ @0 但是是支持中文的版本记录\n', '- @1 \n']
            [I 170324 14:52:50 web:1946] 200 GET /history/NA==/ (::1) 283.62ms
            '''


            #print(diff)

            if ifHas is True:
                self.render('history.html', diff=diff, note=note)
            else:
                self.redirect('/home/', permanent=False)
        else:
            self.redirect('/home/', permanent=False)

