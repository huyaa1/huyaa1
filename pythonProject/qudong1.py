# -*- coding: utf-8 -*-            
# @Author : 测试小牛
# @Time : 03/09/2023 13:30
# -*- coding: utf-8 -*-
# @Author : 测试小牛
# @Time : 03/09/2023 13:22
import unittest
import requests

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        # 执行测试前的准备工作，在每个测试方法执行前都会调用
        print("setUp() method is called.")

    def tearDown(self):
        # 执行测试后的清理工作，在每个测试方法执行后都会调用
        print("tearDown() method is called.")
    def test_login_user1(self):
        username = "user1"
        password = "password1"
        url = "http://117.72.72.134:6000/api/login"
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        print("11111")

    def test_login_user2(self):
        username = "user2"
        password = "password2"
        url = "http://117.72.72.134:6000/api/login"
        payload = {
            "username": username,
            "password": password

        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)

        print("2222222")
    def test_login_user3(self):
        print("333333")

        username = "user3"
        password = "password3"
        url = "http://117.72.72.134:6000/api/login"
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()