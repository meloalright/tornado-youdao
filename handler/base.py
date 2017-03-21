'''
 #
 #
 # base.py 存放有关handler的基础文件
 #
 #
'''

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)


    def user_model(self):
        return self.application.user_model


    def note_model(self):
        return self.application.note_model