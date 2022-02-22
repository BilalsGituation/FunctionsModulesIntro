"""

Pseudocode: exercises 23, 24, 25

Post-solution REVIEW: Too much detail, to be honest
                      especially for someone who understands the fundamentals

Ex 23: Exercise 23 – Your first loops
Generate a list that contains at least 20 random integers. Write one loop that sums up all entries of the list. Write another loop that sums up only the entries of the list with even indices. Write a third loop that generates a new list that contains the values of the list in reverse order. Print out all three results

# Generate number list
import the random package

randomlist = empty list

for index in range of 0-25
    number1, between 0 and 300, is generated
    number1 is appended to randomlist
Loop is exited once whole list is read

# Add numbers in list to sum, by changing its value on iterations
set sum = 0
for index in randomlist
    sum += index
print(sum)

Take user input (integer)
if input in list, just inform user of that
for each element:
    If input bigger than list element, inform them of that then parse next element
    else if input smaller than list element, inform them of that then parse next element


Exercise 24 – 3 while loops
Write a program that uses while loops to finish the tasks below:
    - Searching for a specific number (e.g. 5) in an integer list of unknown length
    - Multiplying all elements of an integer list of unknown length
    - Printing out the contents of a string list of unknown length elementwise

# Generate list of unknown length with random elements
define empty list p
for index in range between 1 and random integer between min1 and max1
    append random number between min2 and max2 to p
print p

# 1st part - search for number
get user input (number to scan for)
start at 0th position
set NumFound to False
while reading position is lower than length of list:
    if reading position = user input
        print confirmation for user
        NumFound becomes True
    reading position += 1
if NumFound remains False, inform user

# 2nd part - multiply list entries together
call list using code from earlier (recommended not to have more than 7 elements and random numbers only between 1-10)
set first parsing index (FPI) to 0
while FPI is less than list length:
    set second parsing index (SPI) to 0
        while SPI is less than list length
            print(f'current entry {SPI} times last entry {FPI} = {SPI*FPI}')
            SPI +=1 # move reading frame for reading position
        FPI +=1 # move reading frame for reading position -1

# 3rd part - print contents of unknown list by element

call list using code from earlier
(STOPPED TO FOLLOW CHRISTOPH'S SOLUTION IN LESSON. It's much nicer to read,
of course, so you can take this as an example of too much detail)
"""


# after that, moved onto definition of function (see pdf)
"""Create a program that defines functions for the four mathematical basic
operations (+, -, * and /). Call the functions at least three times
with different parameters."""
