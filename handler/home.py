import tornado.web
from .base import BaseHandler

'''
 #
 #
 # HomeHandler
 #
 # BaseHandler来自./base.py文件
 #
 #
'''

class HomeHandler(BaseHandler):
    def get(self, template_variables = {}):
        sessid = self.get_secure_cookie("sessid")
        sessid = 1
        id = sessid

        if id:
            um = self.user_model()
            note_list = um.get_user_note_list(id)

        self.render("home.html",note_list=note_list)