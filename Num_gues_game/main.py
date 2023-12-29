# Write  a program that generates a random number and allows the user to guess the number with clues

import random

number = random.randrange(0,12)
n=0
while (n <10): # Only 10 chances to guess
    usr_input = int(input("Guess a number between 0 to 12 "))
    if usr_input != number:
        print("Try again")
        n = n+1
        if usr_input > number:
            print("The number gussed is less than what you guessed\n")
        elif usr_input < number:
            print("The number gussed is more than what you gussed\n" )

    if usr_input == number:
        print("You won")
        n = n + 10 # add 10 to end the loop

Code by : VimKid
Ide :Vim
