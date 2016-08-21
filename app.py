import os.path
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options
define("port", default=7777, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class PostHandler(tornado.web.RequestHandler):
	def post(self):
		a = self.get_argument("aaa", "AAA")
		b = self.get_argument("bbb", "BBB")
		self.write("just to test whether post is working or not see a and b are " + a + b)

	def get(self):
		self.write("goes to get instead of post")

class ContactHandler(tornado.web.RequestHandler):
	def get(self):
		u1 = ["john", "jack", "mary", "hello kitty"]
		self.render("contact.html", userdict = u1)

	def post(self):
		# a = self.get_argument("email")
		# b = self.get_argument("subject")
		self.write("thanks for your comment!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/reverse/(\w+)", ReverseHandler),
        (r"/ppp$", PostHandler),
        (r"/contact$", ContactHandler)
    ], 
    debug = True, 
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "templates"))

if __name__ == "__main__":
	# print "started the server"
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()