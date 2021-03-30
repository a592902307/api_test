# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2021/3/23 16:53
@file:test_user_login.py.py
@desc:
'''

import requests
import unittest
from read_excel import *
import json
from config import *
from case_log import *

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")# 读取该测试类所有用例数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_user_login_normal(self):
        # 从数据列表中查找到该用例数据
        case_data = get_test_data(self.data_list,'test_user_login_normal')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res = requests.post(url=url,data=json.loads(data))# 表单请求，字符串转为字典格式
        log_case_info('test_user_login_normal', url, data, expect_res, res)
        self.assertEqual(res.text,expect_res)

    def test_user_login_password_wrong(self):
        # 从数据列表中查找到该用例数据
        case_data = get_test_data(self.data_list,'test_user_login_password_wrong')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,data=json.loads(data))
        self.assertEqual(res.text,expect_res)



if __name__ == '__main__':
    unittest.main(verbosity=2)