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
        self.render("index.html")