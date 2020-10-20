from models.split import Split
from models.equal_split import EqualSplit
from models.exact_split import ExactSplit
from models.percent_split import PercentSplit
from expense_manager import ExpenseManager
from models.expense_metadata import ExpenseMetadata

class Driver(object):
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.add_users()

    def add_users(self):
        self.expense_manager.add_user("u1", "name1", "email1", "phone1")
        self.expense_manager.add_user("u2", "name2", "email2", "phone2")
        self.expense_manager.add_user("u3", "name3", "email3", "phone3")
        self.expense_manager.add_user("u4", "name4", "email4", "phone4")

    def show_balance(self, command):
        if len(command) > 0:
            self.expense_manager.show_balance(command[0])
        else:
            self.expense_manager.show_all_balances()

    def add_expense(self, command):
        paid_by = command[0]
        amount = float(command[1])
        total_splits = int(command[2])
        users = command[3:3+total_splits]
        command = command[3+total_splits:]
        expense_type = command[0]
        command = command[1:]
        splits = []
        
        if expense_type == "EXACT":
            for i in range(len(users)):
                new_split = ExactSplit(self.expense_manager.users[users[i]], float(command[i]))
                splits.append(new_split)

        elif expense_type == "PERCENT":
            for i in range(len(users)):
                new_split = PercentSplit(self.expense_manager.users[users[i]], percent=float(command[i]))
                splits.append(new_split)

        elif expense_type == "EQUAL":
            for i in range(len(users)):
                new_split = EqualSplit(self.expense_manager.users[users[i]])
                splits.append(new_split)
        expense_metadata = ExpenseMetadata()
        self.expense_manager.add_expense(paid_by, amount, splits, expense_type, expense_metadata)

    def main(self):        
        command = str(input("Enter expense details:"))
        command = str(command)
        command = command.split(" ")
        command_type = command[0]
        if command_type == "EXPENSE":
            self.add_expense(command[1:])
        elif command_type == "SHOW":
            self.show_balance(command[1:])

driver_obj = Driver()
while True:
    driver_obj.main()

        
