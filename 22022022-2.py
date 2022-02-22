'''
Exercise 37 – Random generator
Write a program that generates several random numbers.

Let the user input the ranges for three random integers.

Let the user choose how many random floats between 0 and 1 should be created.
Let the user put in at least two mu and two sigma to create normaldistribution values.

What happens if you switch these two values?

Last but not least put all
generated values in a list, print the list, shuffle the list and print it again
'''
import random

def RndInt(r1int1, r1int2, r2int1, r2int2, r3int1, r3int2):
    print("Let's get some prompts and then I'll generate a random number!")
    print("We'll set 3 ranges with the prompts!")
    while True:
        try:
            # First number has to be a float
            Inp1 = int(input(r1int1))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as a float...
        except ValueError:
            # or not...
            print("Please input the first number.\n")
            continue
    while True:
        try:
            # First number has to be an integer
            Inp2 = int(input(r1int2))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as an integer...
        except ValueError:
            # or not...
            print("Please input the second number.\n")
            continue
    while True:
        try:
            # The number has to be "int"
            Inp3 = int(input(r2int1))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as a integer...
        except ValueError:
            # or not...
            print("Please input the third number.\n")
            continue
    while True:
        try:
            # Number has to be "int"
            Inp4 = int(input(r2int2))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as an integer...
        except ValueError:
            # or not...
            print("Please input the fourth number.\n")
            continue
    while True:
        try:
            # Must be "int"
            Inp5 = int(input(r3int1))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as an integer...
        except ValueError:
            # or not...
            print("Please input the fifth number.\n")
            continue
    while True:
        try:
            # Must be "int"
            Inp6 = int(input(r3int2))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as an integer...
        except ValueError:
            # or not...
            print("Please input the sixth number.\n")
            continue
    print(f'First random integer between a given range is: {random.randint(Inp1,Inp2)}')
    print(f'Second random integer between a given range is: {random.randint(Inp3,Inp4)}')
    print(f'Third random integer between a given range is: {random.randint(Inp5,Inp6)}')

def floats(fprompt):
    while True:
        try:
            # Must be "int"
            Inp7 = int(input(fprompt))
            break
            # User is allowed to advance (out of the loop) for providing
            # a value that can be read as an integer...
        except ValueError:
            # or not...
            print("Please input a whole number.\nI am not going to make you a fraction of a float value.\n")
            continue
    i = 0
    for i in range(Inp7):
        i+= 1
        OutFloat = random.random()
        print(str(OutFloat))
        if i > Inp7:
            break

floats("Please select how many random float values between 0 and 1 to create:\n")

RndInt("Please enter one boundary of the first range that an integer will randomly be selected from:\n", "Please enter the second boundary of the first range that an integer will randomly be selected from:\n", "Please enter one boundary of the second range that an integer will randomly be selected from:\n", "Please enter the second boundary of the second range that an integer will randomly be selected from:\n", "Please enter one boundary of the third range that an integer will randomly be selected from:\n", "Please enter the second boundary of the third range that an integer will randomly be selected from:\n")
