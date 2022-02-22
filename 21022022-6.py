'''
Exercise 35:
Using the "math" module to do maths:
Write a program that takes two numbers (x and y) from the user and calculates new values
with the help of the math functions on the previous slides. Print out the results.
'''

# Get the module
import math

# "Program" asked for by exercise contained within this functions
# Your two inputs serve as the arguments
def maths(prompt1, prompt2):
    while True:
        try:
            # First number has to be a float
            Inp1 = float(input(prompt1))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as a float...
        except ValueError:
            # or not...
            print("Please input the first number.\n")
            continue
            # Check validity of user input, as immediately above
    while True:
        try:
            Inp2 = float(input(prompt2))
            break
        except ValueError:
            print("Please input the second number.\n")
            continue
        # do the mathematical operation
        # (if you were continuing, you could set more variables using the same
        # inputs, then do calculations with them.)
    Ans = math.pow(Inp1, Inp2)
    # Print the result(s) of the mathematical operation(s)
    print(Ans)
    print(f'Square root of the resulting number:\n{math.sqrt(Ans)}')

# Call the function, user input prompts shown in terminal
maths("Please type in a number.\n", "Please type in another, this will act as a power of the first.\nWe will then see what the square root of that number is.\n")
