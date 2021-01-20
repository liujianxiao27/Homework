#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/7 14:53
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_app.py
# @desc :
from appiumClassThreeHomework.myFramework.TestBase import TestBase


class TestApp(TestBase):
    def test_App(self):
        self.app.startApp().goMain().goMarket().goSearch().search()
        self.app.endApp()