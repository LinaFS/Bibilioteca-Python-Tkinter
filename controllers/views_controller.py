from models.views_model import ViewsModel

class ViewsController:
    def __init__(self, root, main_controller):
        self.root = root
        self.main_controller = main_controller  # IndexController
        self.model = ViewsModel()
    
    def mostrar_leidos(self):
        resultados = self.model.buscar_mas_leidos()
        return resultados if resultados else None

    def open_news_view(self):
        self.main_controller.open_news_page()

    def open_index_view(self):
        self.main_controller.open_index_page()

    def open_search_view(self, query):
        self.main_controller.realizar_busqueda(query)