import os.path
import tornado.ioloop
import tornado.web
import tornado.options
from handler import MainHandler, ReverseHandler, PostHandler, ContactHandler
from handler import AboutHandler, ServiceHandler, SignUpHandler

from tornado.options import define, options
define("port", default=7777, help="run on the given port", type=int)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/reverse/(\w+)", ReverseHandler),
        (r"/ppp$", PostHandler),
        (r"/contact$", ContactHandler),
        (r"/index$", MainHandler),
        (r"/about$", AboutHandler),
        (r"/services$",ServiceHandler),
        (r"/signuplist$",SignUpHandler)
    ], 
    debug = True, 
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "templates"))

if __name__ == "__main__":
	# print "started the server"
    app = make_app()
    app.listen(options.port)
    # tornado.ioloop.IOLoop.current().start()
    try:
        tornado.ioloop.IOLoop.instance().start()
    # signal : CTRL + BREAK on windows or CTRL + C on linux
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()