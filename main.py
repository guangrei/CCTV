# -*-coding:utf8;-*-
import bottle
from apps import static
from apps import api
from apps import frontend
from qpycmd import path
import os

os.chdir(path)
app = application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8000)
