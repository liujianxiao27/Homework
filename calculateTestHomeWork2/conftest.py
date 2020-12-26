#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/26 22:13
# @Author : liujianxiao
# @Version：V 0.1
# @File : conftest.py
# @desc : 类装饰器存放文件
import os

import pytest
import yaml

from calculateTestHomeWork2.calculate import calculator


@pytest.fixture(scope="module")
def fixture():
    print("【开始计算】")
    calc = calculator()
    yield calc
    print("【计算结束】")

yamlPath = os.path.dirname(__file__) + "\\file\\datas.yml"

def getyamlDatas(key):
    with open(yamlPath) as f:
        datas = yaml.safe_load(f)
        return datas[key]

@pytest.fixture(params=getyamlDatas("add"))
def getAddDatas(request):
    datas = request.param
    return datas


@pytest.fixture(params=getyamlDatas("reduce"))
def getreduceDatas(request):
    datas = request.param
    return datas

@pytest.fixture(params=getyamlDatas("sub"))
def getsubDatas(request):
    datas = request.param
    return datas

@pytest.fixture(params=getyamlDatas("divi"))
def getdiviDatas(request):
    datas = request.param
    return datas