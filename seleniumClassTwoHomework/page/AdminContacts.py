#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/9 23:16
# @Author : liujianxiao
# @Version：V 0.1
# @File : AdminContacts.py
# @desc : 通讯录页面
from selenium.webdriver.common.by import By

from seleniumClassTwoHomework.page.BasePage import BasePage


class AdminContacts(BasePage):
    #".qui_dialog_body.ww_dialog_body a[id='1688850235672214_anchor']" 组合定位
    # 添加部门
    def addDepartment(self):
        self.steps("../file/pageYaml/adminContacts.yaml","addDepartment")
        return AdminContacts(self._driver)

    # 获取部门名
    def getDepartmentName(self):
        self.refresh()
        return self.steps("../file/pageYaml/adminContacts.yaml","getDepartmentNames")




