from RPG_imports import *


class Inventory:
    def __init__(self):
        pass

    player_items = []

    def display_items(self):
        ui_title("YOUR ITEMS")
        ui(*self.player_items[0])

        position = 0

        run = True
        run1 = True

        while run:
            ui("[W]To Scroll Up.",
               "[S]To Scroll Down.")
            while run1:
                scroll = ui_input("Scroll : ")
                if scroll == "S":
                    if position < len(self.player_items) - 1:
                        position += 1
                    else:
                        ui("End of list")
                    run1 = False
                elif scroll == "W":
                    if position > 0:
                        position -= 1
                    else:
                        ui("Top of list")
                    run1 = False
                else:
                    ui("Not Valid Option")
            run1 = True
            new_page()
            pos_str = "ITEM " + str(position + 1)
            ui_title(pos_str)
            ui(self.player_items[position][0],
               self.player_items[position][1])


"""
        ui_title("YOUR ITEMS")
        for item in self.player_items:
            ui(*item)
            """


class Player:
    name = ""
    player_class = ""
    level = 1
    hp = 0
    strength = 0
    attack = 0
    defense = 0
    speed = 0
    luck = 0
    combat_level = 0
    player_inventory = Inventory()

    def __init__(self):
        name = ui_input("Name this player : ")
        border(inner_width=60, border_width=5, border_symbol="=")
        self.name = name

        ui("WARRIOR CLASSES", *classes1)
        check = False
        while not check:
            player_class = ui_input("Pick a  Warrior Class [1-3]")
            check = validate_num(player_class, 0, 4)


        player_class = int(player_class)
        player_class -= 1
        player_class = classes[player_class]

        self.player_class = player_class

        if player_class == "Fighter":
            self.hp = self.level * 20
            self.strength = self.level * 5
            self.defense = self.level * 5
            self.attack = self.level * 2
            self.speed = self.level * 2
            self.luck = random.randint(1, 2)
            self.combat_level = self.strength + self.attack + self.defense
            self.player_inventory.player_items.append(items[0])
            self.player_inventory.player_items.append(items[1])
        elif player_class == "Mage":
            self.hp = self.level * 15
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 3
            self.luck = random.randint(2, 4)
            self.combat_level = self.strength + self.attack + self.defense
            self.player_inventory.player_items.append(items[0])
            self.player_inventory.player_items.append(items[8])
        elif player_class == "Archer":
            self.hp = self.level * 15
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 5
            self.luck = random.randint(1, 2)
            self.combat_level = self.strength + self.attack + self.defense
            self.player_inventory.player_items.append(items[0])
            self.player_inventory.player_items.append(items[6])
        else:
            ui("HUGE ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def display_all_player_info(self):
        name = "Name : " + self.name
        level = "Level : " + str(self.level)
        player_class = "Class : " + self.player_class
        combat_level = "Combat level : " + str(self.combat_level)
        hp = "HitPoints : " + str(self.hp)
        strength = "Strength : " + str(self.strength)
        attack = "Attack : " + str(self.attack)
        defense = "Defense : " + str(self.defense)
        speed = "Speed : " + str(self.speed)
        ui_title(name)
        ui(player_class,
           level,
           combat_level,
           hp,
           strength,
           attack,
           speed,
           defense)


    def life_check(self):
        if self.hp >= 0:
            ui("Player killed")
        elif self.hp < 0:
            ui("Player still alive")

    def attack(self,dungeon):
        enemy = random.randint(0, len(dungeon.enemies))
        damage_done = (self.attack * self.strength * self.luck) / 3
        dungeon.enemies[enemy].hp -= damage_done
        thing_to_print = "You did " + str(damage_done) + " damage"
        ui(thing_to_print)
        dungeon.enemies[enemy].check_life()
        for i in range(0,len(dungeon.enemies)):
            if dungeon.enemies[i] == None :
                dungeon.enemies.pop(i)


