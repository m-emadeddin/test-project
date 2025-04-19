import Creature

class Human(Creature.Creature):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

    def __str__(self): 
        return f"Human: {self.name} (Health: {self.health}, Attack: {self.attack}, Defense: {self.defense})"