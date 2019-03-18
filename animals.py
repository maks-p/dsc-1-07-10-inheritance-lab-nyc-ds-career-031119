class Animal(object):
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        ### Question: Why are these instance variables necessary if creating below in each sub class? ###
        self.size = None
        self.food_type = None
        self.nocturnal = False

    def sleep(self):
        if self.nocturnal:
            return f"{self.name} sleeps during the day."
        else:
            return f"{self.name} sleeps at night."

    def eat(self, food):
        if food == 'plants':
            if self.food_type == 'herbivore' or self.food_type == 'omnivore':
                return f"{self.name} the {self.species} thinks {food} is yummy!"
            else:
                return f"I don't eat this."
        else:
            if self.food_type == 'carnivore':
                return f"{self.name} the {self.species} thinks {food} is yummy!"
            else:
                return f"I don't eat this."

class Elephant(Animal):

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'elephant'
        self.size = 'enormous'
        self.food_type = 'herbivore'
        self.nocturnal = False


class Tiger(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'tiger'
        self.size = 'large'
        self.food_type = 'carnivore'
        self.nocturnal = True


class Raccoon(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'raccoon'
        self.size = 'small'
        self.food_type = 'omnivore'
        self.nocturnal = True


class Gorilla(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'gorilla'
        self.size = 'large'
        self.food_type = 'herbivore'
        self.nocturnal = False

zoo = []

def add_animal(animal_type, name, weight):
    animal = None
    if animal_type == 'Elephant':
        animal = Elephant(name, weight)
    elif animal_type == 'Tiger':
        animal = Tiger(name, weight)
    elif animal_type == 'Raccoon':
        animal = Raccoon(name, weight)
    else:
        animal = Gorilla(name, weight)
    
    zoo.append(animal)

add_animal('Gorilla', 'Steve', 1500)
add_animal('Elephant', 'Kevin', 2500)
add_animal('Elephant', 'Stampy', 2500)
add_animal('Raccoon', 'Rocky', 25)
add_animal('Raccoon', 'Ricky', 25)
add_animal('Tiger', 'Tony', 800)
add_animal('Tiger', 'Timmy', 800)
add_animal('Tiger', 'Ben', 800)

def feed_animals(zoo, time):

    for animal in zoo:
        
        if time == 'Day' and animal.nocturnal == False:
            if animal.food_type == 'carnivore':
                animal.eat('meat')
                print(f"{animal.name} the {animal.species} ate.")
            else:
                animal.eat('plant')
                print(f"{animal.name} the {animal.species} ate.")

        elif time == 'Night' and animal.nocturnal == True:
            if animal.food_type == 'carnivore':
                animal.eat('meat')
                print(f"{animal.name} the {animal.species} ate.")
            else:
                animal.eat('plant')
                print(f"{animal.name} the {animal.species} ate.")

feed_animals(zoo, 'Night')
