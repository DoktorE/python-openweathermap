import json
import requests

class Client(object):
	""" Main class to preform and interact with the API """

	def __init__(self, url, appid):
		if not url.endswith('/'):
			url += '/'
		self.url = url
		self.appid = appid

	def _request(self, endpoint, method, data=None, **kwargs):
		"""
		Function to handle GET and POST requests

		:param endpoint: endpoint for the API
		:param method: method type for request
		:param appid: API key
		:param data: POST data
		:param kwargs: extra arguments

		:return: request response
		"""
		total_url = self.url + endpoint + '&appid=' + self.appid

		if method == 'get':
			r = requests.get(total_url, **kwargs)
		else:
			r = requests.post(total_url, data, **kwargs)

		r.raise_for_status()

		if len(r.text) == 0:
			data = json.loads('{}')
		else:
			try:
				data = json.loads(r.text)
			except ValueError:
				data = r.text

		return data

	def _get(self, endpoint, **kwargs):
		"""
		Function to preform GET requests

		:param endpoint: endpoint of the API
		:param kwargs: extra arguments

		:return: GET response
		"""
		return self._request(endpoint, 'get', **kwargs)

	def _post(self, endpoint, data, **kwargs):
		"""
		Function to preform POST requests

		:param endpoint: endpoint of the API
		:param data: data to be sent with the request
		:param kwargs: extra arguments

		:return: POST response
		"""
		return self.request(endpoint, 'post', data, **kwargs)

	def getWeatherCity(self, city_name, country_code=None):
		"""
		Function to get the weather based on the name of a city

		:param city_name: name of city to pass into the request
		:param country_code: two letter code (ex: 'us') to pass into the request

		:return: weather from request
		"""
		return self._get('data/2.5/weather?q=', city_name + ',' + country_code)

	def getWeatherCityId(self, city_id):
		"""
		Function to get the weather based on it's city id (refer to OpenWeatherMap's own documentation to get a list of city ids)

		:param city_id: city id of city
		:return: weather from request
		"""
		return self._get('data/2.5/weather?id=', city_id);

	def getWeatherZip(self, zip_code, country_code=None):
		"""
		Function to get the weather based on a zip code

		:param zip_code: zip code to pass into the request
		:param country_code: two letter code (ex: 'us') to pass into the request

		:return: weather from request
		"""
		return self._get('/data/2.5/weather?zip=' + zip_code + ',' + country_code)

	def getWeatherRec(self, bbox, cluster='no'):
		"""
		Function to get the weather for multiple cities in a rectangular area

		:param bbox: array of 5 numbers to describe the bounding box (lat of the top left point, lon of the top left point, lat of the bottom right point, lon of the bottom right point, map zoom)
		:param cluster: use server clustering of points (yes, no) (default: no)

		:return: weather of cities in the bounding box
		"""
		bbox = ",".join(bbox)
		return self._get('data/2.5/box/city?=' + bbox + '&cluster=' + cluster)

	def getWeatherCycle(self, lat, lon, cnt, cluster='no'):
		"""
		Function to get weather from cities laid within definite circle that is specified by center point ('lat', 'lon') and expected number of cities ('cnt') around this point

		:param lat: latitude of the center point
		:param lon: longitude of the center point
		:param cluster: use server clustering of points (yes, no) (default: no)
		:param cnt: expected number of cities laid within circle

		:return: weather of cities in the circle
		"""
		#http://api.openweathermap.org/data/2.5/find?lat=55.5&lon=37.5&cnt=10
		return self._get('data/2.5/find?lat=' + lat + '&lon=' + lon + '&cnt=' + cnt)

	def getCityGroup(self, city_ids=""):
		"""
		Function to get the weather from multiple city IDs

		:param city_ids: array of city ids

		:return: weather for each of the city IDs
		"""
		city_ids = ','.join(str(i) for i in city_ids)

		print(city_ids)

		return self._get('data/2.5/group?id=')