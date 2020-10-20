from models.split import Split

class Expense(object):
    def __init__(self, paid_by, amount, splits, expense_metadata):
        self.paid_by = paid_by
        self.amount = amount
        self.splits = splits
        self.metadata = expense_metadata


    def validate(self):
        pass


