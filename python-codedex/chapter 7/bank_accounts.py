class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    print(f"Your balance is: {self.balance}")

  def withdraw(self, amount):
    self.balance -= amount
    print(f"You have withdrawn: {amount}")
    print(f"Current balance: {self.balance}")

  def display_amount(self):
    print(self.balance)

kenneth = BankAccount("Kenneth", "Hernandez", 12312, "Debit", 121, 100.5)
kenneth.deposit(96)
kenneth.withdraw(25)
kenneth.display_amount()