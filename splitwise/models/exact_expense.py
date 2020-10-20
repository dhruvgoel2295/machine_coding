from models.expense import Expense

class ExactExpense(Expense):
    def __init__(self, paid_by, amount, splits, expense_metadata):
        super().__init__(paid_by, amount, splits, expense_metadata)
        self.validate()


    def validate(self):
        split_amount = 0
        for split in self.splits:
            split_amount += split.amount
        if not split_amount == self.amount:
            raise Exception("Splits not equal to total amount")

        

