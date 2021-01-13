#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:34
# @Author : liujianxiao
# @Version：V 0.1
# @File : main.py
# @desc : 主页
from appiumClassOneHomework.page.BasePage import BasePage
from appiumClassOneHomework.page.addresslist import AddressList


class Main(BasePage):

    # 跳转到通讯录
    def goAddresslist(self):
        self.performSteps("../file/page/main.yml","goAddresslist")
        return AddressList(self.driver)

