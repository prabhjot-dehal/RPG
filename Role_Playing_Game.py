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


start()


def game():
    dungeon = Floor()


players_list[1].player_inventory.player_items.append(items[0])
players_list[1].player_inventory.player_items.append(items[1])
players_list[1].player_inventory.player_items.append(items[2])
players_list[1].player_inventory.player_items.append(items[3])

players_list[1].player_inventory.display_items()