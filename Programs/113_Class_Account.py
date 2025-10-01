class person(object):
    """doc"""
    age = 10
    def greet(self):
        print("Hello")

print(person.__doc__)

class Account(object):
    def __init__(self, holder, number, balance, credit_line = 1500):
        self.holder = holder
        self.number = number
        self.balance = balance
        self.credit_line = credit_line
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if (self.balance - amount < -self.credit_line):
            print("Insufficient balance")
            return False
        else:
            self.balance -= amount
            return True

    def transfer(self, target, amount):
        if (self.balance - amount < -self.credit_line):
            print("Insufficient balance")
            return False
        else:
            self.balance -= amount
            target.balance += amount
            return True

Account.holder = "Krutarth"
Account.number = "1234567890"
Account.balance = 1000
Account.credit_line = 1500

a = Account(Account.holder, Account.number, Account.balance, Account.credit_line)
a.balance
a.withdraw(1000)
a.credit_line
a.deposit(1000)
a.balance()
a.withdraw(200)
a.balance()
a.withdraw(1500)

b = Account("het", "1234567890", 1000, 1500)
b.transfer(a, 1000)
b.balance()
a.balance()