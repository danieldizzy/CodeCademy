"""In this project, we'll build Rock-Paper-Scissors!

The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is
  """


from time import sleep
from random import randint
# Creating a list 'R', 'S', 'P' and storing it as string
options = ['R', 'S', 'P']
# Set the win or Loose messages
LOOSE_MESSAGE = 'You Lost!!'
WIN_MESSAGE = 'You Won !!'

# the function to decide the winner between parameters from the computer_choice and user_choice, and print some functions

def decide_winner(user_choice, computer_choice):
    print('You selected : %s ' % user_choice)
    print('Computer Selecting....')
    sleep(1)
    print('The Computer selected : %s' % computer_choice)
    print('Computer Selecting....')
    sleep(1)

    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print('It\'s a tie')
    elif user_choice_index == 0 and computer_choice_index == 2:
        print('You Win!!')
    elif user_choice_index == 1 and computer_choice_index == 0:
        print('You Win!!')
    elif user_choice_index == 2 and computer_choice_index == 1:
        print('You Win !!')
    elif user_choice_index > 2:
        print('Wrong Choice, Try again !!')
        return
    else:
        print('You Lost')


def play_rps():
    print('Welcome to the Rock Scissors Paper Game !!')
    user_choice = input('Select R for Rock, P for Paper, or S for Scissors: ')
    user_choice = user_choice.upper()
    # computer_choice = options[randint(0, 2)]
    computer_choice = options[randint(0, len(options) - 1)]
    decide_winner(user_choice, computer_choice)
play_rps()






# n = [3, 5, 7]
#
#
# def total(numbers):
#     result = 0
#     for i in numbers:
#         result = result + i
#     return result
# print total(n)
#
# def total1(numbers):
#     result = 0
#     for i in range (0,len(numbers)):
#         result += numbers[i]
#     return result
# print total1 (n)



