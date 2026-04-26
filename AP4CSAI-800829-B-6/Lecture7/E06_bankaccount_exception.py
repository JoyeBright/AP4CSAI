class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError ("Insufficient funds")
        self.balance -= amount

acc = BankAccount(100)
acc.withdraw(150)

print("Balance:", acc.balance)
print("Program continues...")