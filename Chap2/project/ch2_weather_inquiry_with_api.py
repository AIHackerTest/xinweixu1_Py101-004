"""
Program: Weather Inquiry in Real Time using Web API
Author: xinwei
Github: https://github.com/xinweixu1
Last updated: Aug 22, 2017

"""

import sys
import requests
import json

# To send requests to Openweathermap.org, we need the following two things:
# 1) an API key (APPID) generated from your personal account on the website;
# 2) a unique city ID indicating the info of which city to request;
# and a list of unique city IDs can be downloaded from the website (in JSON format)

# So the basic workflow would be:
# user call(city name)--> dict(return city ID) --> request from Openweathermap (return JSON)
# --> decode JSON file (return a python data structure) --> return to user

# 1) set up a dictionary to store API keys
api_keys = {}
api_keys['default'] = '858c8e12893a06793aed1c1c6fa2fd34'
api_keys['xinwei1'] = 'f444a776803c424d3fc01033ffcf2227'

# 2) set up a dictionary of city names(keys) and city IDs(values)
city_dict = {}
path = '/Users/xinweixu/Documents/Comp_Prog/Python/Py101-004/Chap2/resource/city.list.json'
with open(path) as json_city_list:
    city_list = json.load(json_city_list)
    # print(len(city_list)) # there were 209579 items (cities) in the list
    # print(city_list[0]) # each item contains a dictionary with 4 keys
                        # -- 'country', 'id', 'name', and 'coord'
for city in city_list:  # extract values of 'name' and 'id' from the city list
    name = city['name']
    city_dict[name] = city['id'] # values of 'name' as the new keys in city dict
                                 # values of 'id' as the new values in city dict
# let's try looking at an example of Moscow
#print(city_dict['Moscow'])

# 3) define a function returning the url for sending request messages to Openweathermap.org
def request_url (city_name, apikey_name):
    city_id = city_dict[city_name]
    APPID = api_keys[apikey_name]
    request_url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={APPID}'
    return request_url

# 4) define a function to request weather info from Openweathermap.org
def retrieve_weather_info (url, apikey_name):
    raw_info = requests.get(url, auth=(apikey_name, api_keys[apikey_name]))
    decode_info = json.loads(raw_info.text)
    weather_info = decode_info['weather'][0]
    return weather_info['description']

# let's try an example with the function:
#weather_url = request_url("Moscow", "default")
#print(weather_url)
#print(retrieve_weather_info(weather_url, "default"))

# The user-interfaced program starts from here:
print("#"*10)
print("Welcome to the weather inqury wizard!")
print("""
     You can enter one of the comands:\n
     please enter "help" for help information\n
     please enter "history" for your search history\n
     please enter "quit" to exit
      """)
print("#"*10)

hist = [] # set up an empty list for inquiry history

while True:
    user_call = input("Please enter a command or a city name: ")

    if user_call in city_dict.keys():
        weather_url = request_url(user_call, 'default') # use the default API key
        weather = retrieve_weather_info(weather_url, 'default')
        print(f"Now the weather in {user_call} is {weather}.")
        hist.append(user_call + ': ' +weather)
        #add ":" between the city name and weather info for easier views

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
        for ch in map(str.rstrip, hist):
            print (ch)

    else:
        print("It's not a valid input. Please try again.")
