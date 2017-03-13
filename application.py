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

from jinja2 import Environment, FileSystemLoader

import handler.index


'''
 #
 #
 # 初始化 application
 #
 #
'''
define("port", default=8080, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = True,
            cookie_secret = "cookie_secret_code",
            login_url = "/login",
            autoescape = None,
            jinja2 = Environment(loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")), trim_blocks = True),
        )

        handlers = [
            (r"/", handler.index.IndexHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print('tornado-youdao running at localhost:%s'% options.port)
    main()

