from models.search_model import SearchModel

class SearchController:
    def __init__(self, view, query):
        self.view = view
        self.query = query
        self.model = SearchModel()


    def get_data(self):
        print("Mostrando resultados:")
        print(self.query)
        return self.query

    def buscar(self, texto):
        """Lógica para la búsqueda."""
       

    def mostrar_mas_leidos(self):
        """Lógica para mostrar los artículos más leídos."""
       

    def mostrar_novedades(self):
        """Lógica para mostrar los artículos en novedades."""
