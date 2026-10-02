class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance


    def deposit(self,amount):
        if amount >0:
            self.__balance  += amount

    def withdraw(self, amount):
        if 0<amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid Withdrawl")

    def get_balance(self):
        print("The Current balance is ", self.__balance)

acc1 = BankAccount("Pappu",10000)
acc1.get_balance()

acc1.deposit(700)
acc1.get_balance()

acc1.withdraw(1000)
acc1.get_balance()


