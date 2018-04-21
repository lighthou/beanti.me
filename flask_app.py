from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO

from DBConnection import DBConnection

database = DBConnection()
clients = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on("coffee run")
def coffee_run():
    users = database.get_all_with_score_above(6)
    print(users)
    socketio.emit("Coffee", "Someone wants coffee", room=users[0])

@socketio.on("change score")
def change_score(data):
    print("data", data)
    print("{0} change".format(request.sid))
    database.set_score(request.sid, int(data))

@socketio.on("connected")
def connected():
    print("{0} connected".format(request.sid))
    database.set_score(request.sid, 0)


@app.route("/index.js")
def index_jss():
    return send_from_directory("", "index.js")



@app.route("/")
def index():
    return send_from_directory('', "index.html")

if __name__ == '__main__':
    socketio.run(app, host="localhost", port=8237)