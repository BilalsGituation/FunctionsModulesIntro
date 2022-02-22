"""take the exercise from 17/02 (updated matrix exercise with functions)
and convert all of your functions to one function"""

import random

#
# randomlist = []
# for i in range(0, 25):
#     n = random.randint(1, 300)
#     randomlist.append(n)
# print(randomlist)

# generates a matrix of random integers between 10 and 500
# testmatrix = [
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
# ]
#
# print(testmatrix)

# [Carried over from 17/02 script]
# Credit to @neugchr for explaining this to me at the end of 17.02.2022
# My script is different because I got it to describe the list parsing in order
# to teach me what was happening.

# search for its maximal value
def random_max_sum_product():
    # generates a random matrix when called
    testmatrix = [
        list(random.sample(range(10, 500), 5)),
        list(random.sample(range(10, 500), 5)),
        list(random.sample(range(10, 500), 5)),
    ]
    print(f"First random 5x3 matrix generated:\n{testmatrix}")
    top = 0
    xy = (0, 0)
    sum = 0
    newmatrix = range(len(testmatrix))
    for point in newmatrix:
        # displays when the nested list is changed, or "none"
        print(f"point = {point +1}")
        # print the max at every time it changes
        print(f"Max value = {top}")
        newmatrix2 = range(len(testmatrix[point]))
        #
        for pointWithin in newmatrix2:
            sum = sum + testmatrix[point][pointWithin]
            print(f"point within = {pointWithin +1}")
            if testmatrix[point][pointWithin] > top:
                top = testmatrix[point][pointWithin]
                print(f"Max value: {top}")
                xy = (point + 1, pointWithin + 1)
    # return top
    print(f"Max value at End was: {top}")
    print(f"Point where final maximum found (x, y): {xy}")
    print(f"Now let's get the sum of all the points:\n {sum}")
    # See 17022022-1.py in this repository for how the for loop can sum entries up

    # return sum
    # Printing 2 more random matrices:
    testmatrix2 = [
        list(random.sample(range(10, 500), 5)),
        list(random.sample(range(10, 500), 5)),
        list(random.sample(range(10, 500), 5)),
    ]
    testmatrix3 = [
        list(random.sample(range(10, 500), 5)),
        list(random.sample(range(10, 500), 5)),
        list(random.sample(range(10, 500), 5)),
    ]
    print(f"2nd randomly-generated matrix is:\n{testmatrix2}")
    print(f"3rd randomly-generated matrix is:\n{testmatrix3}")
    resultmatrix = []
    for i in range(len(testmatrix2)):
        resultmatrix.append([])
        for j in range(len(testmatrix2[i])):
            product = testmatrix2[i][j] * testmatrix3[i][j]
            resultmatrix[i].append(product)
    print(f"Resulting Matrix when 2 and 3 are multiplied together:\n{resultmatrix}")


random_max_sum_product()

# # See comment above other function
# def matrix_summer(matrix):
#     sum = 0  # See 17022022-1.py in this repository for how the for loop can sum entries up
#     newmatrix2 = range(len(matrix))
#     for point in newmatrix2:
#         for pointWithin in range(len(matrix[point])):
#             sum = sum + matrix[point][pointWithin]
#     print(f"Sum of this matrix is: {sum}")
#     return sum
#
#
# top = find_max(testmatrix)
# print(f"Maximum value in matrix: {top}")
# sum = matrix_summer(testmatrix)
# print(f"Sum of data points in matrix: {sum}")
#
# # Multiplication component of Python exercise 25
# # Generate another matrix
# testmatrix2 = [
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
# ]
# print(testmatrix)
# print(testmatrix2)
# # Testing multiplying them together
# # You must generate a matrix of random numbers which is then modified by the
# # following for loop. commenting out the block where the matrix is filled, this
# # will make this return empty list
#
# testmatrix3 = [
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
# ]
#
# print(testmatrix3)
#
#
# def find_product(matrix, matrix2):
#     resultmatrix = []
#     for i in range(len(matrix)):
#         resultmatrix.append([])
#         for j in range(len(matrix[i])):
#             product = matrix[i][j] * matrix2[i][j]
#             resultmatrix[i].append(product)
#     print(f"Resulting Matrix when multiplied together:\n{resultmatrix}")
#     return resultmatrix
#
#
# find_product(testmatrix2, testmatrix3)
