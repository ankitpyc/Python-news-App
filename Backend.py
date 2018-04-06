import htmlPy
import json
import time
from NewsApp.NewsArticles import Articles
from NewsApp.NewsSources import NewsSources
# from App_init import myapp as htmlPyapp  


class NewsBack(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self,appgui):
        super(NewsBack,self).__init__()
        self.appgui = appgui
        # Initialize the class here, if required.
        return

    @htmlPy.Slot()
    def openfeed(self):
        articles =Articles(API_KEY = "496f260a6944479db35a90652542e274")
        self.appgui.template = ("templates/loading.html",{})
        self.appgui.height = 760
        self.appgui.width = 1024
        self.appgui.template = ("templates/Feeds.html", {"articles": articles.get()})
        # This is the function exposed to GUI events.
        # You can change app HTML from here.
        # Or, you can do pretty much any python from here.
        #
        # NOTE: @htmlPy.Slot decorater needs argument and return data-types.
        # Refer to API documentation.
        return

    @htmlPy.Slot(str, result=str)
    def form_function_name(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot()
    def javascript_function(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI
        return

    @htmlPy.Slot()
    def get_news_sources(self):
        sources = NewsSources(API_KEY = "496f260a6944479db35a90652542e274")
        self.appgui.template = ("templates/sources.html", {"sources": sources.get()})





## You have to bind the class instance to the AppGUI instance to be
## callable from GUI
