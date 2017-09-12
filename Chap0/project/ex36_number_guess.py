#ex 36
# The task of this exercise is to design a number guessing game.
import random

goal = random.randint(1, 20)
n = 10

print ("Please enter an integer from 0 to 20." )
print ("And you have 10 chances to guess the correct number.")
guess = int(input ('> '))


while n != 0:
    if guess == goal:
        print ("Yes, you win!")
        exit(0)

    elif guess < goal:
        n = n - 1
        print ("Your guess is smaller than the correct number.")
        print (f"You can still try {n} times.")
        guess = int(input ('> '))
    else:
        n = n - 1
        print ("Your guess is larger than the correct number.")
        print (f"You can still try {n} times.")
        guess = int(input ('> '))


#Notes on if-statements & loops:
# Rules for if-statements:
# 1) every if-statement must have an else
# 2) if this else should never run because it doesn't make sense,
#    then you must use a die function in the else that prints out
#    an error message and dies
# 3) never nest if-statements more than two deep
# 4) treat if-statements like paragraphs, where if-elif-else grouping
#    is like a set of sentences. Put blank lines before and after
# 5) Your boolean tests should be SIMPLE!
#    If they are complex, move their calculations to variables earlier in
#    your function and use a good name for the variable.

# Rules for Loops:
# 1) use a while loop ONLY to loop forever, and that means probably never...
#    this only applies to python, other languages might be different
# 2) use for-loop for all other kinds of looping, esp. if there is a
#    fixed or limited number of things to loop over

# Tips for debugging:
# 1) The best way to debug is to use print to print out the values of
#    variables at points in the program to see where they go wrong
# 2) Do NOT write massive files of code before you try to run them,
#    code a little, run a little, fix a little.
