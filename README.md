Python API wrapper for OpenWeatherMap

#Overview

##How to install

```
git clone https://github.com/DoktorE/python-openweathermap
```
```python
python setup.py install
```

##How to use

```python
from openweathermap import Client
```
Make sure you have your API key
```python
client = Client('2de143494c0b295cca9337e1e96b00e0')

data = client.getWeatherZip(12702, 'us')
print(data)
# prints JSON response 
```

#API Method Guide

##Getting weather by city name
=======
```python
getWeatherCity('Dallas', 'us') # returns weather for Dallas, TX
```
**Parameters:**
  * Name: Name of city to grab weather from
  * Country code: two letter code (us, ru, etc.) to specify country

**Return:**
  JSON response for city
  
##Getting weather by city ID

Refer to openweathermap.com for the complete list of city IDs
```python
  getWeatherCityId('2172797') 
```
**Parameters:**
  * City ID: ID of city to grab weather from

**Return:**
  JSON response for the city
