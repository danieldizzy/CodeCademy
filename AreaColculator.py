"""In this project, you'll create a calculator than can compute the area of a given shape, as selected by the user. The calculator will be able to determine the area of the following shapes:

Circle
Triangle
Square
The program should do the following:

Prompt the user to select a shape
Depending on the shape the user selects, calculate the area of that shape
Print the area of that shape to the user """

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print("The calculator is starting up")
print('%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute))

sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
option = input("Enter C for Circle or T for Triangle or S for Square: ")
option.upper()

if option == 'C':
    # float is used to convert to a floating point number
    radius = float(input("Enter the radius: "))
    area = pi * radius ** 2
    print("The pie is baking... ")
    sleep(1)
    print(area)
    print("Area: %.2f. \n%s" % (area, hint))

elif option == "T":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = (0.5 * base) * height
    print("Uni Bi Tri...")
    sleep(1)
    print("Area: %.2f. \n%s" % (area, hint))

elif option == "S":
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    area = width * height
    print("Calc...")
    sleep(1)
    print(area)
else:
    print("Error! Invalid shape selector specified. Exiting")
