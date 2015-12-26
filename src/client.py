import json

# API Key: bf3844714352ff4d788cda36b7710e92

class Client(object):
	""" Main class to preform and interact with the API """

	def __init__(self, url):
		if not url.endswith('/'):
			url += '/'
		self.url = url

	def _api_get():
		