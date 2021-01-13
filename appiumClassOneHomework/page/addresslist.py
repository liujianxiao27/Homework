#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:41
# @Author : liujianxiao
# @Version：V 0.1
# @File : addresslist.py
# @desc : 通讯录
from appiumClassOneHomework.page.BasePage import BasePage
from appiumClassOneHomework.page.addmember import AddMember


class AddressList(BasePage):
    # 跳转至添加成员页面
    def goAddMember(self):
        self.performSteps("../file/page/addresslist.yml","goAddMember")
        return AddMember(self.driver)