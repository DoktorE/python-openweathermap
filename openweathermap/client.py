import json
import requests

class Client(object):
	""" Main class to preform and interact with the API """

	def __init__(self, url):
		if not url.endswith('/'):
			url += '/'
		self.url = url

	def _request(self, endpoint, method, data=None, **kwargs):
		"""
		Function to handle GET and POST requests

		:param endpoint: endpoint for the API
		:param method: method type for request
		:param data: POST data
		:param kwargs: extra arguments

		:return: request response
		"""

		total_url = self.url + endpoint

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

	def getWeatherZip(self, zip_code, country_code, appid=''):
		"""
		Function to get the weather based on a zip code

		:param query: query to pass into the request
		:param appid: api key to pass into the request
		"""

		return self._get('/data/2.5/weather?zip=' + zip_code + ',' + country_code, + '&appid=' + appid)
