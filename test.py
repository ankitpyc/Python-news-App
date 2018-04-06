#testing of the Current APP

from NewsApp.NewsArticles import Articles
from NewsApp.NewsSources import NewsSources
articles =	Articles(API_KEY = "496f260a6944479db35a90652542e274")
articles.get()
s = NewsSources(API_KEY = "496f260a6944479db35a90652542e274")
print s.get()	