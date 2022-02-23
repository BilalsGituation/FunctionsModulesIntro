# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 10:01:48 2022

@author: user
"""


import argparse

#Create parser with mandatory argument of a string
parser = argparse.ArgumentParser(description='Process some strings.')
parser.add_argument('strings', metavar='Characters', type=str, nargs='+',
                    help='a string for the concatenator')
# Optional arguments allow concatenation of inputs,...
parser.add_argument('-C','--cat', dest='plonk_on', action='store_true',
                    help='add the second string to the first string')
# ... Reversal of inputs, ...
parser.add_argument('-r','--reverse', action='store_true',
                    help='reverse the string given into the shell with the script')
# ... Adding spaces between them (see help=), ...
parser.add_argument('--space', action='store_true',
                    help='add a space to the string under our focus\nwhen used alone with print, printout will be empty')
# ... and printout of outputs.
parser.add_argument('--print', action='store_true',
                    help='print the output of operation result')

# Reverses the string put in by the user
args = parser.parse_args()


# Prints the list of arguments given in the terminal
print(f'Arguments supplied: {args.strings}')

# If the user would like to concatenate multiple entries
# and/or put spaces between them, then this "if" tree will use "for" to
# iterate over each argument given, in order to perform either task.
Bigword = ""
if args.plonk_on and args.space:
    print('"--cat" AND "--space" called')
    for word in args.strings:
        Bigword += f'{word} '
elif args.space and not args.plonk_on:
    print('ONLY "--space" called')
    for word in args.strings:
        Bigword += " "
elif args.plonk_on and not args.space:
    print('ONLY "--cat" called')
    for word in args.strings:
        Bigword += f'{word}'
elif not args.plonk_on and not args.space:
    print('NEITHER "--cat" NOR "--space" called')
    for word in args.strings:
        Bigword = Bigword

print(f'Your output is: {Bigword}')

# Gives a verbose reversal of the "Bigword" variable
if args.reverse:
    print('"--reverse" called')
    if Bigword:
        print(f'List (just reversed): {str(list(reversed(args.strings)))}')
        print(f'List (split and reversed): {list(reversed(Bigword))}')
        print(f'Concatenated entries reversed: {"".join(list(reversed(args.strings)))}')
        print(f'Entries split, reversed, then concatenated\n(unless "--space" given): {"".join(list(reversed(Bigword)))}')
    else:
        pass
