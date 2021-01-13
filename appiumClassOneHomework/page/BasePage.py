#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:17
# @Author : liujianxiao
# @Version：V 0.1
# @File : BasePage.py
# @desc : page 公共方法

from appium.webdriver.webdriver import WebDriver

from appiumClassOneHomework.util import yamlUtil


class BasePage():
    backlist = []
    errorCounts = 0
    errorMax = 3
    # 初始化driver
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    # 定位元素
    def find(self,by,locator):
        element=self.driver.find_element(by, locator)
        return element



    # 执行步骤，操作元素
    # path yaml路径
    # key yaml文件key
    # dircts 字典 当有额外字段时可存储在此字段传入
    def performSteps(self,path,key=None):
        if key is None:
            steps = yamlUtil.getDatas(path)
        else:
            steps = yamlUtil.getDatasBykey(path,key)
        for step in steps:
            by = step["by"]
            locator = step["locator"]
            element = self.find(by,locator)
            action = step["action"]
            if action == "click":
                element.click()
            elif action == "sendkeys":
                element.send_keys(step["value"])
