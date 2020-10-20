from models.split import Split

class ExactSplit(Split):
    def __init__(self, user, amount=None):
        super().__init__(user, amount=amount)
