class Createure:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} (Health: {self.health} ---- Attack: {self.attack}, Defense: {self.defense})"