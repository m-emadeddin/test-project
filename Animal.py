import creature

class Animal(creature.Creature):
    def __init__(self, name, species, age, habitat):
        super().__init__(name, species, age)
        self.habitat = habitat

    def make_sound(self):
        return f"{self.name} makes a sound."

    def __str__(self):
        return f"{self.name} is a {self.species} aged {self.age} living in {self.habitat}."