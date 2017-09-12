#Ex39 - Dictionaries continued

#create a mapping of states to their abbrevation
states = {
      'Oregon': 'OR',
      'Florida': 'FL',
      'California': 'CA',
      'New York': 'NY',
      'Michigan': 'MI'
}

#create a basic set of states with some cities in them
cities = {
      'CA': 'San Francisco',
      'MI': 'Ann Arbor',
      'FL': 'Miami'

}

#add more cities:
cities['NY'] = 'Ithaca!'
cities['OR'] = 'Portland'

#print out some cities:
print ('-' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

#and some states:
print ('-' * 10)
print ("Michigan's abbrevation is: ", states['Michigan'])
print ("Florida's abbrevation is: ", states['Florida'])

#now use the states abbrevation dic to access the cities dict:
print ('-' * 10)
print ("California State has: ", cities[states['California']]) # fancy!
print ("Oregon State has: ", cities[states['Oregon']])

#print every state abbrevation using a for-loop:
for state, abbrev in list(states.items()):
    print (f"{state} is abbrevated {abbrev}")

#print every city in state:
print ('-' * 10)
for stabbrev, city in list(cities.items()):
    print (f"{stabbrev} has the city {city}")

#now do both at the same time:
print ('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# to safely get a abbreviation by state that might not be there
# for example, Texas is not in the dictionary
state = states.get('Texas')
print (state)  # now the variable state takes a value of "None"

if not state:  # the condition - not None, would return True
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")


## Note that in the context of True value testing,
## the following values are considered false:
## 1) None, false
## 2) zero of any numeric type
## 3) any empty sequence, '', (), []
## 4) any empty mapping {}

## see documentation : https://docs.python.org/2/library/stdtypes.html#truth-value-testing
