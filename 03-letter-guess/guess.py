# Mostafa Asef Agah
# letter guess game

import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


words = [
    'blackberry', 'cherry', 'grapefruit', 'peach', 'strawberry', 'pineapple',
    'wrench', 'screwdriver', 'hammer', 'workbench', 'september', 'november',
    'march', 'october', 'brown', 'green', 'yellow', 'architect', 'astronomer',
    'butcher', 'dentist', 'engineer', 'gardener', 'lecturer', 'mechanic'
]

# get a random word
current_word = words[random.randint(0,len(words)-1)]

allowed_tries = 5

invalid_guesses = []

valid_guesses = []

game_finished = False
while not game_finished:
    cls()
    if invalid_guesses: print("Invalid Guessed letters are: {}".format(invalid_guesses))
    print("Remaining tries: {}".format(allowed_tries))

    # show guessed letters
    correct_letters_count = 0
    for letter in current_word:
        if letter in valid_guesses:
            print(letter, end='')
            correct_letters_count +=1
        else:
            print("-", end='')
    print()

    # is word guessed?
    if correct_letters_count == len(current_word):
        print("Congrats, You have guessed our word: '{}'".format(current_word))
        game_finished = True
    else:
        # get next guess
        guess = input("What is your next guess: ")

        if guess.isalpha():
            # is guessed letter in word?
            if guess[0].lower() in current_word:
                valid_guesses.append(guess)
            elif guess[0].lower() not in invalid_guesses:
                invalid_guesses.append(guess)
                allowed_tries -= 1

            # is user finished all tries?
            if allowed_tries <= 0:
                print("You have failed to guess the word. It was '{}'".format(current_word))
                game_finished = True


