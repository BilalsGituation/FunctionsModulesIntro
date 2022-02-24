'''
Exercise 42 – Being an Esper
We want to write a more complex program in which the user guesses a number from 1, 2 or
3. The program should run 25 tries for the user and count how often he guessed right (while
loop). The program should raise an exception if the user put in a number outside the range
of 1 to 3 and another exception for inputs that weren‘t integer. Count how many tries the
user needed to finish the 25 iterations (in the finally command).
'''
# Random number needed by exercise
import random

# Defining function that responds to user inputs
def reject_count_invalid_inputs_123(userchoice):
    # Attempts at all
    tries = 0
    # Attempts correct
    corrects = 0
    # Start your while loop with an integer between 1 and 3
    RndInt1_3 = random.randint(1,3)
    # Responds to different types of input
    while True:
        print(f"\nAttempt: {tries + 1}")
        try:
            Inp = int(input(userchoice))
            if Inp == RndInt1_3:
                print("\nYou got that one CORRECT! Selecting number randomly out of [1], [2] and [3]..")
                corrects += 1 # Correct attempts goes up if user is correct
                print(f"You have guessed correctly {corrects} times!\n")
                RndInt1_3 = random.randint(1,3)
            # Builtin error message, for integers that aren't options
            if Inp not in [1, 2, 3]:
               raise RuntimeError("Please select one of the options:\n")
        # Core error message, for strings and other unwanted input
        except ValueError:
            print("Please input a whole number:\n")
        # Print different error for irrelevant integers
        except RuntimeError:
           print("That isn't one of the options.\n")
           continue
        # extra housekeeping
        except:
            pass
        # attempts counter goes up on every iteration
        finally:
            tries +=1
            if tries >= 25:
                break
    print(f"Final score: You guessed the correct number {corrects}/{tries} times")


reject_count_invalid_inputs_123("\nI am thinking of a number\nPlease select [1], [2] or [3] as a guess:\n")
