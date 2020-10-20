class User(object):
    def __init__(self, user_id, name, email, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone

    def _get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

