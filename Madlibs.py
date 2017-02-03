"""
This is a program about Mad Libs
"""

print('The Program has begun')
name = input("What is your name: ")
first_adjective = input("Enter the first adjective: ")
second_adjective = input("Enter the second adjective: ")
third_adjective = input("Enter the third adjective: ")
first_verb = input("Enter the first verb: ")
second_verb = input("Enter the second verb: ")
third_verb = input("Enter the third verb: ")
first_noun = input("Enter the first noun: ")
second_noun = input("Enter the second noun: ")
third_noun = input("Enter the third noun: ")
fourth_noun = input("Enter the fourth noun: ")
animals = input("Enter an Animal: ")
food = input("Enter a Food: ")
fruit = input("Enter a Fruit: ")
number = input("Enter a number: ")
superhero = input("Enter a Superhero: ")
country = input("Enter a country: ")
desert = input("Enter a desert: ")
year = input("Enter a year: ")

# The template for the story

STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s. On the other "
"side of the" " %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of" \
        " the %s, which made all " "of the %s very %s. %s tried to %s into the sewers and found %s rats. " \
        "Needing help, %s quickly called %s. "  "%s  " "appeared and saved %s by flying to %s and dropping %s into a " \
        "puddle of %s. %s then fell asleep and woke up in  "  "the year %s, in a world where %ss ruled the world."
print(STORY % (first_adjective, name, first_verb, second_adjective, first_noun, second_noun, animals, food, second_verb,
               third_noun, fruit, third_adjective, name, third_verb, number, name, superhero, superhero, name, country,
               name, desert, name, year, fourth_noun))
