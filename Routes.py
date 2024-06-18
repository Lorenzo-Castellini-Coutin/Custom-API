from flask import Flask, jsonify, request
from Controllers import Users, Messages

app = Flask(__name__)

@app.route("/app")
def hello():
    return "Welcome!"

@app.route("/app/adduser", methods=['POST'])
def new_user():
    if request.method == 'POST':
        new_user_data = request.get_json()
        Users.addNewUser(new_user_data)

@app.route("/app/getuserbyid", methods=['POST'])
def get_user_by_id():
    if request.method == 'POST':
        userid_data = request.get_json()
        Users.getUsersById(userid_data)

@app.route("/app/getuserbyemail", methods=['GET']) 
def get_user_by_email():
    pass

@app.route("/app/sendmessage", methods=['POST'])
def send_message():
    if request.method == 'POST':
        message = request.get_json()
        Messages.sendNewMessage(message)


@app.route("/app/deletemessage", methods=['GET'])
def delete_message():
    pass

