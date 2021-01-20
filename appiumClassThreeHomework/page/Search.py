#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/7 14:49
# @Author : liujianxiao
# @Version：V 0.1
# @File : Search.py
# @desc :
from appiumClassThreeHomework.myFramework.base_page import BasePage


class Search(BasePage):
    # 搜索
    def search(self):
        self.steps("../file/search.yml","search")

    def getSearchText(self):
        pass
