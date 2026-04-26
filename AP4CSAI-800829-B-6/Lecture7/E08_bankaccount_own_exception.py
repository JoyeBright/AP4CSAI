
# your own customized class
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        # Exception.__init__(self, f"cannot withdraw {amount} from {balance}")
        super().__init__(f"cannot withdraw {amount} from {balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError (self.balance, amount)
        self.balance -= amount

account = BankAccount(1000)
try:
    account.withdraw(1500)
except InsufficientFundsError as e:
    print("Transaction failed: ", e)

