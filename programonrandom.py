import random

playing = True
number = str(random.randint(0,9))
print("I will generate a number from 0 to 9, and u have to guess the number 1 digit at a time.")
print("The game ends when u get one hero")

while playing:
    guess = input("Give me your best guess:")

    if number ==guess:
        print("You win the game")
        print("The number was:", number)
        break
    else:
        print("Your guess is not quite right, try again")

