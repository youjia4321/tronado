import tornado.ioloop
from tornado.web import RequestHandler, Application
from tornado.options import define, options
import tornado.httpserver
import textwrap

define('port', default=8000, help='run on the given port', type=int)

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello World <a href='login'>login</a>")

class LoginHandler(RequestHandler):
    def get(self):
        self.write('''
        Welcome to login <a href='/'>back</a><br>
        <form method="post" action="wrap">
            username<br><input type="text" name="username" required><br>
            password<br><input type="password" name="password" required><br>
            <input type="submit" value="提交">
        </form>
        ''')

class WrapHandler(RequestHandler):

    def write_error(self, status_code, **kwargs):  # 重写write_error方法
        self.write("Gosh darnit, user! You caused a %d error." % status_code)
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username == 'admin' and password == '123456':
            self.write("就算你登录进来也没的奖励啊!")
        else:
            self.write('''用户名或密码错误 <a href='/login'>back</a>''')

def make_app():
    return Application(handlers=[
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/wrap", WrapHandler)],
        debug=True)

if __name__ == "__main__":
    options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



