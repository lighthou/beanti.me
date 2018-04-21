from bottle import Bottle, static_file, run, request, abort
from DBConnection import DBConnection
from WebSocketHandler import WebSocketHandler
from NotificationData import NotificationData
app = Bottle()
database = DBConnection()
webSockets = WebSocketHandler()
id = 1

def onNotification(data):
    notification_data = NotificationData(data)
    if notification_data.is_coffee_now_notification():
        users = database.get_all_with_score_above(6)
        webSockets.send_message_to_all(users, "Come Get Coffee!")

    elif notification_data.is_invitation_notification():
        return

    elif notification_data.is_score_change_notification():
        database.set_score(notification_data.get_user(), notification_data.get_coffee_score())


@app.get("/websocket")
def websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, "Websocket Request failed")

    # TODO: find user_id and register them in database as well.
    user_id = get_user_id(request.environ)
    webSockets.add_user(user_id, wsock)
    wsock.send("Connected properly on backend")
    print("got a websocket connection working")

def get_user_id(request):
    id +=1
    return id-1


@app.get("<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="")

@app.get("<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="")

@app.get('/')
def index():
   return static_file("index.html", root= "")


if __name__ == '__main__':
   run(app, host="localhost", port=8000)