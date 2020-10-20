class Split(object):
    def __init__(self, user, amount=None):
        self.user = user
        self.amount = amount

    def set_amount(self, amount):
        self.amount = amount