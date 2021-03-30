# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2021/3/23 18:40
@file:test_user_reg.py.py
@desc:
'''

import requests
import unittest
from read_excel import *
import json
from db import *

class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx","TestUserReg")# 读取该测试类所有用例数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_user_reg_normal(self):
        # 从数据列表中查找到该用例数据
        case_data = get_test_data(data_list,"test_user_reg_normal")
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')# 从字典中取数据，excel中的标题也必须是小写url
        data = json.loads(case_data.get('data'))  # 转为字典，需要取里面的name进行数据库检查
        expect_res = json.loads(case_data.get('expect_res'))  # 转为字典，断言时直接断言两个字典是否相等
        name = data.get('name')

        # 环境检查
        if check_user(name):
            del_user(name)
        # 发送请求
        res = requests.post(url=url, json=data)  # 用data=data 传字符串也可以
        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), expect_res)
        # 数据库断言
        self.assertTrue(check_user(name))
        # 环境清理（由于注册接口向数据库写入了用户信息）
        del_user(name)


    def test_user_reg_exist(self):
        case_data = get_test_data(data_list,"test_user_reg_exist")
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = json.loads(case_data.get('expect_res'))
        name = data.get('name')

        # 发送请求1
        requests.post(url=url,data=data)
        # 数据库断言
        self.assertTrue(check_user(name))

        # 发送请求2
        res = requests.post(url=url,data=data)
        # 响应断言（整体断言）
        self.assertDictEqual(res.json(),expect_res)
        # 数据库断言
        self.assertTrue(check_user(name))
        # 环境清理
        del_user(name)






