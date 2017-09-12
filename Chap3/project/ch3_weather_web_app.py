"""
Program: Weather Inquiry Web APP
Author: xinwei
Github: https://github.com/xinweixu1
Last updated: Sep 4, 2017

"""
from flask import Flask, request, render_template
import requests
import urllib.request
import gzip
import json

# Request weather information from Openweathermap.org
# 1) set up a dictionary of city names(keys) and city IDs(values)
api_keys = {}
api_keys['default'] = '858c8e12893a06793aed1c1c6fa2fd34'

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

# 2) define a function returning weather info from Openweathermap.org
def retrieve_weather_info (city_name):
    city_id = city_dict[city_name]
    APPID = api_keys['default']
    request_url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={APPID}'
    raw_info = requests.get(request_url, auth=('default', api_keys['default']))
    decode_info = json.loads(raw_info.text)
    weather_info = decode_info['weather'][0]
    return weather_info['description']


# Use Flask to build up the html webpages
app = Flask(__name__)

hist = []

@app.route('/',  methods=['GET','POST'])
def home_page():
    return render_template('home_page.html')

@app.route('/weather/<cityname>',  methods=['GET','POST'])
def weather_search(cityname):
    cityname = request.form['cityname']
    if cityname in city_dict.keys():
        weather = retrieve_weather_info(cityname)
        hist.append(cityname + ': ' +weather)
        return render_template('city_weather.html', cityname=cityname, weather=weather)

    else:
        return render_template('home_page.html',
                           message="""
                           Sorry, we couldn't find the city you enterd.
                           Please try again!
                           """)


@app.route('/help')
def help_info():
    return render_template('help_info.html')

@app.route('/history')
def history():
    return render_template('history.html', hist_list=map(str.rstrip, hist))

if __name__ == '__main__':
    app.run()
