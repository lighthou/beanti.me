
class DBConnection(object):

    def __init__(self):
        self.db = {}

    def set_score(self, user, score):
        self.db[user] = score

    def get_score(self, user):
        return self.db[user]

    def get_all_with_score_above(self, score):
        return [user[0] for user in self.db.items() if user[1] > score]

