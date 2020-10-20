from models.expense import Expense

class PercentExpense(Expense):
    def __init__(self, paid_by, amount, splits, expense_metadata):
        super().__init__(paid_by, amount, splits, expense_metadata)
        self.validate()


    def validate(self):
        split_percent = 0
        for split in self.splits:
            split_percent += split.percent

        if not split_percent == 100:
            raise Exception("Total percent of splits not 100.")
        
        

