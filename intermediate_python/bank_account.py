
class BankAccount:
    def __init__(self, initial_balance=100):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must not be 0 or less than 0.")
        if amount > self.balance:
            raise ValueError("Invalid amount. Balance not enough.")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must not be 0 or less than 0.")
        self.balance += amount