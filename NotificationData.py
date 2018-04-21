import json



class NotificationData(object):

    def __init__(self, data):
        data = json.loads(data)

        self.notification_type = data["type"]
        self.user_id = data["user"]
        if self.notification_type == "change_score":
            self.value = data["score"]
        elif self.notification_type == "coffee_now":
            self.value = True
        elif self.notification_type == "answer_invitation":
            self.value = data["accept_invitation"]
        else:
            print("invalid Notification type.")

    def get_user(self):
        return self.user_id

    def is_score_change_notification(self):
        return self.notification_type == "change_score"

    def is_coffee_now_notification(self):
        return self.notification_type == 'coffee_now'

    def is_invitation_notification(self):
        return self.notification_type == "answer_invitation"

    def get_coffee_score(self):
        return self.value if self.notification_type == "coffee" else -1

