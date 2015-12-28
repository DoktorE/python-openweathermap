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
##Getting weather by geographical coordinates
```python
  getWeatherCoord(55.5, 72.5)
```
**Parameters:**
  * lat: latitudinal coordinate
  * lon: longitudinal coordinate

**Return:**
  JSON response for the area described by the geographical coordinates

##Getting weather for a rectangular area
```python
  getWeatherRec([55, 65, 75, 85, 11)
```
**Parameters:**
  * bbox: array of 5 numbers to describe the bounding box (lat of the top left point, lon of the top left point, lat of the bottom right point, lon of the bottom right point, map zoom)

**Return:**
  JSON response for the cities inside of the bounding box

##Getting weather in cycle
```python
  getWeatherCycle(55.5, 75.2, 10)
```
Gets weather from cities laid within definite circle that is specified by a center point ('lat', 'lon') and expected number of cities ('cnt') around the point
**Parameters:**
  * lat: latitudinal coordinate for center point of circle
  * lon: longitudinal coordinate for center point of circle
  * cnt: expected number of cities around circle
**Return:**
  Number of expected cities inside circle

##Getting weather in a group
```python
  getWeatherGroup([48549386, 1759265, 2859584, 2859573])
```
**Parameters:**
  * city_ids: array of city IDs 
**Return:**
  Weather for each city ID specified in array 
