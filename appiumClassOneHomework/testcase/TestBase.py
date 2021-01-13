#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:49
# @Author : liujianxiao
# @Version：V 0.1
# @File : TestBase.py
# @desc :
from appiumClassOneHomework.page.app import App


class TestBase():
    def setup(self):
        self.app = App()
