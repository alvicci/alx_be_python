class BankAccount:
    """
    A simple BankAccount class that supports balance management operations
    such as deposit, withdrawal, and balance display. Encapsulates the 
    account balance using property decorators for controlled access.
    """
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    @property
    def account_balance(self):
        """
        Getter method to retrieve the current account balance.

        Returns:
            int or float: The current balance in the account.
        """
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        """
        Setter method to update the account balance.

        Args:
            account_balance (int or float): The new balance to set.
        """
        self.__account_balance = account_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (int or float): The amount to deposit.
        """
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Attempts to withdraw the specified amount from the account.

        Args:
            amount (int or float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False if insufficient funds.
        """
        if self.__account_balance > amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Displays the current account balance to the console.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
