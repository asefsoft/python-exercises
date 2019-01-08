# Mostafa Asef Agah

import random

dimension = -1


while dimension < 3 or dimension > 15:
    dimension = input("Please enter dimension of game board [3-15]")
    dimension = int(dimension) if dimension.isnumeric() else -1
    print("Your chose is: {}".format(dimension))


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
                        print("  ", end='')
        print()


door_position   = get_rand_position()
dragon_position = get_rand_position(door_position)
user_position   = get_rand_position([door_position, dragon_position])

print(door_position, dragon_position, user_position)

show_game_board()

