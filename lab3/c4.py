class Bankaccount:
    def __init__(self):
        self.owner=input()
        self.balance=0
    def deposit(self):
        self.deposited=int(input())
        self.balance=+self.deposited
        print(self.balance)
    def withdraw(self):
        self.withdrawed=int(input())
        if self.withdrawed>self.balance:
            print("not enough money")
        else:
            self.balance-=self.withdrawed
        print(self.balance)
zxc=Bankaccount()
zxc.deposit()
zxc.withdraw()        