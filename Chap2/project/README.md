### Ch2 实时天气查询程序

#### 程序功能：
   * 输入城市名，返回该城市最近的天气数据；
   * 输入指令 （h 或 help），获取帮助信息；
   * 输入指令（history），获取历史查询信息；
   * 输入指令（quit），退出程序交互

#### 使用说明：
实时天气信息来源为[Openweathermap.org](http://openweathermap.org/current)，由于从网页端提取实时天气信息需要使用[Openweathermap.org](http://bulk.openweathermap.org/sample/)的城市ID作为唯一识别，因而程序使用可分为两个版本：
  * [版本一](https://github.com/xinweixu1/Py101-004/blob/master/Chap2/project/ch2_weather_inquiry_with_api_cleaned.py)需要从github 的 [resource](https://github.com/xinweixu1/Py101-004/tree/master/Chap2/resource)文件夹里下载city.list.json到本地路径，然后将程序中的文件路径修改 `path = '/Users/xinweixu/Documents/Comp_Prog/Python/Py101-004/Chap2/resource/city.list.json'`为你的本地存储路径；
  * [版本二](https://github.com/xinweixu1/Py101-004/blob/master/Chap2/project/ch2_weather_inquiry_fetch_cityid_from_web.py) 则直接从[Openweathermap.org](http://bulk.openweathermap.org/sample/) 下载并解压city.list.json.gz，然后提取城市ID信息


#### 分支程序工作流(user call == city name)：
user call(city name)
--> city dict (return city ID)
--> request from [Openweathermap.org](http://openweathermap.org/current) (return JSON)
--> decode JSON file (return a python data structure)
--> return to user in a readable format

#### 功能解构：
   * 城市名 －-> 城市ID   (`dictionary`)
   * 从 API 端提取城市天气信息 （`requests`）
   * 将 API 所返回的 JSON 数据中提取主要天气信息，并转化为 python 中的list数据结构 (`json.loads`)
