from models.search_model import SearchModel
from models.index_model import IndexModel

class SearchController:
    def __init__(self, root, main_controller, query):
        self.root = root
        self.main_controller = main_controller
        self.model = SearchModel()
        self.query = query

    def get_data(self):
        return self.query

    def open_index_view(self):
        self.main_controller.open_index_page()

    def buscar(self, texto, filtro):
        index_model = IndexModel()
        resultados = index_model.search(texto, filtro)
        return resultados if resultados else None

    def mostrar_mas_leidos(self):
        resultados = self.model.buscar_mas_leidos()
        return resultados if resultados else None

    def realizar_busqueda(self, query):
        self.main_controller.realizar_busqueda(query)