# bank_account.py

class BankAccount:
<<<<<<< HEAD
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
=======
    def __init__(self, initial_balance = 0):
>>>>>>> 861775cb4cf8cb226a1b7ab599d751adac6431a8
        self.account_balance = initial_balance

    def deposit(self, amount):
<<<<<<< HEAD
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds exist."""
=======
        self.account_balance = amount
    def withdraw(self, amount):
>>>>>>> 861775cb4cf8cb226a1b7ab599d751adac6431a8
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
<<<<<<< HEAD
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
=======
        print(f"Current Balance: ${self.account_balance}")
>>>>>>> 861775cb4cf8cb226a1b7ab599d751adac6431a8
