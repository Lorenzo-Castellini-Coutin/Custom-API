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
        user_sigin = request.get_json()
        return Users().userLogin(user_sigin)
    else:
        return jsonify('Method not allowed.'), 405
    

@app.route('/app/users/<user_id>', methods = ['GET', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'GET':
        return Users().getUserById(user_id, request.args)
    elif request.method == 'DELETE':
        return Users().deleteUser(user_id, request.args)
    elif request.method == 'PUT':
        update_user = request.get_json()
        return Users().updateUser(update_user, user_id, request.args)
    else:
        return jsonify('Method not allowed.'), 405
    

@app.route('/app/messages', methods = ['POST', 'PUT'])
def new_messages():
    if request.method == 'POST':
        new_message = request.get_json()
        return Messages().sendNewMessage(new_message, request.args)
    else:
        return jsonify('Method not allowed.'), 405
    

@app.route('/app/inbox/<recipient_user_id>', methods = ['GET'])
def inbox(recipient_user_id):
    if request.method == 'GET':
        return Messages().getInbox(recipient_user_id, request.args)
    else:
        return jsonify('Method not allowed.'), 405


@app.route('/app/sent/<sender_user_id>', methods = ['GET'])
def sent(sender_user_id):
    if request.method == 'GET':
        return Messages().getSent(sender_user_id, request.args)
    else:
        return jsonify('Method not allowed.'), 405


@app.route('/app/messages/<message_id>', methods = ['GET', 'DELETE', 'PUT'])
def messages(message_id):
    if request.method == 'GET':
        user_id = request.get_json()
        return Messages().getMessageById(user_id, message_id, request.args)
    elif request.method == 'DELETE':
        user_id = request.get_json()
        return Messages().deleteMessage(user_id, message_id, request.args)
    elif request.method == 'PUT':
        modify_message = request.get_json()
        return Messages().updateMessage(modify_message, message_id, request.args)
    else:
        return jsonify('Method not allowed.'), 405











#Author: Lorenzo Castellini Coutin