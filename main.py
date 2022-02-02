from email import message
from flask import Flask, render_template, request
from markupsafe import re
from database import Database
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def kecatko():
    if request.method == 'POST':
        data = request.form
        Database().insert_message(user=data['user'], message=data['message'])

    msg = Database().get_messages()
    print(msg)
    return render_template('chat.html', zpravy=msg)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')