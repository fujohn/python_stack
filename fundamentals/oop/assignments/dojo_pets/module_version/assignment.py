from ninja_mod import Ninja
from pet_mod import Pet, Cat

# hammie = Pet('hammie', 'cat', 'sit', 100, 50)
hammie = Cat('hammie', 'sit', 100, 50)
karissa = Ninja('karissa', 'wong', 'jerky', 'wet food', hammie)

karissa.feed()
karissa.walk()
karissa.bathe()