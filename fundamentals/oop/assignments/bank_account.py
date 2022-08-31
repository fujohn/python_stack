class BankAccount:
    all_accounts = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        # your code here
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
    
    def display_account_info(self):
        # your code here
        print('Balance: $' + str(self.balance))
        return self
    
    def yield_interest(self):
        # your code here
        self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def display_all_balances(cls):
        for account in cls.all_accounts:
            print(account.int_rate)
            print(account.balance)

test_1 = BankAccount()
test_2 = BankAccount(0.02, 0)

test_1.deposit(10).deposit(100).deposit(1001).withdraw(111).yield_interest().display_account_info()
test_2.deposit(100).deposit(1000).withdraw(900).withdraw(50).withdraw(45).withdraw(110).yield_interest().display_account_info()

test_1.display_all_balances()