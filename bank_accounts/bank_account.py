class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = .07
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_int(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self

dave_account = BankAccount(.01,0)
kelly_account = BankAccount(.01,0)

dave_account.deposit(200).deposit(500).deposit(1000).withdraw(200).yield_int().display_account_info()

kelly_account.deposit(1000).deposit(1000).withdraw(100).withdraw(50).withdraw(100).withdraw(100).yield_int().display_account_info()
