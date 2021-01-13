#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:44
# @Author : liujianxiao
# @Version：V 0.1
# @File : addmember.py
# @desc :添加成员
from appiumClassOneHomework.page.BasePage import BasePage
from appiumClassOneHomework.page.manuallyaddmember import ManuallyAddMember


class AddMember(BasePage):
    # 跳转至手动添加成员页面
    def goManuallyAddMember(self):
        self.performSteps("../file/page/addmember.yml","goManuallyAddMember")
        return ManuallyAddMember(self.driver)