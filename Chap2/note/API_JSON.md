#### What's an API?
An API (application programming interface) is a set of subroutine definitions, protocols, and tools for building application software, or, a set of clearly defined methods of communication between various software components. A good API makes it easier to develop a computer program by providing all the building blocks.

#### What's a web-based API?
When used in the context of web development, an API is typically defined as a set of Hypertext Transfer Protocol (HTTP) **request** messages, along with a definition of the structure of **response** messages, usually in an Extensible Markup Language (XML) or JavaScript Object Notation (JSON) format.

#### What's JSON?
JavaScript Object Notation (JSON) is an open-standard file format that uses human-readable text to **transmit** data objects consisting of **attribute-value pairs** and **array** data types (or any **serializable** data types).
JSON's basic data types are:
 * Number
 * String
 * Boolean
 * Array (an ordered list of items of any type)
 * Object (an unordered collections of key/value pairs, where the keys are strings)
 * `null`

#### Examples of JSON and XML:
##### JSON example describing a person:
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021"
             },
  "phoneNumber": [
     {
      "type": "home",
      "number": "212 555-1234"
       },
      {
      "type": "fax",
      "number": "646 555-4567"
      }
   ],
  "gender": {
    "type": "male"
     }
}
```

##### XML example describing a person:
###### using tags:
```xml
<person>
   <firstName>John</firstName>
   <lastName>Smith</lastName>
   <age>25</age>
  <address>
    <streetAddress>21 2nd Street</streetAddress>
    <city>New York</city>
    <state>NY</state>
    <postalCode>10021</postalCode>
  </address>
  <phoneNumber>
    <type>home</type>
    <number>212 555-1234</number>
  </phoneNumber>
  <phoneNumber>
    <type>fax</type>
    <number>646 555-4567</number>
  </phoneNumber>
  <gender>
    <type>male</type>
  </gender>
</person>
```
###### using serialized attributes:
```xml
<person firstName="John" lastName="Smith" age="25">
  <address streetAddress="21 2nd Street" city="New York" state="NY" postalCode="10021" />
  <phoneNumber type="home" number="212 555-1234"/>
  <phoneNumber type="fax" number="646 555-4567"/>
  <gender type="male"/>
</person>
```
##### A JSON example of the API response from [Openweathermap.org](http://openweathermap.org/current):

```json
{"coord":
{"lon":145.77,"lat":-16.92},
"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
"base":"cmc stations",
"main":{"temp":293.25,"pressure":1019,"humidity":83,"temp_min":289.82,"temp_max":295.37},
"wind":{"speed":5.1,"deg":150},
"clouds":{"all":75},
"rain":{"3h":3},
"dt":1435658272,
"sys":{"type":1,"id":8166,"message":0.0166,"country":"AU","sunrise":1435610796,"sunset":1435650870},
"id":2172797,
"name":"Cairns",
"cod":200}
```

Parameters:
 - coord
    * coord.lon City geo location, longitude
    * coord.lat City geo location, latitude
 - weather (more info Weather condition codes)
    * weather.id Weather condition id
    * weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
    * weather.description Weather condition within the group
    * weather.icon Weather icon id
 - base Internal parameter
 - main
    * main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    * main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
    * main.humidity Humidity, %
    * main.temp_min Minimum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    * main.temp_max Maximum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    * main.sea_level Atmospheric pressure on the sea level, hPa
    * main.grnd_level Atmospheric pressure on the ground level, hPa
 - wind
    * wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
    * wind.deg Wind direction, degrees (meteorological)
 - clouds
    * clouds.all Cloudiness, %
 - rain
    * rain.3h Rain volume for the last 3 hours
 - snow
    * snow.3h Snow volume for the last 3 hours
 - dt Time of data calculation, unix, UTC
 - sys
    * sys.type Internal parameter
    * sys.id Internal parameter
    * sys.message Internal parameter
    * sys.country Country code (GB, JP etc.)
    * sys.sunrise Sunrise time, unix, UTC
    * sys.sunset Sunset time, unix, UTC
 - id City ID
 - name City name
 - cod Internal parameter



#### JSON Decoding and Encoding in Python 3
##### Basic Usage: `json.dumps` and `json.load`/`json.loads`
Encoding basic python object hierarchies:
`json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'`
Decoding:
`json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
['foo', {'bar': ['baz', None, 1.0, 2]}]`
Note that `json.load` takes a **file** object and `json.loads` takes strings.

##### Decoder and Encoder
`JSONDecoder` and `JSONEncoder` perform the following translation:

| JSON  | Python |
| ----- | ------ |
| object | dict  |
| array  | list  |
| string | str  |
| number(int)  | int  |
| number(real)  | float  |
| true  | True  |
| false | False  |
| null  | None  |

#### Reference:
- [Documentation](https://docs.python.org/3/library/json.html)
- [Wikipedia -  API](https://en.wikipedia.org/wiki/Application_programming_interface)
- [Wikipedia -  JSON](https://en.wikipedia.org/wiki/JSON)
