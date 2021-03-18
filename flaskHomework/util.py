#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/18 16:47
# @Author : liujianxiao
# @Version：V 0.1
# @File : util.py
# @desc : 工具类

# 封装task
from flaskHomework.interface import Task, TestCase


class util():
    def getTasklist(task: Task):
        id=task.id
        name=task.name
        caseid=task.caseid
        isDelete=task.is_delete
        if isDelete == 0:
            return None
        else:
            testCaseList=[]
            for cid in caseid:
                testcase=TestCase.query.filter_by(id=cid)
                testcaseJson={
                    "id": testcase.id,
                    "name": testcase.name,
                    "steps": testcase.steps
                }
                testCaseList.append(testcaseJson)
            taskJson={
                "id": id,
                "name": name,
                "cases": testCaseList
            }
            return taskJson