# Ex38 - Doing Things to Lists
# Recall that in EX 33 we used a while loop to append numbers to a list
# When we write mystuff.append('hello'), we are actually setting off a chain of
#  events in python to cause something to happen to the list of "mystuff";
# And here's what happens:
#  1) Python looks up the variable you mentioned - "mystuff" and checks if
#     it's a function argument or a global variable.
#  2) Once it finds mystuff, it reads the . operator and starts to look at
#     variables that are a part of mystuff. Since mystuff is a list, it knows that
#     mystuff has a bunch of functions.
#  3) Then python hits append and compares the name to all the names that mystuff
#     says it owns. If append is contained in mystuff, then Python grabs that to use.
#  4) Next Python sees the parenthesis and realizes, "oh, hey, this is a function!"
#     At this point it calls (runs/executes) the function just like normally,
#     but with an extra argument
#  5) The extra argument is mystuff. So it's basically a function call like:
#     append(mystuff, 'hello')

# What's a list?
# A list is a type of data structure in the form of an ordered list of things
# that you want to store and access randomly or linearly by an index.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')  # split "ten_things" by ' '(space),
                               # now stuff is a list containing 6 elements

more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # next_one is the last element in the more_stuff list
    print ("Adding: ", next_one)
    stuff.append(next_one) # append next_one to the list of stuff
    print (f"There are {len(stuff)} items now.") #{ } is the new style for format in python 3

# Notes on list.pop([i])
# it removes the element at the given position i in the list and return it;
# if no index is specified, the default is the last item in the list

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1])
print (stuff.pop()) # print the last element in the list of stuff
print (' '.join(stuff)) # joining the elements in the stuff with spaces
print ('#'.join(stuff[3:5])) # joining elements from position 3 to 5 with #
