#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/22 21:51
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_calculator.py
# @desc :计算器测试类
import pytest
import yaml

from pythonTest.calculator import calculator

def getYamlDatas(path):
    with open(path) as f:
        datas = yaml.safe_load(f)
        return datas


class TestCalculator():
    yamlDatas=getYamlDatas("../file/datas.yaml")

    def setup_class(self):
        self.cal = calculator()


    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expected",yamlDatas["add"])
    def test_add(self,a,b,expected):
        result = self.cal.add(a,b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", yamlDatas["reduce"])
    def test_reduce(self,a,b,expected):
        result=self.cal.reduce(a, b)
        assert result == expected
    @pytest.mark.parametrize("a,b,expected", yamlDatas["sub"])
    def test_mul(self,a,b,expected):
        result=self.cal.mul(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", yamlDatas["divi"])
    def test_divi(self,a,b,expected):
        result=self.cal.divi(a, b)
        assert result == expected



if __name__ == '__main__':
    pytest.main()