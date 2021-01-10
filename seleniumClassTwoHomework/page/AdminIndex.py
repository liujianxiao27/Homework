#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/9 23:12
# @Author : liujianxiao
# @Version：V 0.1
# @File : AdminIndex.py
# @desc : 登录后的企业微信主页面
from seleniumClassTwoHomework.page.AdminContacts import AdminContacts
from seleniumClassTwoHomework.page.BasePage import BasePage


class AdminIndex(BasePage):

    # 跳转至通讯录页面
    def goAdminContacts(self):
        self.steps("../file/pageYaml/adminIndex.yaml","goAdminContacts")
        return AdminContacts(self._driver)
