class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if amount<=0:
            print("the amount must be positive")
        else:
            self.balance+=amount
    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficient balance")
        elif amount<=0:
            print("amount must be positive")
        else:
            self.balance-=amount
    def show(self):
        print("Owner",self.owner)
        print("Balance",self.balance)

acc=BankAccount("Chala Gobena",50000)
acc2=BankAccount("Aanaa Abdela",5000)


acc2.deposit(6000)
acc.deposit(6000)

acc.withdraw(-500)
acc.show()
acc2.show()