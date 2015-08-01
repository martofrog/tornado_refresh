__author__ = 'martofrog'

import sys
import tornado.web
import logging

import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class RefreshHandler(tornado.web.RequestHandler):
    def get(self):
        items = []

        items.append(["A", "B", 0])
        items.append(["C", "D", 0])
        items.append(["E", "F", 0])
        items.append(["G", "H", 0])

        for i in range(4):
            items[i][2] = str(random.randint(0, 10000))

        self.render("item_row.html", items=items)
