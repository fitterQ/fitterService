# coding:utf8

import hqlh.db

def create_user(user):
    '''用户注册
    '''
    dbc = hqlh.db.get_conn('fitter')
    sql = "INSERT INTO user (mobile,passwd) VALUES (%s,%s)"
    mobile = user['mobile']
    password = user['password']
    params = [mobile,password]
    userInfo = dbc.execute(sql, *params)
    return userInfo

def login_user(user):
    '''用户登陆
    '''
    dbc = hqlh.db.get_conn('fitter')
    mobile = user['mobile']
    password = user['password']
    params = [mobile,password]
    userInfo = dbc.get("SELECT * FROM user WHERE mobile=%s and passwd=%s", *params)
    if userInfo :
        return userInfo
    else :
        return False

def exist_user(user):
    '''检查用户存在
    '''
    dbc = hqlh.db.get_conn('fitter')
    mobile = user['mobile']
    params = [mobile]
    userInfo = dbc.get("SELECT * FROM user WHERE mobile=%s",*params)
    if userInfo:
        return userInfo
    else :
        return False

def id_user(uid):
    dbc = hqlh.db.get_conn('fitter')
    userInfo = dbc.get("SELECT * FROM user WHERE id=%s",uid)

    if userInfo:return userInfo
    else :return False