from flask import Flask, jsonify, request
from Controllers.Users import Users
from Controllers.Messages import Messages

app = Flask(__name__)

@app.route('/app')

@app.route('/app/adduser', methods=['POST'])
def add_user_input():
    if request.method == 'POST':
        user_data = request.get_json()
        Users().addNewUser1(user_data)
        return jsonify({'Message' : 'Data received succesfully'}), 200
    else:
        return jsonify({'Message' : 'Data not received properly'}), 405

@app.route('/app/getuserbyemail', methods=['GET'])
def get_user_by_email_input():
    if request.method == 'GET':
        user_email = request.get_json()
        user_info = Users().getUserByEmail1(user_email)
        return jsonify({user_info}), 200
    else:
        return jsonify({'Message': 'User not found...'}), 405

@app.route('/app/getuserbyid', methods = ['GET'])
def get_user_by_id():
    pass

@app.route('/app/sendnewmessage', methods = ['POST'])
def send_new_message():
    if request.method == 'POST':
        new_message = request.get_json()
        Messages().sendNewMessage(new_message)
        return jsonify({'Message' : 'Message sent successfully'}), 200
    else:
        return jsonify({'Message' : 'Message not sent properly'}), 405
    
@app.route('/app/deleteMessage', methods = ['GET'])
def delete_message():
    if request.method == 'GET':
        message = request.get_json()
        