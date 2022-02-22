"""
18/02/2022 3 2nd function: combine these into one function that includes only one loop
"""

import random


def list_sum_reverse(list):
    sum = 0
    newlist = []
    newlist2 = reversed(range(len(list)))
    for i in newlist2:
        sum = sum + list[i]
        newlist.append(list[i])
    print(f"Sum of this list is: {sum}")
    print(f"List reversed was: {newlist}")
    return sum, newlist


# get random list as argument
randomlist = []
for i in range(0, 25):
    n = random.randint(1, 300)
    randomlist.append(n)
print(f"List generated is: {randomlist}")

newlist2 = list_sum_reverse(randomlist)
