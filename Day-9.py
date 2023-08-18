##17.Create  classes to model a simple banking system with customers and accounts.
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawl Machine")

    def deposit(self):
        amount=float(input("Enter amount to be deposited:"))
        self.balance +=amount
        print("\n Amount Deposited:",amount)

    def withdraw(self):
        amount=float(input("Enter amount to be Withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdraw:",amount)
        else:
            print("\n Insufficient balance")
        
    def display(self):
            print("\n Net Available Balance=",self.balance)

s=Bank_Account()
s.deposit()
s.withdraw()
s.display()