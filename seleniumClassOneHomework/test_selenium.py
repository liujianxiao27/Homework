#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/5 22:00
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_selenium.py
# @desc :使用 cookie 和浏览器复用，实现企业微信的点击客户联系
import json
from time import sleep

import pytest
from selenium import webdriver

# 运行前cmd执行chrome --remote-debugging-port=9222
class TestWeiXin():
    def setup(self):
        chromeargs = webdriver.ChromeOptions()
        chromeargs.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chromeargs)
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # 写入过cookie后下次跳过运行
    @pytest.mark.skip
    def test_witerCookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        with open("cookies.json","w") as f:
            json.dump(cookies,f)

    def test_addCookies(self):
        self.driver.get("https://work.weixin.qq.com")
        with open("cookies.json","r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath('//*[@id="menu_customer"]/span').click()