#/usr/bin/python
#coding=utf8
__author__ = 'jarrahwu'

import tornado.web
from tornado.escape import json_decode, json_encode
from hqlh import codedef

class BaseHandler(tornado.web.RequestHandler):

    def check_params(self, *keys):
        params = json_decode(self.request.body)
        params_got = {}
        for tmp_key in keys:
            params_got[tmp_key] = params.get(tmp_key, False)
            #如果找不到这个参数就返回参数不匹配
            if not params_got[tmp_key]:
                return False

        return params_got

    def write_back(self, status = 200, code = None, **info):
        user_info = json_encode(info)
        if code:
            info['code'] = code
        user_info = json_encode(info)

        self.write(user_info)
        self.set_status(status)
