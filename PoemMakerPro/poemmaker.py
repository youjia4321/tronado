import os.path
import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.web import RequestHandler, Application
from tornado.options import options, define

define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(RequestHandler):
    def get(self):
        return self.render("index.html")

class PoemHandler(RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        return self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                difference=noun3)

class BookHandler(RequestHandler):
    def get(self):
        self.render(
            "book.html",
            header="Books that are great",
            books=[
                "Learning Python",
                "Programming Collective Intelligence",
                "Restful Web Services"
            ]
        )

def make_app():
    return Application(handlers=[
        (r"/", IndexHandler),
        (r"/books", BookHandler),
        (r"/poem", PoemHandler)], 
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        debug=True)

if __name__ == "__main__":
    options.parse_command_line()
    app = make_app()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()