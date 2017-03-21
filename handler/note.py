import tornado.web
from .base import BaseHandler

'''
 #
 #
 # NoteHandler
 #
 # BaseHandler来自./base.py文件
 #
 #
'''

class NoteHandler(BaseHandler):
    def get(self, template_variables = {}):
        self.set_secure_cookie("nick", "##melo##")
        self.set_secure_cookie("sessid", '1', expires_days=1)

        self.render("spa/index.html")