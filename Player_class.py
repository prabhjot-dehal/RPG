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
            pos_str = "ITEM "+str(position + 1)
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
        player_class = ui_input("Pick a  Warrior Class [1-3]")
        check = validate_num(player_class)

        while check == "False":
            ui("Not a Number")
            player_class = ui_input("Pick a  Warrior Class [1-3]")
            check = validate_num(player_class)

        check = int(check)

        while check > 3 or check < 1:
            ui("Not Between 1 and 3")
            player_class = ui_input("Enter Again : ")
            check = player_class

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
        elif player_class == "Mage":
            self.hp = self.level * 15
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 3
            self.luck = random.randint(2, 4)
            self.combat_level = self.strength + self.attack + self.defense
        elif player_class == "Archer":
            self.hp = self.level * 15
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 5
            self.luck = random.randint(1, 2)
            self.combat_level = self.strength + self.attack + self.defense
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


