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

