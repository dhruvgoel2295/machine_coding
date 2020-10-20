from models.split import Split

class EqualSplit(Split):
    def __init__(self, user, amount=None):
        super().__init__(user)