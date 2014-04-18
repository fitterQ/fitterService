#!/usr/bin/env python
#coding=utf8
from hqlh import codedef as DEFINE
import hqlh.uservice
from hqlh.wrapper import BaseHandler

def url_spec(*args, **kwargs):
    return [
        (r'/user/login', LoginHandler, kwargs),
    ]
        
class LoginHandler(BaseHandler):
    def post(self):
        user = {}
        user = self.check_params('mobile','password')
        #如果参数没有传上来的话,进行处理
        if not user:
            self.write_back(**DEFINE.NO_MATCH_PARAMS)
            return

        _mobile = user['mobile']
        _password = user['password']

        userInfo = self.is_valid(_mobile,_password);
        if userInfo:
            self.send_user_info(userInfo)
        else :
            self.send_user_error(DEFINE.USER_NOT_FOUND)

    #调用服务登陆验证
    def is_valid(self, mobile, password):
        #if account == password:return True
        userInfo = hqlh.uservice.login_user(mobile=mobile, password=password)
        if userInfo:
            return userInfo
        else: return False

    #返回用户信息
    def send_user_info(self, userInfo):
        print(userInfo)
        self.write_back(code=1,**userInfo)

    def send_user_error(self, errorInfo):
        self.write_back(**errorInfo)
