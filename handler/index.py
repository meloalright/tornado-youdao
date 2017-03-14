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
        u = self.user_model()
        u.test_conn()
        self.render("index.html")