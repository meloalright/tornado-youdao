import tornado.web
from .base import BaseHandler

'''
 #
 #
 # LoginHandler
 #
 # BaseHandler来自./base.py文件
 #
 #
'''

class LoginHandler(BaseHandler):
    def get(self, template_variables = {}):
        self.render("login.html")