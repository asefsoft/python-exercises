# Mostafa Asef Agah
# dungeon and dragon game

import random
import os

dimension = -1


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# get a random position on game's board for user, dragon and door with no overlap
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


# show game board to user
def show_game_board():
    for row in range(dimension * 2 + 1):
        for col in range(dimension * 2 + 1):
            if row % 2 == 0:
                print("--", end='')
            else:
                if col % 2 == 0:
                    print("|", end='')
                else:
                    if [(row-1)/2, (col-1)/2] == user_position:
                        print(" X ", end='')
                    else:
                        print("   ", end='')
        print()


# get valid moves base on player position on game board
def get_valid_moves():
    valid_moves=[]
    if user_position[1] >= 1:
        valid_moves.append("Left")
    if user_position[1] <= dimension - 2:
        valid_moves.append("Right")
    if user_position[0] >= 1:
        valid_moves.append("Up")
    if user_position[0] <= dimension - 2:
        valid_moves.append("Down")

    return valid_moves


# move player position if it's valid move
def do_move(move_command):
    move_command = move_command.capitalize()
    # is valid move?
    if move_command in get_valid_moves():
        if move_command == "Left":
            user_position[1] -= 1
        if move_command == "Right":
            user_position[1] += 1
        if move_command == "Up":
            user_position[0] -= 1
        if move_command == "Down":
            user_position[0] += 1
        return True
    else:
        return False


# is player safe or hunted by dragon
def get_player_state():
    if user_position == dragon_position:
        print("\nooh Sorry!! you hunted by dragon!")
        return False
    elif user_position == door_position:
        print("\nCongrats! you found escape door and you are safe now!")
        return False

    return True


# play game until player command to exit the game
while True:

    cls()

    # get board size from user
    while dimension < 3 or dimension > 15:
        dimension = input("Please enter dimension of game board [3-15]")
        dimension = int(dimension) if dimension.isnumeric() else -1

    # get random position for door, dragon and user
    door_position   = get_rand_position()
    dragon_position = get_rand_position(door_position)
    user_position   = get_rand_position([door_position, dragon_position])

    is_player_safe = True

    # showing game board and start playing
    while is_player_safe:
        cls()
        # print(door_position, dragon_position, user_position)
        print("Valid moves are: {}".format(get_valid_moves()))

        show_game_board()

        move = input("\nPress enter your move: ")

        do_move(move)

        is_player_safe = get_player_state()

    # game finished, play another round?
    command = input("\nPress enter to play another round or enter 'exit' to exit the game: ")
    if command.lower() == "exit":
        exit(0)
    else:
        dimension = -1
