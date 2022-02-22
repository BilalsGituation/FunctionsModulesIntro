"""
Exercise 29 – Functions with simple loops
Write a program that contains two different functions. The first function should take a list as argument and return the sum of all elements in the list, calculated by a loop. The second function should also take a list and return a list in which the contents of the handed over list are reversed
"""


import random

# get random list as argument
randomlist = []
for i in range(0, 25):
    n = random.randint(1, 300)
    randomlist.append(n)
print(f"List generated is: {randomlist}")


def list_summer(list):
    # Get sum of list
    sum = 0
    for i2 in randomlist:
        sum = sum + i2
    print(f"Sum of this list is: {sum}")
    return sum


def list_reverser(list):
    #    list.reverse() # This does it very simply
    newlist = []
    i3 = reversed(range(len(list)))
    for i in i3:
        newlist.append(list[i])
    return newlist


sum = list_summer(randomlist)
print(f"Sum of the list generated above is: {sum}")
newlist = list_reverser(randomlist)
print(f"List reversed is {newlist}")
