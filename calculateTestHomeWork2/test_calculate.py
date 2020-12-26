#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/26 22:18
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_calculate.py
# @desc :计算器测试类
import pytest


class TestCalculate():
    @pytest.mark.run(order=1)
    def test_add(self,fixture,getAddDatas):
        print("参数1：",getAddDatas[0])
        print("参数2：",getAddDatas[1])
        result = fixture.add(getAddDatas[0],getAddDatas[1])
        print("结果:",result)
        print("断言值：",getAddDatas[2])
        assert result == getAddDatas[2]

    @pytest.mark.run(order=4)
    def test_divi(self,fixture,getdiviDatas):
        print("参数1：", getdiviDatas[0])
        print("参数2：", getdiviDatas[1])
        result=fixture.divi(getdiviDatas[0], getdiviDatas[1])
        print("结果:", result)
        print("断言值：", getdiviDatas[2])
        assert result == getdiviDatas[2]

    @pytest.mark.run(order=2)
    def test_reduce(self,fixture,getreduceDatas):
        print("参数1：", getreduceDatas[0])
        print("参数2：", getreduceDatas[1])
        result=fixture.reduce(getreduceDatas[0], getreduceDatas[1])
        print("结果:", result)
        print("断言值：", getreduceDatas[2])
        assert result == getreduceDatas[2]

    @pytest.mark.run(order=3)
    def test_mul(self,fixture,getsubDatas):
        print("参数1：", getsubDatas[0])
        print("参数2：", getsubDatas[1])
        result=fixture.mul(getsubDatas[0], getsubDatas[1])
        print("结果:", result)
        print("断言值：", getsubDatas[2])
        assert result == getsubDatas[2]

