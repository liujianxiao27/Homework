#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/7 14:45
# @Author : liujianxiao
# @Version：V 0.1
# @File : Market.py
# @desc :行情页面
from appiumClassThreeHomework.page.Search import Search
from appiumClassThreeHomework.myFramework.base_page import BasePage


class Market(BasePage):
    # 跳转至搜索页面
    def goSearch(self):
        self.steps("../file/market.yml","goSearch")
        return Search(self._driver)