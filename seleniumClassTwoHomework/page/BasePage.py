#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/9 23:02
# @Author : liujianxiao
# @Version：V 0.1
# @File : BasePage.py
# @desc : 封装公共方法
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webdriver import WebDriver

from seleniumClassTwoHomework.util import yamlUtil


class BasePage():

    #初始化
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self._driver = driver
        self._driver.implicitly_wait(10)




    # 定位元素
    # by 查找方式 支持元组(by,locator)若以元组形式不用传locator字段
    # locator 定位元素
    def find(self,by,locator):
        if by == "css_selector":
            element = self._driver.find_element(By.CSS_SELECTOR,locator)
        else:
            element = self._driver.find_element(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)
        return element

    # 获取元素值列表
    # by 查找方式 支持元组(by,locator)若以元组形式不用传locator字段
    # locator 定位元素
    def getElementTextList(self,by,locator):
        elementstxts = [] # 元素值列表
        elements = self._driver.find_elements(*by) if isinstance(by,tuple) else self._driver.find_elements(by,locator)
        for element in elements:
            elementstxts.append(element.text)
        print("elementstxts列表:",elementstxts)
        return elementstxts

    # 根据步骤操作元素
    # path yaml文件路径
    # key yaml文件key值非必填
    def steps(self,path,key=None):
        # 从yaml文件中读取步骤
        if key is None:
            steps = yamlUtil.getdatas(path)
        else:
            steps = yamlUtil.getdatasByKey(path, key)
        for step in steps:
            by = step["by"]
            locator = step["locator"]
            action = step["action"]
            if action == "click":
                self.find(by,locator).click()
            elif action == "sendkeys":
                self.find(by,locator).send_keys(step["value"])
            elif action == "getlist":
                namelists = self.getElementTextList(by,locator)
                return namelists




    # cookie登录
    def _cookie_login(self):
        self._driver.get("https://work.weixin.qq.com")
        with open("../file/cookies.json", "r") as f:
            cookies=json.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def refresh(self):
        self._driver.refresh()
    # 释放资源
    def end(self):
        self._driver.quit()
