# Problem statement in description

import random

def game():
    value = random.randint(0,50)

    chances = 5
    c = 1
    all_guesses = []
    print(value)
    while c <= 5:
        print("You have", chances-c+1, "left\n")
        
        guess = int(input("Guess the number: "))

        all_guesses.append(guess)
        
        if guess == value:
            print("Hurray! You guessed it")
            print("Guesses used", all_guesses)
            break
        else:
            print("Better Luck Next Time")

        c += 1

        print()
    else:
        print("Sorry! Game Over")

game()
