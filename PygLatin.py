pyg = "ay"
original = input("Enter a word : ")


# An if condition to check that a word is typed and also checking the characters for all lower case test

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    # my_string[1:] # "ython"
    # my_string = "Python"
    new_word = original[1:] + first + pyg
    print(new_word)
    print(first)
    print(original)
else:
    print("empty")
