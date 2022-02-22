"""
SKIPPED: Write a program that uses while loops to finish the tasks below: Searching for a specific number
(e.g. 5) in an integer list of unknown length Multiplying all
elements of an integer list of unknown length Printing out the contents
of a string list of unknown length elementwise """

# This does not work. everyone had a long day

"""
COMPLETED: Exercise 25 – Loop through a matrix
Write a Program that uses nested loops to tackel the tasks below: Search for the
coordinates of maximal value of the matrix Sum up all entries of the matrix
Describe the multiplication of the components of two matrices in a third
resulting matrix
"""

import random

#
# randomlist = []
# for i in range(0, 25):
#     n = random.randint(1, 300)
#     randomlist.append(n)
# print(randomlist)

# generates a matrix of random integers between 10 and 500
testmatrix = [
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
]

print(testmatrix)

# Credit to @neugchr for explaining this to me at the end of 17.02.2022
# My script is different because I got it to describe the list parsing in order
# to teach me what was happening.

# search for its maximal value

# You have broken this and you have no backup of it
def find_max(matrix):
    top = 0
    xy = (0, 0)
    newmatrix = range(len(matrix))
    for point in newmatrix:
        # displays when the nested list is changed, or "none"
        print(f"point = {point +1}")
        # print the max at every time it changes
        print(f"Max value = {top}")
        newmatrix2 = range(len(matrix[point]))
        #
        for pointWithin in newmatrix2:
            print(f"point within = {pointWithin +1}")
            if matrix[point][pointWithin] > top:
                top = matrix[point][pointWithin]
                print(f"Max value: {top}")
                xy = (point + 1, pointWithin + 1)
                print(f"Point where new top found (x, y): {xy}")
    return top


# See comment above other function
def matrix_summer(matrix):
    sum = 0  # See 17022022-1.py in this repository for how the for loop can sum entries up
    newmatrix2 = range(len(matrix))
    for point in newmatrix2:
        for pointWithin in range(len(matrix[point])):
            sum = sum + matrix[point][pointWithin]
    print(f"Sum of this matrix is: {sum}")
    return sum


top = find_max(testmatrix)
print(f"Maximum value in matrix: {top}")
sum = matrix_summer(testmatrix)
print(f"Sum of data points in matrix: {sum}")

# Multiplication component of Python exercise 25
# Generate another matrix
testmatrix2 = [
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
]
print(testmatrix)
print(testmatrix2)
# Testing multiplying them together
# You must generate a matrix of random numbers which is then modified by the
# following for loop. commenting out the block where the matrix is filled, this
# will make this return empty list

testmatrix3 = [
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
]

print(testmatrix3)


def find_product(matrix, matrix2):
    resultmatrix = []
    for i in range(len(matrix)):
        resultmatrix.append([])
        for j in range(len(matrix[i])):
            product = matrix[i][j] * matrix2[i][j]
            resultmatrix[i].append(product)
    print(f"Resulting Matrix when multiplied together:\n{resultmatrix}")
    return resultmatrix


find_product(testmatrix2, testmatrix3)
