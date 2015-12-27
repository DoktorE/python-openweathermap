import json
import requests

class Client(object):
	""" Main class to preform and interact with the API """

	def __init__(self, url):
		if not url.endswith('/'):
			url += '/'
		self.url = url

	def _request(self, endpoint, method, appid='', data=None, **kwargs):
		"""
		Function to handle GET and POST requests

		:param endpoint: endpoint for the API
		:param method: method type for request
		:param appid: API key
		:param data: POST data
		:param kwargs: extra arguments

		:return: request response
		"""
		total_url = self.url + endpoint + '&appid=' + appid

		r = self.session

		if method == 'get':
			request = r.get(total_url, **kwargs)
		else:
			request = r.post(total_url, data, **kwargs)

		request.raise_for_status()

		if len(request.text) == 0:
			data = json.loads('{}')
		else:
			try:
				data = json.loads(request.text)
			except ValueError:
				data = request.text

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

	def getWeatherZip(self, zip_code, country_code):
		"""
		Function to get the weather based on a zip code

		:param zip_code: zip code to pass into the request
		:param country_code: two letter code (ex: 'us') to pass into the request

		:return: weather from request
		"""
		return self._get('/data/2.5/weather?zip=' + zip_code + ',' + country_code)
