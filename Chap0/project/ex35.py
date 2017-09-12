#ex 35 Branches and functions
# - combining if-statements and functions

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice. You are not greedy and you win!")
        exit(0)

    else:
        dead("You greedy bastard!")  # note that dead is a function


def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False  # bear_moved is a logic variable

    while True:
          # when any of the following if-statements is False,
          # it will exit the while loop
        choice = input ("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
        # not bear_moved = True
        # when choice == "taunt bear" is True,
        # the whole "and" argument yields: True and True, which is True
            print ("The bear has moved from the door.")
            print ("You can go through the door now.")
            bear_moved = True
            #so from here it goes back to the start of the loop
            #the player will be prompted to enter another choice

        elif choice == "taunt bear" and bear_moved:
            # if the player chooses to taunt bear the 2nd time
            # the dead function will be executed
            dead ("The bear gets pissed off and chews your leg off.")

        elif choice == "open door" and bear_moved:
            # if the player chooses to open the door,
            # the gold_room function will be executed
            gold_room()

        else:
            print ("I got no idea what that means.")

def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("Do you flee for life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty...")
    else:
        cthulhu_room()

def dead(why):
    print (why, "Good job!")
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    if choice ==  "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()


#The order of the game:
#start function ---> choose between the bear room and the cthulhu room
# --> if bear room, decide how to move the bear -->


#What does exit(0) do?
#On many operating systems a program can abort with exit(0),
# and the number passed in will indicate an error or not.
# If you do exit(1) then it will be an error, but exit(0) will be a good exit.
# The reason it's backward from normal Boolean logic (with 0==False) is
#  that you can use different numbers to indicate different error results.
# You can do exit(100) for a different error result than exit(2) or exit(1).
