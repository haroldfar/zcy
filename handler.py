import tornado.web
from utility import use

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
		a = self.get_argument("email", "none")
		b = self.get_argument("subject", "no subject")
		c = self.get_argument("content", "no content")
		print "received the data" + a + " " + b
		if a != "none":
			use.sendEmail(a, b, c)
			self.write("thanks for your comment!")
		else:
			self.write("wrong!")

class AboutHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("about.html")

class ServiceHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("services.html")