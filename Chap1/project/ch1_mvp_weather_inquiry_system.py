"""
This is a weather inqury system with the following functions:
1) enter a city name to retrieve weather information
2) enter "help" to get help information
3) enter "history" to look at search history
4) enter "quit" to quit the program

"""

#Prepare the dictionary containing all the weather information to be used:
path = '/Users/xinweixu/Documents/Comp_Prog/Python/Py101-004/Chap1/resource/weather_info.txt'

weather_dict = {}

with open(path) as f:
    weather_data = f.readlines()

for line in weather_data:     #loop over each line to extract cities and weathers
    city = line.split(',')[0]
    weather = line.split(',')[1]
    weather_dict[city] =  weather

#The user-interfaced program starts from here
print("#"*10)
print("Welcome to the weather inqury wizard!")
print("""
     You can enter one of the comands:\n
     please enter "help" for help information\n
     please enter "history" for your search history\n
     please enter "quit" to exit
      """)
hist = []

while True:
    user_call = input("Please enter a command or a city name: ")

    if user_call in weather_dict.keys():
        print(user_call, weather_dict[user_call])
        hist.append(user_call + '  ' +weather_dict[user_call])
        #add double-space between the city name and weather info for easier views

    elif user_call == "quit":
        print("Thank you! Bye!")
        exit(0)

    elif user_call == "help":
        print("""
        Please enter a city name to get its weather information. Or,
        enter "history" for your search history,
        enter "quit" to exit,
        enter "help" to see the help file again.
        """)

    elif user_call == "history":
        print ("Here is your search history: ")
        # 1) a simple version, just print out the hist list:
        #print (hist)
        # 2) an improved version stripping the '\n' when printing:
        #print (list(map(str.rstrip, hist)))
        # right-stripping each element in the hist list
        # 3) a further improved version printing each element separately:
        for ch in map(str.rstrip, hist):
            print (ch)

    else:
        print("It's not a valid input. Please try again.")

# Notes on the map() function:
# map(function, iterable, ...)
# return an iterator that applies function to every item of iterable,
# yielding the results;
# Note that in python 3, you need to turn the object returned from the
# map function into a list in order to print all the elements
