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
        '''
        #redis get id
        '''
        try:
            sessid = self.get_secure_cookie('sessid').decode()
            id = self.redis_object().get(sessid).decode()

            if id:
                um = self.user_model()
                note_list = um.get_user_note_list(id)
                self.render("home.html",note_list=note_list)
            else:
                self.redirect('/', permanent=False)
        except:
            self.redirect('/', permanent=False)

