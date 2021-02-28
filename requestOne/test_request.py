#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/23 21:37
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_request.py
# @desc : 通讯录增删改查
import requests


class TestWeixin():
    token = None

    def setup(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww82b74853d3f08580&corpsecret=ws13zUNeO5HbzWdZFHzd10tN6odXac_1iDyVQ2tTyMM"
        result = requests.get(url)
        self.token = result.json()["access_token"]

    # 添加用户
    def test_add(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        jsonData = {
            "userid":"suolong",
            "name":"索隆",
            "mobile":"16930000000",
            "department": [2],
        }
        result = requests.post(url,json=jsonData)
        print(result.json())
        assert result.json()["errmsg"] == "created"

    # 查询
    def test_search(self):
        userId = "suolong"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userId}"
        result = requests.get(url)
        print(result.json())
        assert result.json().get("name") == "索隆"

    # 更改成员信息
    def test_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        jsondata = {
            "userid":"suolong",
            "alias":"海贼猎人"
        }
        result = requests.post(url,json=jsondata)
        print(result.json())
        assert result.json()["errmsg"] == "updated"

    # 删除成员
    def test_delete(self):
        userId = "suolong"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userId}"
        result = requests.get(url)
        print(result.json())
        assert result.json()["errmsg"] == "deleted"
