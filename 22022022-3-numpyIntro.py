'''
Intro to numpy and arrays:

np.attribute calls numpy functions

np.array turns your list into an array
np.zeros(x, y, z...) produces an array full of zeros, Dimensions x*y*z*...
np.zeros(x, y, z...) produces an array full of zeros, Dimensions x*y*z*...

Write a simple python program that generates the following arrays:
An array consisting of 25 zeros
An array consisting of 8 ones
An array consisting of numbers from 0 to 24 in order
An array consisting of 9 entries of your choice
An two-dimensional array TD consisting of 6 rows of arrays with 5 entries
A transposed version of the two-dimensional array TD
Write furthermore an algorithm to print out the sum, maximum value, minimum value and
shape of all created arrays.
'''

import numpy as np
import random

# For loop to get sum and maximum value of each array generated
def search_array_return_sum_max(array):
    sum = 0
    max = 0
    for i in array:
        sum += i
        if max < i:
            max = i
    print(f'Array produced:\n{array}')
    print(f'Its maximum value is {max}')
    print(f"Sum of array produced is: {sum}")

# loops (for) over a matrix to give sum of entries and max value
def search_2d_array_return_sum_max(array):
    sum = 0
    max = 0
    for i in array:
        for j in i:
            sum += j
            if max < j:
                max = j
    print(f'Array produced:\n{array}')
    print(f'Its maximum value is {max}')
    print(f"Sum of array produced is: {sum}")

# Inputs numbers to the empty User-generated array defined later in array_choice(arguments),
# rejects if invalid and appends to the User-generated array in valid
def reject_invalid_inputs_floats(userchoice, array):
    while True:
        try:
            # Change to int or string or whatever as needed
            Inp = float(input(userchoice))
            # Here is space for you to execute once you have a valid input
            array.append(Inp)
            break
        except ValueError:
            print("Please input a number:\n") # Or whatever a valid entry would be
            continue

# Lets user input entries into their array
def array_choice(prompt1, prompt2, prompt3, prompt4,prompt5,prompt6,prompt7,prompt8,prompt9):
    UserArray = []
    reject_invalid_inputs_floats(prompt1, UserArray)
    reject_invalid_inputs_floats(prompt2, UserArray)
    reject_invalid_inputs_floats(prompt3, UserArray)
    reject_invalid_inputs_floats(prompt4, UserArray)
    reject_invalid_inputs_floats(prompt5, UserArray)
    reject_invalid_inputs_floats(prompt6, UserArray)
    reject_invalid_inputs_floats(prompt7, UserArray)
    reject_invalid_inputs_floats(prompt8, UserArray)
    reject_invalid_inputs_floats(prompt9, UserArray)

    print(f"User-defined Array:")
    search_array_return_sum_max(UserArray)
    print(f'Its minimum value is {np.array(UserArray).min()}')
    return
# Generate and print an array of 25 zeros
array1 = np.zeros(25)
print(f'\nFirst Array:')
search_array_return_sum_max(array1)
print(f'Its minimum value is {array1.min()}\n')

# Generate and print an array of 8 ones
array2= np.ones(8)
print(f'Second array:')
search_array_return_sum_max(array2)
print(f'Its minimum value is {array2.min()}\n')

# Generate and print an array of numbers 0-24
array3=np.array(range(0,25))
print(f"Third Array:")
search_array_return_sum_max(array3)
print(f'Its minimum value is {array3.min()}\n')

# Generate an array using 9 user choices
array_choice("Please enter the 1st number of your array:\n", "Please enter the 2nd number of your array:\n", "Please enter the 3rd number of your array:\n", "Please enter the 4th number of your array:\n", "Please enter the 5th number of your array:\n", "Please enter the 6th number of your array:\n", "Please enter the 7th number of your array:\n", "Please enter the 8th number of your array:\n", "Please enter the 9th and final number of your array:\n")

# Generate the 2d array 5x6
array4 = np.random.randint(1,100,(6,5))
print(f'Fourth array:')
search_2d_array_return_sum_max(array4)
print(f'Its minimum value is {array4.min()}')

# Transpose and print it
array5 = np.transpose(array4)
print(f"\nFifth array is a transposition (matrix) of the fourth array:")
print(f'Fifth array produced:\n{array5}')
