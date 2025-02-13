from models.news_model import NewsModel

class NewsController:
    def __init__(self, view):
        self.view = view
        self.model = NewsModel()