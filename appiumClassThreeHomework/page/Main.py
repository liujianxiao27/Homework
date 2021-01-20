#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/7 14:36
# @Author : liujianxiao
# @Version：V 0.1
# @File : Main.py
# @desc :
from appiumClassThreeHomework.page.Market import Market
from appiumClassThreeHomework.myFramework.base_page import BasePage


class Main(BasePage):

    # 跳转至行情页面
    def goMarket(self):
        self.steps("../file/main.yml","goMarket")
        return Market(self._driver)

