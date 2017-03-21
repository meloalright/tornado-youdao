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
        self.set_cookie("nick", "##melo##")
        self.render("spa/index.html")