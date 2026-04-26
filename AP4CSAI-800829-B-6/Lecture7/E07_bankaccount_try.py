class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError ("Insufficient funds")
        self.balance -= amount


account = BankAccount(1000)
try:
    account.withdraw(1500)
except ValueError as e:
    print("Transaction failed: ", e)

