# 5.	Create a parent class BankAccount with a method deposit().
# Create two child classes, SavingsAccount and CurrentAccount,
# that override the deposit() method to include specific rules for each account type.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount < 500:
            print("Minimum deposit for Savings Account is 500.")
        else:
            super().deposit(amount)

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 100000:
            print("Maximum deposit for Current Account is 100,000.")
        else:
            super().deposit(amount)

savings = SavingsAccount("SA123", 1000)
savings.deposit(1000)
current = CurrentAccount("CA456", 5000)
current.deposit(50000)