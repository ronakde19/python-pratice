class Payment:
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print("Processing payment: ", self.amount)

class CreditcardPayment(Payment):
    def pay(self):
        print("Amount processed", self.amount, "with %2 FEE")

class UPI(Payment):
    def pay(self):
        print("UPI Amount processed", self.amount, "with NO FEE")

p1 = CreditcardPayment(500)
p1.pay()