
"""
     Boolean Operators
------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""


def using_one():
    if 13 < 10:
        return "This is true"
    elif 3 < 4:
        return "This is False"


def using_two():
    if 10 > 8:
        return "This is also true"


print(using_one())
print(using_two())


def using_control_once():
    if 13 > 10:
        return "This is true"
    elif 3 < 4:
        return "This is False"


def using_control_again():

    if 10 > 8:
        return "This is also true"

print(using_control_once())
print(using_control_again())

