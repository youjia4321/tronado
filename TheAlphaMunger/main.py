import os.path
import random
import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.web import RequestHandler, Application
from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class PoemHandler(RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped: 
                    mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        # print(source_map)
        change_lines = text_to_change.split('\r\n')
        self.render('munged.html', source_map=source_map, change_lines=change_lines,
                choice=random.choice)


def make_app():
    return Application(handlers=[
        (r"/", IndexHandler),
        ((r'/poem', PoemHandler))],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True)


if __name__ == "__main__":
    options.parse_command_line()
    app = make_app()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()