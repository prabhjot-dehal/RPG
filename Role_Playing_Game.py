__author__ = 'prabh_000'

from RPG_imports import *


new_page()


def generate_players():
    new_page()
    ui("Make and name your Players")
    player1 = Player()
    print("")
    ui("PLAYER 2")
    player2 = Player()
    print("")
    ui("PLAYER 3")
    player3 = Player()
    print("")
    ui("PLAYER 4")
    player4 = Player()
    player1.display_all_player_info()
    players["player1"] = player1
    players["player2"] = player2
    players["player3"] = player3
    players["player4"] = player4
    players_list.append(player1)
    players_list.append(player2)
    players_list.append(player3)
    players_list.append(player4)
    new_page()


def start():
    new_page()
    ui_title("Welcome to THE UNDER WORLD!!!")
    ui("[N] Any number to Play",
       "[L] Any letter to Quit")
    try:
        next = int(ui_input("Pick a choice"))
    except ValueError:
        ui("Too Scared? Goodbye")
        quit()
    generate_players()
    game()


def option():
    ui("[1]To attack",
       "[2]To win an Item",
       "[3]To use item")
    choice = ui_input("Pick a option")
    try:
        choice = int(choice)
    except ValueError:
        ui("Not a number Pick again")
        option()
    if choice not in [1, 2, 3]:
        ui("Not a choice, pick again")
        option()
    return choice





def win_item(player, dungeon):
    luck = players_list[player].luck
    chance = luck * 10
    missed = random.randint(0, 100)
    if chance > missed:
        item = random.randint(0, len(items))
        to_print = "You won a " + str(items[item][0])
        ui(to_print,
           items[item][1])
        players_list[player].player_inventory.player_items.append(items[0])
    elif chance < missed:
        ui("You didn't win a item")






def game():
    new_page()
    ui_title("Lets start playing!")
    dungeon = Floor()
    if len(players_list) > 0 and len(dungeon.enemies) > 0:
        for x in range(0, len(players_list)):
            thing_to_print = str(players_list[x].name) + "'s" + " turn to play!"
            ui(thing_to_print)
            choice = option()
            if choice == 1:
                players_list[x].attack(dungeon)
            elif choice == 2:
                win_item(x, dungeon)
        for i in range(0,len(dungeon.enemies)):
            to_print = "Enemy " + str(i) + "'s turn to attack"
            ui(to_print)
            dungeon.enemies[i].hit




    elif players_list > 0 >= len(dungeon.enemies):
        ui("You win")
    elif len(players_list) <= 0 < len(dungeon.enemies):
        ui("you lose")
    elif len(players_list) < 0 and len(dungeon.enemies) < 0:
        ui("draw")
    else:
        ui("HUGE ERROR!!!")

    level += 1
    game()

start()





