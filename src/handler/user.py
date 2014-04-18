#!/usr/bin/env python
#encoding=utf8
import tornado.web
import tornado.ioloop
from tornado.escape import json_decode
import json
import hqlh.pwd
from hqlh.uservice import exist_user
from hqlh.validate import valid_pwd, valid_mobile
from hqlh import codedef as DEFINE
from hqlh.wrapper import BaseHandler
from hqlh.uservice import register_user, get_id_user

def url_spec(*args, **kwargs):
    return [
        (r'/user/register', RegisterHandler, kwargs),
    ]

class RegisterHandler(BaseHandler):

    def post(self, *args, **kwargs):
        """用户注册"""
        #检查是否有对应的参数
        user = {}
        user = self.check_params('mobile','password')

        if not user:
            self.write_back(**DEFINE.NO_MATCH_PARAMS)
            return

        #密码长度检验
        if not valid_pwd(user['password']):
            self.write_back(**DEFINE.PWD_LEN_NOT_VALID);
            return

        #用户账号检验,也就是电话号码的检验
        if not valid_mobile(user['mobile']):
            self.write_back(**DEFINE.USER_MOBILE_FORMAT_NOT_VALID)
            return

        #对密码进行前端加密和后台加密
       # user['password'] = hqlh.pwd.fore_sha1(params['password'])
       # user['password'] = hqlh.pwd.back_sha1(user['mobile'], user['password'])

        #用户有效性检验
        if not exist_user(**user):
            userId = register_user(**user)
            userInfo = get_id_user(userId)
            self.write_back(status=200, code=1, **userInfo)
            return
        else:
            self.write_back(**DEFINE.USER_EXISTED)
            return
