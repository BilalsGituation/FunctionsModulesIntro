'''
Write a program that runs a simple division. Generate a random integer and divide it
through an integer inputted by the user. Create an exception for wrong inputs (a string for
example). Create a second exception to handle division by zero. Both exceptions should
belong to the same try. Print out the result of the division at the end and try several different
inputs.
'''
import random

def reject_invalid_inputs_then_div(userchoice, number):
    while True:
        try:
            # An integer should divide into the random integer generated
            Inp = int(input(userchoice))
            # Do division operation
            DivRando = number / Inp
            print(f'{number} divided by {Inp} equals {DivRando}')
            break
            # Reject strings etc.
        except ValueError:
            print("Please input a number:\n") # Or whatever a valid entry would be
            continue
            # Reject zero
        except ZeroDivisionError:
            print("Don't say zero, that's super uncooperative!\n")
            # This is just to be safe
        except:
            pass

# Generate random number
rando = random.randint(-5000000000000,9999999999999)
print(f"Let me think of a number....")
print("\n\n\n\n...")
print(f"{rando}")
print(f"Now you're going to supply a whole number to divide {rando} by:\n")
# Call reject_invalid_inputs_then_div(args)
reject_invalid_inputs_then_div(f"Go ahead. Which number shall we divide {rando} by?\n", rando)
