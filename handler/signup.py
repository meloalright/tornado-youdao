import tornado.web
from .base import BaseHandler

'''
 #
 #
 # SignupHandler
 #
 # BaseHandler来自./base.py文件
 #
 #
'''

class SignupHandler(BaseHandler):
    def get(self, template_variables = {}):
        self.render("signup.html")