from bottle import Bottle, static_file, run
from DBConnection import DBConnection
from NotificationData import NotificationData

app = Bottle()
database = DBConnection()

def onNotification(data):
    notification_data = NotificationData(data)
    if notification_data.is_coffee_now_notification():
        users = database.get_all_with_score_above(6)
        

    elif notification_data.is_invitation_notification():

    elif notification_data.is_score_change_notification():
        database.set_score(notification_data.get_user(), notification_data.get_coffee_score())




@app.get('/')
def index():
    return static_file("index.html", root= "")

if __name__ == '__main__':
    run(app, host="localhost", port=8080)

