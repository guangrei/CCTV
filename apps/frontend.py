#-*-coding:utf8;-*- 
from bottle import route, view
from .mylib import util

@route('/')
@view('index')
def hi():
	ip = util.myip()
	return {'ip': ip}
		