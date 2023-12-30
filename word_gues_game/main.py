# To write a program that chooses a random word from the given list and the user answers it
# If user fails more than 10 time answering the question he is out 

import random 

list_of_words = ["cat","doge","animal","bull","peacock","lioness"]
random_word = random.choice(list_of_words)

chance = 0
while chance<11:
    user_choice = str(input("Enter word: "))
    if user_choice != random_word:
        print("Wrong Guess")
        print("Hint: The lenght of the word is",len(random_word))
        chance = chance + 1
        print("")
    else:
        print("You Won")
        break

#By - VimKidCodz

