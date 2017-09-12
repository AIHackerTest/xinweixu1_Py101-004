#ex 34 - Accessing Elements of Lists
#Version: python 3.6.1

animals = ['bear', 'tiger', 'penguin', 'zebra']
print (animals[0])

animals2 = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

animal_at_1 = animals2[1] #python3.6 is in position 1
print ("The animal at 1 is: ", animal_at_1)

the_first_animal = animals2[0] #bear is the first animal in the list
print ("The 1st animal is: ", the_first_animal)

the_third_animal = animals2[3] #kangaroo, in position 3
print ("The 3rd animal is: ", the_third_animal)

the_animal_at_3 = animals2[3]
#kangaroo is the 4th element in the list but it's in position 3
print ("The animal at 3 is: ", the_animal_at_3)

the_fifth_animal = animals2[5]
#playpus is the 5th animal and is in position 5
print ("The 5th animal is: ", the_fifth_animal)

the_animal_at_2 = animals2[2]
#the animal at position 2 is peacock
print ("The animal at 2 is: ", the_animal_at_2)

print("There is no sixth animal...because there were only 5 animals in the list of 6 elements.")

the_animal_at_4 = animals2[4]
#the animal at position 4 is whale
print("The animal at 4 is: ", the_animal_at_4)
