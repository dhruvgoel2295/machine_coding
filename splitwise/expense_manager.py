from models.user import User
from models.split import Split
from models.exact_split import ExactSplit
from models.equal_split import EqualSplit
from models.percent_split import PercentSplit
from models.expense import Expense
from models.exact_expense import ExactExpense
from models.equal_expense import EqualExpense
from models.percent_expense import PercentExpense
from services.expense_service import ExpenseService

class ExpenseManager(object):
    def __init__(self):
        self.balances = {}
        self.users = {}
        self.expenses = []
        self.expense_service = ExpenseService()

    def add_expense(self, paid_by, amount, splits, expense_type, expense_metadata):
        expense = self.expense_service.create_expense(paid_by, amount, splits, expense_type, expense_metadata)
        self.expenses.append(expense)
        self.update_balances(paid_by, splits)

    def update_balances(self, paid_by, splits):
        for split in splits:
            paid_to = split.user.user_id
            if paid_to == paid_by:
                continue
            if not paid_to in self.balances[paid_by]:
                self.balances[paid_by][paid_to] = 0
            if not paid_by in self.balances[paid_to]:
                self.balances[paid_to][paid_by] = 0
            self.balances[paid_by][paid_to] -= split.amount
            self.balances[paid_to][paid_by] += split.amount

    def show_balance(self, user_id):
        balances = self.balances[user_id]
        for uid, balance in balances.items():
            if balance > 0:
                print("%s owes %s: %f" % (user_id, uid, balance))
            else:
                print("%s owes %s: %f" % (uid, user_id, 0-balance))

    def show_all_balances(self):
        for owed_by, balance_sheets in self.balances.items():
            for owed_to, balance in balance_sheets.items():
                if balance > 0:
                    print("%s owes %s: %f" % (owed_by, owed_to, balance))


    def add_user(self, uid, name, email, phone):
        new_user = User(uid, name, email, phone)
        self.users[uid] = new_user
        self.balances[uid] = {}
        
