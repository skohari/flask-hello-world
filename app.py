from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/hw')
def index():
    return 'Hello, World! 3'


@app.route('/')
def greet():
    time = datetime.now().hour
    if time >= 0 and time < 12:
        return 'Good Morning!'
    elif time >= 12 and time < 16:
        return 'Good Afternoon!'
    else:
        return 'Good Evening! The time is ' + str(time)
