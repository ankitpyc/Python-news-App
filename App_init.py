import htmlPy
import os
from PyQt4 import QtCore, QtGui
from NewsApp.NewsArticles import Articles
from config import init_configuration
  

myapp = htmlPy.AppGUI(title=u"NewsBytes")
articles =Articles(API_KEY = "496f260a6944479db35a90652542e274")
myapp = init_configuration(myapp)
myapp.template = ("index.html", {"articles": articles.get()})
from Backend import NewsBack
# Register back-end functionalities


myapp.bind(NewsBack(myapp))
if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    myapp.start()


