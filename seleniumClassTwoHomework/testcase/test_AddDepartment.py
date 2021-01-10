#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/10 11:49
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_AddDepartment.py
# @desc :
from seleniumClassTwoHomework.page.AdminIndex import AdminIndex


class TestAddDepartment():
    def setup(self):
        self.main=AdminIndex()
    def test_Success(self):

        namelists = self.main.goAdminContacts().addDepartment().getDepartmentName()
        # namelists = self.main.goAdminContacts().getDepartmentName()
        assert "火影部" in namelists

