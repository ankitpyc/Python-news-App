from baseconf import NewsConf


class NewsSources(NewsConf):
	"""docstring for NewsSources"""
	def __init__(self,API_KEY):
		super(NewsSources, self).__init__(API_KEY)
		self.API_KEY = API_KEY
		self.api_endpoint = "https://newsapi.org/v2/sources"
		self.sources = []
		self.country = []
		self.language = []
		self.source_base_information = []
 	def get(self,category=None,country=None,language="en",attributes_format=True):
 		if(category):
			self.category = category
		if(language):
			self.language = language
		if(country):
			self.language = language		
 		response = self.requests.get(self.api_endpoint,params = self.url_payload)
 		#print response.json()
 		if response.status_code != '200':
 			BaseException("Error fetching lists of resources from the Server")
 		try:
 			content = response.json()
 		except:
 			BaseException("Could not decode the response from the Server")
 		if attributes_format:
 			return self.NewsDict(content)

 		return content
 	def get_by_category(self, category):
		return self.get(category=category)

	def get_by_language(self, language):
		return self.get(language=language)

	def get_by_country(self, country):
		return self.get(country=country)

	def information(self):
		content = self.get()
		self.sources = content.sources
		for index, source in enumerate(self.sources):
			source_category_name = source['category']
			source_language_name = source['language']
			source_country_name = source['country']
			source_identifier = source['id']
			source_name = source['name']
			source_desciption = source['description']
			source_url = source['url']
			self.source_base_information[name] = source_url
			self.sources_id_info[name] = source_identifier
			temp_dict = {
                "id": source_identifier,
                "name": source_name,
                "description": source_desciption, 
                "url": source_url,
                "country" : source_country_name,
                "description" : source_desciptions
            }
			if source_category_name in self.categories:
				self.categories[category_name].append([temp_dict])
			else:
				self.categories[category_name] = [temp_dict]
			if source_language_name in self.languages:
				self.languages[language_name].append([temp_dict])
			else:
				self.languages[language_name] = [temp_dict]
			if source_country_name in self.countries:
				self.countries[country_name].append([temp_dict])
			else:
				self.countries[country_name] = [temp_dict]
		return self

	def all_sorted_information(self):
		return self.sources

	def all_categories(self, detailed=False):
		if detailed:
			return self.categories
		return self.categories.keys()

	def all_languages(self, detailed=False):
		if detailed:
			return self.languages
		return self.languages.keys()

	def all_countries(self, detailed=False):
		if detailed:
			return self.countries
		return self.countries.keys()

	def all_base_information(self):
		return self.source_base_information

	def all_ids(self, detailed=False):
		if detailed:
			return self.sources_id_info
		return self.sources_id_info.values()

	def all_names(self, detailed=False):
		if detailed:
			return self.source_base_information
		return self.source_base_information.keys()

	def all_urls(self, detailed=False):
		if detailed:
			return self.source_base_information
		return self.source_base_information.values()

	def search(self, name):
		matches = []
		if not self.sources:
			self.information()
		for source in self.sources:
			if name.lower() in source['name'].lower():
				matches.append(source)
		if not matches:
			return "No match found!"
		return matches
			



