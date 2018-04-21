

class WebSocketHandler(object):

    def __init__(self):
        self.websockets = {}

    def add_user(self, used_id, ws):
        self.websockets[used_id] = ws

    def send_message(self, user_id, message):
        self.websockets[user_id].send(message)

    def send_message_to_all(self, user_ids, message):
        for user_id in user_ids:
            self.websockets[user_id].send(message)


