#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 14:22
# @Author : liujianxiao
# @Version：V 0.1
# @File : TestBase.py
# @desc :
from appiumClassThreeHomework.myFramework.app import App


class TestBase():
    def setup(self):
        self.app = App()

    def assertText(self,actual,expect):
        assert actual == expect