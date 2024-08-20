import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

class Player(Character):
    def __init__(self, name, health, attack, defense, level=1, experience=0):
        super().__init__(name, health, attack, defense)
        self.level = level
        self.experience = experience

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 2
        self.defense += 2
        self.experience = 0
        print(f"{self.name} leveled up to level {self.level}!")

class Enemy(Character):
    def __init__(self, name, health, attack, defense, experience_value):
        super().__init__(name, health, attack, defense)
        self.experience_value = experience_value

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        player.attack_enemy(enemy)
        if enemy.is_alive():
            enemy.attack_enemy(player)
        print(f"{player.name} has {player.health} health left.")
        print(f"{enemy.name} has {enemy.health} health left.")
    if player.is_alive():
        print(f"{player.name} defeated {enemy.name}!")
        player.gain_experience(enemy.experience_value)
    else:
        print(f"{player.name} was defeated by {enemy.name}...")

if __name__ == "__main__":
    player = Player(name="Hero", health=100, attack=20, defense=10)
    enemy = Enemy(name="Goblin", health=50, attack=15, defense=5, experience_value=50)
    battle(player, enemy)