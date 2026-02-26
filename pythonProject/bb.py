# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
