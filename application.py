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

import redis

from jinja2 import Environment, FileSystemLoader

from lib.loader import Loader

import handler.index
import handler.signup
import handler.home
import handler.note
import handler.history

import handler.api
import handler.usi


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
            (r"/signup/", handler.signup.SignupHandler),
            (r"/home/", handler.home.HomeHandler),
            (r"/history/(.*)/", handler.history.HistoryHandler),

            (r"/spa/(.*)/", handler.note.NoteHandler),
            # signup
            (r"/api/signup/", handler.usi.UsiSignupHandler),
            # login
            (r"/api/login/", handler.usi.UsiLoginHandler),
            # logout
            (r"/api/logout/", handler.usi.UsiLogoutHandler),
            # get_note_list
            (r"/api/note-list/", handler.usi.UsiGetNoteListHandler),

            # new api
            (r"/api/new-note/", handler.api.ApiNewNoteHandler),
            # get note api
            (r"/api/get-note/", handler.api.ApiGetNoteHandler),
            # delete api
            (r"/api/delete-note/", handler.api.ApiDeleteNoteHandler),
            #save api
            (r"/api/heartbeat/", handler.api.ApiHeartbeatHandler),
            # websocket api
            (r"/api/ws/echo/(.*)", handler.api.EchoWebSocket),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)


        self.db = sqlite3.connect('db/youdao.db')

        self.redis = redis.Redis(host='127.0.0.1', port=6379)

        self.loader = Loader(self.db)
        self.user_model = self.loader.use("user.model")
        self.note_model = self.loader.use("note.model")




def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print('tornado-youdao running at localhost:%s'% options.port)
    main()

