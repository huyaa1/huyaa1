# -*- coding: utf-8 -*-            
# @Author : 测试小牛
# @Time : 03/09/2023 13:22
import unittest
from ddt import ddt, data
import requests


@ddt
class LoginTestCase(unittest.TestCase):
    def setUp(self):
        # 执行测试前的准备工作，在每个测试方法执行前都会调用
        print("setUp() method is called.")

    def tearDown(self):
        # 执行测试后的清理工作，在每个测试方法执行后都会调用
        print("tearDown() method is called.")
    #数据源
    @data(["user1", "password1"],
          ["user2", "password2"],
          ["user3", "password3"])
    def test_login(self, data):
        username, password = data
        url = "http://117.72.72.134:6000/api/login"
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=payload)
        print(username)
        print(password)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()