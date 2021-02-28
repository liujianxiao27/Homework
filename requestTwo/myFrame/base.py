#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/28 11:37
# @Author : liujianxiao
# @Version：V 0.1
# @File : base.py
# @desc : 父类
import requests


class Base():
    def __init__(self):
        self.request_session = requests.session()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww82b74853d3f08580&corpsecret=ws13zUNeO5HbzWdZFHzd10tN6odXac_1iDyVQ2tTyMM"
        result = requests.get(url)
        token = result.json()["access_token"]
        print("token:",token)
        self.request_session.params ={'access_token':token}

    def send(self,*args,**kwargs):
        return self.request_session.request(*args,**kwargs)
