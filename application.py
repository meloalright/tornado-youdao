# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.httpclient
import tornado.web
import tornado.gen
from tornado.options import define, options

import datetime
import sqlite3


from jinja2 import Environment, FileSystemLoader

from lib.loader import Loader
import handler.index
import handler.login
import handler.note
import handler.api


'''
 #
 #
 # 初始化 application
 #
 #
'''
define("port", default=8002, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "templates/spa/static"),
            #xsrf_cookies = True,
            xsrf_cookies = False,
            cookie_secret = "cookie_secret_code",
            login_url = "/login",
            autoescape = None,
            jinja2 = Environment(loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")), trim_blocks = True),
        )

        handlers = [
            (r"/", handler.index.IndexHandler),
            (r"/login", handler.login.LoginHandler),
            (r"/spa/(.*)/", handler.note.NoteHandler),
            (r"/api/heartbeat/", handler.api.ApiHeartbeatHandler),
            (r"/api/put-modified/", handler.api.ApiPutModifiedHandler),
            # websocket api
            (r"/api/ws/echo/(.*)", handler.api.EchoWebSocket),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)


        self.db = sqlite3.connect('db/youdao.db')

        self.loader = Loader(self.db)
        self.user_model = self.loader.use("user.model")





def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print('tornado-youdao running at localhost:%s'% options.port)
    main()

