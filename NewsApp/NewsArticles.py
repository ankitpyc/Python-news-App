from NewsApp.baseconf import NewsConf


class Articles(NewsConf):
	"""docstring for Articles"""
	''' Articles basically retrieves all news from all sources'''
	def __init__(self, API_KEY):
		super(Articles,self).__init__(API_KEY)
		self.API_KEY = API_KEY
		self.endpoint = "https://newsapi.org/v2/everything"

	def get(self,source="abc-news",keyword = None,sort_by="publishedAt",domains=None, attributes_format=True):
		if(keyword):
			self.url_payload["q"] = keyword
		self.url_payload["sources"] = source
		self.url_payload["sortby"] = sort_by 
		response = self.requests.get(self.endpoint,params=self.url_payload)
		if response.status_code != 200:
			BaseException("Either the Server or Down or Articles couldn't be Fetched")
		try:
			content = response.json()
			#print content
		except:
			ValueError("No response content")
		if(attributes_format):
			return self.NewsDict(content)
	def get_by_popularity(self,source):
		return self.get(source,sort_by="popularity")

	def get_by_relevance(self,source,keyword):
		return self.get(source, sort_by="latest")
