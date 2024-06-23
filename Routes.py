from flask import Flask, jsonify, request
from Controllers.Users import Users
from Controllers.Messages import Messages

app = Flask(__name__)

@app.route('/app')

@app.route('/app/adduser', methods = ['POST'])
def add_user():
    if request.method == 'POST':
        user_data = request.get_json()
        Users().addNewUser1(user_data)
        return jsonify({'Message' : 'Data received succesfully'}), 200
    else:
        return jsonify({'Message' : 'Data not received properly...'}), 405

@app.route('/app/getuserbyemail', methods = ['GET'])
def get_user_by_email():
    if request.method == 'GET':
        user_data = request.get_json()
        user_email = user_data['email']
        user_info = Users().getUserByEmail1(user_email)
        if user_info:
            return jsonify(list(user_info)), 200
        else:
            return jsonify({'Message' : 'User not found....'}), 405
    else:
        return jsonify({'Message': 'Incorrect method....'}), 405

@app.route('/app/getuserbyid', methods = ['GET'])
def get_user_by_id():
    if request.method == 'GET':
        user_data = request.get_json()
        user_id = user_data['user_id']
        user_info = Users().getUsersById1(user_id)
        if user_info:
            return jsonify(list(user_info)), 200
        else:
            return jsonify({'Message' : 'User not found...'}), 405
    else:
        return jsonify({'Message' : 'Incorrect method....'}), 405

@app.route('/app/sendnewmessage', methods = ['POST'])
def send_new_message():
    if request.method == 'POST':
        new_message = request.get_json()
        Messages().sendNewMessage1(new_message)
        return jsonify({'Message' : 'Message sent successfully'}), 200
    else:
        return jsonify({'Message' : 'Message not sent properly...'}), 405
    
@app.route('/app/getmessagebyid', methods = ['GET'])
def get_message_by_id():
    if request.method == 'GET':
        user_data = request.get_json()
        message_id = user_data['message_id']
        message_info = Messages().getMessageById1(message_id)
        if message_info:
            return jsonify(list(message_info)), 200
        else:
            return jsonify({'Message' : 'Message not found...'}), 405
    else:
        return jsonify({'Message': 'Incorrect method.....'}), 405

@app.route('/app/deletemessage', methods = ['GET'])
def delete_message():
    if request.method == 'GET':
        del_message = request.get_json()
        Messages().deleteMessage1(del_message)
        if del_message:
            return jsonify({'Message': 'Message deleted successfully'}), 200
        else:
            return jsonify({'Message': 'Message not found....'}), 405
    else:
        return jsonify({'Message' : 'Incorrect method...'}), 405
        