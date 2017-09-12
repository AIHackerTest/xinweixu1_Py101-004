#Ex39 - Dictionaries

# What's a dictionary?
#A dictionary is a way to store data just like a list,
#but the main distinction is that -
#instead of using numbers as an index for a list,
#you can use almost anything as an index for a dictionary.

#Here's a list:
things = ['a', 'b', 'c', 'd']
print (things[1])

things[1] = 'z'
print (things[1])

#And here's a dictionary:
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print (stuff['name'])
print (stuff['age'])
print (stuff['height'])

stuff['city'] = 'SF'
print (stuff['city'])

# And we can also use numbers as the index for things in the dictionary:
stuff[1] = "Wow"
stuff[2] = "Neato"
print (stuff[1])
print (stuff[2])

print (stuff)

#You can delete things from the dictionary using del:
del stuff['city']
print (stuff)
del stuff[1]
print (stuff)
del stuff[2]
print (stuff)
