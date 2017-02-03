"""for item in list:
    print item

for i in range(len(list)):
    print list[i]
    """

    n = ["Michael", "Lieberman"]


    def join_strings(words):
        result = ""
        for word in words:
            result = result + word
        return result


    # Add your function here

    print(join_strings(n))
""" Using multiple lists in a function is no different from just using multiple arguments in a function!

a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# prints [1, 2, 3, 4, 5, 6]
The example above is just a reminder of how to concatenate two lists."""

m = [1, 2, 3]
n = [4, 5, 6]


# Add your code here!
def join_lists(x, y):
    return x + y


print
join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

""" Using a list of lists in a function
Finally, this exercise shows how to make use of a single list that contains multiple lists and how to use them in a function.

list_of_lists = [[1,2,3], [4,5,6]]

for lst in list_of_lists:
    for item in lst:
        print item
In the example above, we first create a list containing two items, each of which is a list of numbers.
Then, we iterate through our outer list.
For each of the two inner lists (as lst), we iterate through the numbers (as item) and print them out.
We end up printing out:

1
2
3
4
5
6"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    result = []
    for numbers in lists:
        for i in range(len(numbers)):
            result.append(numbers[i])
    return result
print flatten(n)

