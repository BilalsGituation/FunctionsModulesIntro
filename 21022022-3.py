"""
The class has been told about the following loop commands today:

Break: completely exits your loop at the point you set

Continue: goes back to the beginning of your loop at the point you set

Pass: Tells python that there is code rather than nothing

Exercise: Continue, Break, Pass commands:

    -Create a list with at least 15 random entries

    -Iterate over it with a for loop and add up the elements

    -Create one if statement in your loop that can’t be true and
    add a pass

    -Include a second if statement in your loop that breaks the
    loop if your sum gets bigger than a threshold ( you chose)

    -Include a third if statement in your loop that uses continue if
    the current entry of your list is in a specific range, eg. 50 to
    60, and prints out something in all other cases (use else)

    -Print out the sum and the number of

"""
# Allows our list of randomly-generated integers
import random

# Generate a list of random integers
randomlist = []
for i in range(0, 15):
    n = random.randint(1, 300)
    randomlist.append(n)
print(f"List generated is: {randomlist}")

# Define our function which performs a summation of the list entries
# and comments on the sixe of each integer
def list_break_pass_continue_demo(list):
    # Set summation variable to starting level 0
    sum = 0
    # Prevent IndexError by converting length of list to range
    newlist = range(len(list))
    # for-loop subjects each list entry to if-else tree
    for i in newlist:
        sum = sum + list[i]
        if list [i] < 0:
            print(f"You're not going to see this one.")
            pass
        elif sum > 2000:
            print(f"Sum exceeded 2000 at point {i + 1} ({list[i]}) so I stopped reading the list.")
            break
        elif 250 >= list[i] > 49:
            print(f"{list[i]} is between 50 and 250.\nSum right now is {sum}")
            continue
        else:
            print(f"{list[i]} is not between 50 and 250.\nSum right now is {sum}")
            pass
    # Informative message when loop is exited
    print(f"Sum of list until point {i + 1} of {len(list)} is: {sum}")

# Summation/Assessment function is called
list_break_pass_continue_demo(randomlist)
