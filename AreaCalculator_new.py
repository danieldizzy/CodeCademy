""" In this project, you'll create a calculator than can compute the area of a given shape, as selected by the user. The calculator will be able to determine the area of the following shapes:

Circle
Triangle
The program should do the following:

Prompt the user to select a shape
Depending on the shape the user selects, calculate the area of that shape
Print the area of that shape to the user """

from math import pi
from time import sleep
from datetime import datetime
# use the datetime.now() function to retrieve the current date and time. Store the result into a variable called now.
now = datetime.now()
print("The Calculator is Starting Up ...")
print('%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)
hint = 'Don\'t forget to include the correct units! \nExiting..'
option = input('Enter C for Circle or T for Triangle or S for Square :')
option.upper()

# Use an if statement that will check if the option the user entered is C (for circle)
if option == 'C':
    radius = float(input('Enter the Radius: '))
    area = pi * radius ** 2
    print('The Pie is baking...')
    sleep(1)
    print('Are: %.2f. \n%s ' % (area, hint))

# Use an if statement that will check if the option the user entered is T (for Triangle)
elif option == 'T':
    base = float(input('Enter the base: '))
    height = float(input('Enter the height: '))
    area = (0.5 * base) * height
    print('Uni Bi Tri...')
    sleep(1)
    print('Area: %.2f. \n%s' % (area, hint))

# Use an if statement that will check if the option the user entered is S (for Square)
elif option == 'S':
    width = float(input('Enter the width: '))
    height = float(input('Enter the height: '))
    area = width * height
    print('Build a Square!...')
    sleep(1)
    print('Area: %.2f. \n%s' % (area, hint))
else:
    print('Invalid Shape Argument: ')




