"""  We'll build a program that rolls a pair of dice and asks the user to guess a number. Based on the user's guess, the program should determine a winner. If the user's guess is greater than the total value of the dice roll, they win! Otherwise, the computer wins.

The program should do the following:

Randomly roll a pair of dice
Add the values of the roll
Ask the user to guess a number
Compare the user's guess to the total value
Decide a winner (the user or the program)
Inform the user who the winner is """


from random import randint
from time import sleep


def get_user_guess():
    user_guess = int(input("Guess a number: "))
    return user_guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(2, number_of_sides)
    max_val = number_of_sides * 2
    print("The Maximum Possible Value is: " + str(max_val))

    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print("No guessing higher than the maximum possible value!: ")
        return
    else:
        print("Rolling...")
        sleep(2)
        print("The first value is: %d " % first_roll)
        sleep(1)
        print("The Second value is: %d " % second_roll)
        total_roll = first_roll + second_roll
        print("Result... %d " % total_roll)
        if user_guess > total_roll:
            print("You Won !!")
            return
        else:
            print("You Lost !!")
            sleep(1)
            print("Better Luck Next Time...")
            return
roll_dice(6)













