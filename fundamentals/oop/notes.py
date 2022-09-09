# Classes
class User:
    pass    # we'll fill this in shortly

michael = User()
anna = User()

#################################################
# Constructors and Defaulted Attributes
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

# For the most part, you'll create your object instances outside the class definition, in the outer or global scope. i.e have its own file
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
user_ada = User()
print(user_ada.first_name) # prints Ada

#################################################
# Assigning Attributes
class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
    # the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats


#################################################
# Methods
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
    
adrien.greeting()
# prints Hello, my name is Adrien
    
cool_person.greeting()
# prints Hello, my name is Sadie


#################################################
# Updating Attributes
class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)


skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
skater_shoe.on_sale_by_percent(0.1)
print(skater_shoe.price)

#################################################
# class and static methods
class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


#################################################
# association between classes
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

class User:
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        # or access its attributes
        print(self.account.balance)


#################################################
# oop & dicts

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position) # prints small forward

#################################################
# Inheritance

class CheckingAccount(BankAccount): # BankAccount is the parent class
    pass     # 100% of BankAccount attributes and methods copied to CheckingAccount

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	# take the methods from parent's init for int_rate and balance
        self.is_roth = is_roth	

# If bank account has method like this
class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

# inheriting this will and adding is_early logic will look like this
class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
    	    amount = amount * 1.10
        super().withdraw(amount)
        return self
        
#################################################
# Modules & Packages

# import the library
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

from my_package.subdirectory import my_functions # package = collections of modules

# directory where my_module is the package
sample_project
     |_____ python_file.py
     |_____ my_modules
               |_____ __init__.py
               |_____ test_module.py
               |_____ another_module.py
               |_____ third_module.py

# if importing test_module from python_file.py
import my_modules.test_module # OR
from my_modules import test_module

# __init__.py required for Python 2.7
# to restrict importing of packages, do this
__all__ = ["test_module"] # would only allow test_module to be imported


#################################################
# Polymorphism

class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")

class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")

dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!


# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError

# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
        
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")


#################################################
# Input and Outputs
favorite_color = input('What is your favorite color? ') # input takes a prompt, which needs to be a string
print(f'Your favorite color is: {favorite_color}') #output, prints the color given to the console 😊



