from flask import Flask, jsonify, request
from Controllers.Users import Users
from Controllers.Messages import Messages

app = Flask(__name__)

@app.route('/app')

@app.route('/app/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        user_data = request.get_json()
        return Users().addNewUser(user_data)
    else:
        return jsonify('Method not allowed.'), 405
    
    
@app.route('/app/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        user_data = request.get_json()
        return Users().userLogin(user_data)
    else:
        return jsonify('Method not allowed.'), 405
    

@app.route('/app/users/<user_id>', methods = ['GET', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'GET':
        return Users().getUserById(user_id)
    elif request.method == 'DELETE':
        return Users().deleteUser(user_id)
    elif request.method == 'PUT':
        return Users().updateUser(request.get_json(), user_id)
    else:
        return jsonify('Method not allowed.'), 405
    

@app.route('/app/messages', methods = ['POST', 'PUT'])
def messages():
    if request.method == 'POST':
        new_message = request.get_json()
        return Messages().sendNewMessage(new_message)
    elif request.method == 'PUT':
        modify_message = request.get_json()
        return Messages().updateMessage(modify_message)
    else:
        return jsonify('Method not allowed.'), 405
    

@app.route('/app/messages/<message_id>', methods = ['GET', 'DELETE'])
def messages(message_id):
    if request.method == 'GET':
        return Messages().getMessageById(request.get_json(), message_id)
    elif request.method == 'DELETE':
        return Messages().deleteMessage(request.get_json(), message_id)
    else:
        return jsonify('Method not allowed.'), 405











#Author: Lorenzo Castellini Coutin