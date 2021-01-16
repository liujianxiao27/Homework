#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:50
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_AddMember.py
# @desc :
from appiumClassOneHomework.page.app import App
from appiumClassOneHomework.testcase.TestBase import TestBase


class TestAddMember(TestBase):

    def test_addSuccess(self):
       toast = self.app.start().goMain().goAddresslist().goAddMember().goManuallyAddMember().addMember().getTost()
       assert toast == "添加成功"

