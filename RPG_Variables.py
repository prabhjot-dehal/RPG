__author__ = 'prabh_000'
from RPG_imports import *


with open("ITEMS.txt", "r") as f:
    file = f.read()
items = file.split("\n")
for i in range(0, len(items)):
    items[i] = items[i].split(",")
print(items)

players = {}
players_list = []
classes = ["Fighter", "Mage", "Archer", ]
classes1 = ["Class1 : Fighter", "Class2 : Mage", "Class3 : Archer"]
level = 1