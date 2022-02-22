# This is an extremely basic calculator which does + - * and /

def adding(prompt1, prompt2):
    while True:
        try:
            arg1 = int(input(prompt1))
        except ValueError:
            print("Please enter a whole number. I've already asked you once.\n")
            continue
        else:
            break
    while True:
        try:
            arg2 = int(input(prompt2))
        except ValueError:
            print("Please enter a whole number. I've already told you once.\n")
            continue
        else:
            break
    sumofinputs = arg1 + arg2

    print(f"Sum result was:\n{sumofinputs}")


adding(
    "Please enter the first whole number to add:\n",
    "Please enter a whole number to add to it:\n",
)


def subtracting(prompt3, prompt4):
    while True:
        try:
            arg1 = int(input(prompt3))
        except ValueError:
            print("Please enter a whole number. I've already asked you once.\n")
            continue
        else:
            break
    while True:
        try:
            arg2 = int(input(prompt4))
        except ValueError:
            print("Please enter a whole number. I've already told you once.\n")
            continue
        else:
            break
    sumofinputs = arg1 - arg2

    print(f"Subtraction result was:\n{sumofinputs}")


subtracting(
    "Please enter the first whole number to subtract from:\n",
    "Please enter a whole number to subtract from it:\n",
)


def multiplying(prompt5, prompt6):
    while True:
        try:
            arg1 = int(input(prompt5))
        except ValueError:
            print("Please enter a whole number. I've already asked you once.\n")
            continue
        else:
            break
    while True:
        try:
            arg2 = int(input(prompt6))
        except ValueError:
            print("Please enter a whole number. I've already told you once.\n")
            continue
        else:
            break
    sumofinputs = arg1 * arg2

    print(f"Multiplication result was:\n{sumofinputs}")


multiplying(
    "Please enter the first whole number to multiply with:\n",
    "Please enter a whole number to multiply it by:\n",
)


def dividing(prompt7, prompt8):
    while True:
        try:
            arg1 = int(input(prompt7))
        except ValueError:
            print("Please enter a whole number. I've already asked you once.\n")
            continue
        else:
            break
    while True:
        try:
            arg2 = int(input(prompt8))
        except ValueError:
            print("Please enter a whole number. I've already told you once.\n")
            continue
        else:
            break
    sumofinputs = arg1 / arg2

    print(f"Division result was:\n{sumofinputs}")


dividing(
    "Please enter the first whole number to divide:\n",
    "Please enter a whole number to divide it by:\n",
)
