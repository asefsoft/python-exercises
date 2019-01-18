# Mostafa Asef Agah
# dungeon and dragon game
# challenge 1: move player by arrow keys

# NOTE: to be able to play this game, after entering dimension,
# focus on 'tk' window then press Up Down Left Right keys

import random
import os

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# get a random position on game's board for player, dragon and door with no overlap
def get_rand_position(occupied_position=()):
    position = []

    if occupied_position:
        found_valid_position = False
        while not found_valid_position:
            position = [random.randint(0, dimension - 1), random.randint(0, dimension - 1)]
            found_valid_position = position not in occupied_position
    else:
        position = [random.randint(0, dimension - 1), random.randint(0, dimension - 1)]

    return position


# show game board to player
def show_game_board():
    cls()
    for row in range(dimension * 2 + 1):
        for col in range(dimension * 2 + 1):
            if row % 2 == 0:
                print("--", end='')
            else:
                if col % 2 == 0:
                    print("|", end='')
                else:
                    if [(row-1)/2, (col-1)/2] == player_position:
                        print(" X ", end='')
                    else:
                        print("   ", end='')
        print()


# get valid moves base on player position on game board
def get_valid_moves():
    valid_moves=[]
    if player_position[1] >= 1:
        valid_moves.append("Left")
    if player_position[1] <= dimension - 2:
        valid_moves.append("Right")
    if player_position[0] >= 1:
        valid_moves.append("Up")
    if player_position[0] <= dimension - 2:
        valid_moves.append("Down")

    return valid_moves


# move player position if it's valid move
def do_move(move_command):
    move_command = move_command.capitalize()
    # is valid move?
    if move_command in get_valid_moves():
        if move_command == "Left":
            player_position[1] -= 1
        if move_command == "Right":
            player_position[1] += 1
        if move_command == "Up":
            player_position[0] -= 1
        if move_command == "Down":
            player_position[0] += 1
        return True
    else:
        return False


# is player safe or hunted by dragon
def get_player_state():
    if player_position == dragon_position:
        print("\nooh Sorry!! you hunted by dragon!")
        return False
    elif player_position == door_position:
        print("\nCongrats! you found escape door and you are safe now!")
        return False

    return True


def is_arrow_key(key):
    return True if key in ("Up", "Down", "Right", "Left") else False


def key_pressed(event):

    # is up down ... keys pressed?
    if is_arrow_key(event.keysym):

        # move player on board base on pressed key
        do_move(event.keysym)

        # show game board
        show_game_board()

        # exit game if player found door or hunted by dragon!
        if not get_player_state():
            root.destroy()

    elif event.keysym == 'Escape':
        root.destroy()


# START GAME
cls()

dimension = -1

# get board size from player
while dimension < 3 or dimension > 15:
    dimension = input("Please enter dimension of game board [3-15]")
    dimension = int(dimension) if dimension.isnumeric() else -1

# get random position for door, dragon and player
door_position   = get_rand_position()
dragon_position = get_rand_position(door_position)
player_position   = get_rand_position([door_position, dragon_position])

show_game_board()

# start tkinter to capture keyboard key press events
root = tk.Tk()
root.bind_all('<Key>', key_pressed)
# don't show the tk window
# root.withdraw()
root.mainloop()



