class InsufficientfundsError(Exception):
    pass

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientfundsError("Not enough funds")
        self.balance -= amount
        print("Withdraw Successful")

try:
    acc = BankAccount(2000)
    acc.withdraw(7000)

except InsufficientfundsError as e:
    print("Transaction failed", e)
