from calendar import c


class BankAccount:
    all_accounts = []

    # don't forget to add some default values for these parameters!
    def __init__(self, user='unassigned', int_rate=0.01, balance=0, account_type='Checking'): 
        # your code here! (remember, instance attributes go here)
        self.user = user
        self.int_rate = int_rate
        self.balance = balance
        self.account_type = account_type
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
        print(f'User: {self.user}, {self.account_type} Balance: ${self.balance}')
        return self
    
    def yield_interest(self):
        # your code here
        self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def display_all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()


###############################################################

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
    
    def open_bank_account(self, amount=0, interest=0.01, account_type='Checking'):
        self.accounts[account_type] = BankAccount(self.name, interest, amount, account_type)
    
    def make_deposit(self, amount, account_type):
        # your code here
        self.accounts[account_type].deposit(amount)
        print(self.accounts[account_type].balance)
        return self

    def make_withdrawal(self, amount, account_type):
        self.accounts[account_type].withdraw(amount)
        print(self.accounts[account_type].balance)
        return self

    def display_user_balances(self):
        for account_info in self.accounts.values():
            account_info.display_account_info()
        return self

    def transfer_money(self, amount, other_user):
        if len(other_user.accounts) < 1:
            print('No Accounts to transfer to')
        else:
            self.make_withdrawal(amount, 'Checking')
            other_user.make_deposit(amount, 'Checking') # what happens if no checking account?

test = User('John', 'abc@def.com')
test.open_bank_account(1100)
test.open_bank_account(3000, 0.02, 'Savings')
test.make_withdrawal(100, 'Checking')
test.display_user_balances()

test_2 = User('Jeff', '123@gmail.com')
test_2.open_bank_account()
test.transfer_money(100, test_2)
test.display_user_balances()
test_2.display_user_balances()
