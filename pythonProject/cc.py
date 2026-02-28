# -*- coding: utf-8 -*-
# @Author : 测试小牛
# @Time : 07/09/2023 22:24
# 自动化请求文件
from flask import Flask, request, jsonify

app = Flask(__name__)
users = []

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    for user in users:
        if user['username'] == username:
            return jsonify({'message': 'Username already exists.'}), 400

    user = {
        'username': username,
        'password': password
    }
    users.append(user)

    return jsonify({'message': 'User registered successfully.'}), 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                return jsonify({'message': 'Login successful.'}), 200
            else:
                return jsonify({'message': 'Invalid password.'}), 401

    return jsonify({'message': 'Username not found.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)  # 允许来自所有IP的访问并监听6000端口