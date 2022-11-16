# -*-coding:utf8;-*-
from bottle import route, static_file
import os
import sys


@route('/data/<filepath:path>')
def server_static(filepath):
    pathx = os.path.dirname(sys.argv[0]) + "/files"
    print(pathx)
    return static_file(filepath, root=pathx)


@route('/assets/<filepath:path>')
def server_static(filepath):
    pathx = os.path.dirname(sys.argv[0]) + "/assets"
    return static_file(filepath, root=pathx)
