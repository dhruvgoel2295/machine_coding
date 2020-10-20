from models.percent_expense import PercentExpense
from models.exact_expense import ExactExpense
from models.equal_expense import EqualExpense
from models.user import User

class ExpenseService(object):

    def create_expense(self, paid_by, total_amount, splits, expense_type, expense_metadata):
        expense = None
        if expense_type == "EQUAL":
            split_amount = round( (total_amount*100/len(splits))/100.0, 2)
            for split in splits:
                split.set_amount(split_amount)
            amount_left = round((total_amount - split_amount*len(splits)), 2)
            splits[0].set_amount(split_amount + amount_left)
            expense = EqualExpense(paid_by, total_amount, splits, expense_metadata)

        elif expense_type == "EXACT":
            expense = ExactExpense(paid_by, total_amount, splits, expense_metadata)

        elif expense_type == "PERCENT":
            for split in splits:
                amount = round(((split.percent*total_amount)/100.0), 2)
                split.set_amount(amount)
            expense = PercentExpense(paid_by, total_amount, splits, expense_metadata)

        return expense

