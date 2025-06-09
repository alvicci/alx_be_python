class BankAccount(object):
    """
    A simple BankAccount class that supports balance management operations
    such as deposit, withdrawal, and balance display. Encapsulates the 
    account balance using property decorators for controlled access.
    """
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        self.__account_balance = account_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance > amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: $[{self.__account_balance}]")

# Creating a class with no encapsulation
# 
# 
# class BankAccount:
#     def __init__(self, account_balance):
#         self.account_balance = account_balance
# test = BankAccount(10)
# test.account_balance = 20
# print(test.account_balance)