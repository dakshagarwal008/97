import random

print ("Number Guessing Game")

number = random.randint(5,15)

chances = 0

print("Guess A Number Between 5 to 15")

while chances < 5:

    guess = int(input("Enter Your Guess:- "))

    if guess == number:
        print("Congratulations You Won !!")

        break
    elif guess < number:
        print("Your Guess Was Too Low . Guess A Higher Number")

    else :
        print("Your Guess Was High Low . Guess A Small Number")

    chances  = chances+1

    if not chances < 5:
        print("You Lose !! The Number is",number)