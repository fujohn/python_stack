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

class Cat(Pet):
    def __init__(self, name, tricks, health, energy):
        super().__init__(name, 'cat', tricks, health, energy)
    
    def play(self):
        print(f"{self.name} went to chase squirrels")
        super().play()
        return self

    def noise(self):
        print("Cats don't like baths")
        super().noise()
        return self