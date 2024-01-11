class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f"Balance amount after deposit {dep_amount} is {self.balance}")

    def withdraw(self, wit_amount):
        if wit_amount <= self.balance:
            self.balance -= wit_amount
            print(f"Balance amount after withdrawal {wit_amount} is {self.balance}")
        else:
            print("Insufficient funds!")

    def displayBalance(self):
        print(f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
        self.interest_amount = 0

    def deposit(self, dep_amount):
        super().deposit(dep_amount)
        self.calculateInterest()

    def calculateInterest(self):
        self.interest_amount = self.balance * (self.interest_rate / 100) / 365 * 30

    def displayBalance(self):
        super().displayBalance()
        print(f"Balance amount including interest: {self.balance + self.interest_amount}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, wit_amount):
        if wit_amount <= (self.balance + self.overdraft_limit):
            self.balance -= wit_amount
            print(f"The amount withdrawn {wit_amount} and balance: {self.balance}")
        else:
            print("Exceeds overdraft limit!")

    def displayBalance(self):
        super().displayBalance()
        print(f"Balance: {self.balance}")


savingaccount = SavingAccount("SA123", "John Doe", 1000, 2)
savingaccount.deposit(500)
savingaccount.withdraw(200)
savingaccount.displayBalance()

print("--------")

currentaccount = CurrentAccount("CA456", "Jane Smith", 2000, 500)
currentaccount.withdraw(1500)
currentaccount.displayBalance()
