__author__ = 'prabh_000'
from RPG_imports import *



class Enemies:
    choices = ["norm", "miss", "crit"]
    hp = 0
    strength = 0
    attack = 0
    defence = 0

    def __init__(self, difficulty):
        self.hp = (difficulty * level) / 2
        self.strength = (5 / 4) * difficulty
        self.attack = difficulty
        self.defence = (5 / 4) * difficulty

    def hit(self):
        move = random.randint(0, 100)
        if move > 0 and move < 50:
            move = self.choices[0]  # norm hit
        elif move > 50 and move < 75:
            move = self.choices[1]  # miss hit
        elif move > 75 and move < 100:
            move = self.choices[2]  # crit hit

        target = players_list[random.randint(0, 3)]


class Floor:
    difficulty = 0
    enemies = []
    no_enemies = 0

    def __init__(self):
        self.difficulty = random.randint(1, 3)
        self.enemies = []
        self.no_enemies = random.randint(4, 8)
        for i in range(0, self.no_enemies):
            self.enemies.append(Enemies(self.difficulty))

