from models.split import Split

class PercentSplit(Split):
    def __init__(self, user, amount=None, percent=None):
        super().__init__(user)
        self.percent = percent