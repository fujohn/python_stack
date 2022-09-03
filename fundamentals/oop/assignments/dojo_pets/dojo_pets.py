class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"{self.first_name} is taking {self.pet.name} on a walk")
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name} some {self.treats} and {self.pet_food}")
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"{self.first_name} is giving {self.pet.name} a bath")
        self.pet.noise()
        return self


class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"After sleeping, {self.name}'s energy is now {self.energy}")
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"After eating, {self.name}'s energy is now {self.energy} and health is now {self.health}")
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"After playing, {self.name}'s health is now {self.health}")
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(f'{self.name} is making {self.type} sounds.')
        return self

hammie = Pet('hammie', 'cat', 'sit', 100, 50)
karissa = Ninja('karissa', 'wong', 'jerky', 'wet food', hammie)

karissa.feed()
karissa.walk()
karissa.bathe()