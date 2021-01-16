#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:46
# @Author : liujianxiao
# @Version：V 0.1
# @File : manuallyaddmember.py
# @desc : 手动添加成员
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.mobile import Mobile

from appiumClassOneHomework.page.BasePage import BasePage
from appiumClassOneHomework.page.addmember import AddMember


class ManuallyAddMember(BasePage):

    # 添加成员
    def addMember(self):
        self.performSteps("../file/page/manuallyaddmember.yml","addMember")
        return AddMember()


