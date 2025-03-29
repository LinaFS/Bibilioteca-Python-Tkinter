from models.news_model import NewsModel

class NewsController:
    def __init__(self, root, main_controller):
        self.root = root
        self.main_controller = main_controller
        self.model = NewsModel()
    
    def mostrar_novedades(self):
        """Lógica para mostrar los artículos en novedades."""     
        resultados = self.model.buscar_novedades()
        return resultados if resultados else None

    def open_most_view(self):
        self.main_controller.open_views_page()

    def open_index_view(self):
        self.main_controller.open_index_page()

    def open_search_view(self, query):
        self.main_controller.realizar_busqueda(query)