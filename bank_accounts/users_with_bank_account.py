
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name = name, int_rate = .05, balance = 0)
        
    def deposit_account(self, amount):
        self.account.balance += amount
        return self

    def withdraw_account(self, amount):
        self.account.balance -= amount
        return self

    def transfer_account(self, name, amount):
        self.account.balance -= amount
        name.account.balance += amount
        print(self.account.balance.display(), name.account.balance.display())
        return self

    def display_account(self):
        print(self.account.balance)
        return self

    def yield_account(self):
        interest = self.account.balance * self.account.balance.int_rate
        self.account.balance += interest
        return self


class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = .07
        self.balance = 0
        

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit = ${amount}')
        print(f'Account Balance = ${self.balance}')
        return self

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Withdraw = ${amount}')
        print(f'Account Balance = ${self.balance}')
        return self

    def display(self):
        print(f"{self.name} Your balance is {self.balance}")
        return self

    def transfer(self, otheraccount, amount):
        print(f"{self.name} gave ${amount} to {otheraccount.name}")
        self.withdraw(amount)
        otheraccount.deposit_account(amount)
        return self

    def yield_int(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        print(f'Balance with interest = ${self.balance}')
        return self


david = User('David Pitz', 'dp@gmail.com')
kelly = User('Kelly pitz', 'kp@gmail.com')
jon = User('jon smith', 'js@gmail.com')



# kelly.deposit_account(100).display_account().withdraw_account(50).display_account()
# kelly.account.deposit(100).display().withdraw(50).yield_int().display()
kelly.account.deposit(100).withdraw(50).yield_int().transfer(david, 10)
david.account.display().deposit(1000000000000000000)