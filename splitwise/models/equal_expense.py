from models.expense import Expense

class EqualExpense(Expense):
    def __init__(self, paid_by, amount, splits, expense_metadata):
        super().__init__(paid_by, amount, splits, expense_metadata)
        self.validate()


    def validate(self):
        pass
        
        

