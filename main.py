__author__ = 'martofrog'

import tornado.web
import tornado.ioloop

from lib.handlers import MainHandler, RefreshHandler

TEMPLATE_PATH = "./html"
STATIC_PATH = "./static"

if __name__ == "__main__":
	application = tornado.web.Application([
			(r"/", MainHandler),
			(r"/refresh", RefreshHandler),
		],
		template_path=TEMPLATE_PATH,
		static_path=STATIC_PATH,
		debug=True,
		autoreload=True,
	)

	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()

