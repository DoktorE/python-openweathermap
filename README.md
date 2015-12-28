Python API wrapper for OpenWeatherMap

#How to install
```
git clone https://github.com/DoktorE/python-openweathermap
```
```python
python setup.py install
```

#How to use
```python
from openweathermap import Client
```
Make sure you have your API key
```python
client = Client('2de143494c0b295cca9337e1e96b00e0')

data = client.getWeatherZip(12702, 'us')
print(data)
# prints returned JSON
```

#API Method Guide
