from flask import Flask, jsonify, request
from Controllers.Users import Users
from Controllers.Messages import Messages

app = Flask(__name__)

@app.route('/app')

@app.route('/app/register', methods = ['POST'])
def new_user():
    if request.method == 'POST':
        user_data = request.get_json()
        return Users().addNewUser1(user_data)
    else:
        return jsonify('Method not allowed.'), 405
    
@app.route('/app/login', methods = ['POST'])
def log_in():
    if request.method == 'POST':
        user_credentials = request.get_json()
    else:
        return jsonify('Method not allowed.'), 405

@app.route('/app/users/<int:user_id>', methods = ['GET', 'DELETE', 'PUT'])
def existing_users(user_id):
    if request.method == 'GET':
        return Users().getUsersById1(user_id)
    elif request.method == 'DELETE':
        return Users().deleteUsers1(user_id)
    elif request.method == 'PUT':
        return Users().updateUsers1(request.get_json())
    else:
        return jsonify('Method not allowed'), 405

@app.route('/app/new_messages', methods = ['POST'])
def new_message():
    if request.method == 'POST':
        new_message = request.get_json()
        return Messages().sendNewMessage1(new_message)
    else:
        return jsonify('Method not allowed.'), 405

@app.route('/app/messages/<int:message_id>', methods = ['GET', 'DELETE', 'PUT'])
def existing_messages(message_id):
    if request.method == 'GET':
        return Messages().getMessageById1(message_id)
    elif request.method == 'DELETE':
        return Messages().deleteMessage1(message_id)
    elif request.method == 'PUT':
        new_message = request.get_json()
        return Messages().updateMessage1(new_message)
    else:
        return jsonify('Method is not allowed.'), 405

