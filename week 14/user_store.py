class UserStore:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_data):
        self.users[user_id] = user_data

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def list_users(self):
        return list(self.users.keys())