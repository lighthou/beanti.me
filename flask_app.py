from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO

from DBConnection import DBConnection

database = DBConnection()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on("coffee run")
def coffee_run(data):
    print("coffee run button")
    socketio.emit("Coffee", "Someone wants cofee")

@app.route("/index.js")
def index_jss():
    return send_from_directory("", "index.js")

@app.route("/")
def index():
    return send_from_directory('', "index.html")

if __name__ == '__main__':
    socketio.run(app, host="localhost", port=8030)