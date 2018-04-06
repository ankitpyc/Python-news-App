import requests

class NewsDict(dict):
    def __init__(self, *args, **kwargs):
        super(NewsDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class NewsConf(object):
	def __init__(self,API_KEY):
		self.API_KEY = API_KEY
		self.url_payload = {"apiKey":self.API_KEY}
		self.NewsDict = NewsDict
		self.requests = requests