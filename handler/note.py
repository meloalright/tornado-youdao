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
        '''
        #redis get id
        '''
        try:
            sessid = self.get_secure_cookie('sessid').decode()
            id = self.redis_object().get(sessid).decode()


            if id is not None:
                self.render("spa/index.html")
            else:
                self.redirect('/', permanent=False)
        except:
            self.redirect('/', permanent=False)
