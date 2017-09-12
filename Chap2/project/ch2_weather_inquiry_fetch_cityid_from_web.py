"""
Program: Weather Inquiry in Real Time using Web API
Author: xinwei
Github: https://github.com/xinweixu1
Last updated: Aug 22, 2017

"""
import sys
import requests
import urllib.request
import gzip
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
#download the city.list.json.gz from Openweathermap.org and unzip the file
city_list_url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
zipped_city_list = requests.get(city_list_url)
unzipped_city_list = gzip.decompress(zipped_city_list.content)
city_list = json.loads(unzipped_city_list)
#set up the dictionary with city names and city IDs extracted from the city_list
for city in city_list:
    name = city['name']
    city_dict[name] = city['id']

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

hist = []

while True:
    user_call = input("Please enter a command or a city name: ")

    if user_call in city_dict.keys():
        weather_url = request_url(user_call, 'default') # use the default API key
        weather = retrieve_weather_info(weather_url, 'default')
        print(f"Now the weather in {user_call} is {weather}.")
        hist.append(user_call + ': ' +weather)

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
