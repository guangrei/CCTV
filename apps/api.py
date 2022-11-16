#-*-coding:utf8;-*- 
from bottle import route, hook, response
from .mylib import cctv, util
import json

c = cctv.CCTV()

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

@hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = _allow_origin
	response.headers['Access-Control-Allow-Methods'] = _allow_methods
	response.headers['Access-Control-Allow-Headers'] = _allow_headers

@route('/', method = 'OPTIONS')
@route('/<path:path>', method = 'OPTIONS')
def options_handler(path = None):
	return

@route('/api/start_webcam')
def ws():
	ip = util.myip()
	response.headers['Content-Type'] = 'application/json'
	res = {}
	ok = c.startWebcam()
	if ok:
		res['status'] = 'success'
		res['msg'] = 'http://{0}:9000'
		return json.dumps(res)
	else:
		res['status'] = 'failed'
		res['msg'] = "couldn't start webcam!"
		return json.dumps(res)
		
@route('/api/stop_webcam')
def we():
	w = c.stopWebcam()
	res = {}
	res['status'] = 'success'
	return json.dumps(res)
	
@route('/api/start_rec')
def rec():
	ip = util.myip()
	response.headers['Content-Type'] = 'application/json'
	res = {}
	ok = c.record()
	if ok:
		res['status'] = 'success'
		res['msg'] = 'http://{0}:8000/data/{1}'.format(ip, ok)
		return json.dumps(res)
	else:
		res['status'] = 'failed'
		res['msg'] = 'please turn off recorder or webcam first!'
		return json.dumps(res)

@route('/api/start_rec2')
def rec():
	ip = util.myip()
	response.headers['Content-Type'] = 'application/json'
	res = {}
	ok = c.record(True)
	if ok:
		res['status'] = 'success'
		res['msg'] = 'http://{0}:8000/data/{1}'.format(ip, ok)
		return json.dumps(res)
	else:
		res['status'] = 'failed'
		res['msg'] = 'please turn off recorder or webcam first!'
		return json.dumps(res)

@route('/api/stop_rec')
def rec():
	ip = util.myip()
	response.headers['Content-Type'] = 'application/json'
	res = {}
	ok = c.stop()
	if ok:
		res['status'] = 'success'
		res['msg'] = 'http://{0}:8000/data/{1}'.format(ip, ok)
		return json.dumps(res)
	else:
		res['status'] = 'failed'
		return json.dumps(res)

@route('/api/shot')
def rec():
	ip = util.myip()
	response.headers['Content-Type'] = 'application/json'
	res = {}
	ok = c.shot()
	if ok:
		res['status'] = 'success'
		res['msg'] = 'http://{0}:8000/data/{1}'.format(ip, ok)
		return json.dumps(res)
	else:
		res['status'] = 'failed'
		res['msg'] = 'currently cant use camera for taking pictures!'
		return json.dumps(res)