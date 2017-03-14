import tornado.web
from .base import BaseHandler

'''
 #
 #
 # IndexHandler
 #
 # BaseHandler来自./base.py文件
 #
 #
'''

class IndexHandler(BaseHandler):
    def get(self, template_variables = {}):
        print(self.user_model)
        self.render("index.html")