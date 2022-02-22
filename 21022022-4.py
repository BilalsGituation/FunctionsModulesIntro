'''
Exercise 33 – New modules
Write a program that asks the user to guess a specific number.
-Generate a random number between 0 and 99,
search the library to find a module and a function for this task.
-Generate a while loop that asks for a guess as long as the user didn’t guess
right.
-Print out hints if the user is lower or higher than the random number.
-Count the number of guesses the user needed and print them out after 
the user guessed correctly.
'''
import random # Allows random integer generation

# Defines function that carries out the number-guessing game asked by the exercise
def RndNumGame(prompt):
    # Generate the number for the user to guess
    RndNmr = random.randint(0,99)
    Count = 0 # Attempt no. count starts at 0
    # Set up while loop:
    while True:
        # Counts the number of attempts, adds one for each iteration at start
        Count += 1
        # Make sure that the user input is indeed an integer
        try:
            Ans = int(input(prompt))
        except ValueError:
            print("\nPlease enter a whole number. I have already asked you once.\n")
            continue
        # Make sure number is in valid range (Lower Bound)
        if Ans < 0:
            print(f"\nYour chosen number is too low.")
            print(f'Current number of attempts is: {Count}.\n')
            pass
        # Make sure number is valid range (Upper Bound)
        elif Ans > 99:
            print(f"\nYour chosen number is too high.")
            print(f'Current number of attempts is: {Count}.\n')
            pass
        # If answer is higher than the secret number
        elif Ans > RndNmr:
            print(f"\nThe number I am thinking of is lower than {Ans}.")
            print(f'Current number of attempts is: {Count}.\n')
            pass
        # If answer is lower than the secret number
        elif Ans < RndNmr:
            print(f"\nThe number I am thinking of is higher than {Ans}.")
            print(f'Current number of attempts is: {Count}.\n')
            pass
        # If the user guessed the secret number correctly
        elif Ans == RndNmr:
            print(f'\n{Ans} was correct! You got it in {Count} attempts!')
            break
        else:
            print("I don't know how you got this message. Well done!")

# Call function that starts the "game"
RndNumGame("I am thinking of a whole number between 0 and 99.\nTry to guess it or perform a KeyboardInterrupt to quit.\n\n")
