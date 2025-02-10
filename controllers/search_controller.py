from models.search_model import SearchModel
from models.index_model import *

class SearchController:
    def __init__(self, view, query):
        self.view = view
        self.query = query
        self.model = SearchModel()

    def get_data(self):
        #print("Mostrando resultados:")
        #print(self.query)
        return self.query

    def open_index_view(self, window):
        # Importar dentro del método
        from views.index_view import IndexView
        from controllers.index_controller import IndexController
        
        window.destroy()
        controller = IndexController(None)  # Inicialmente el controlador no tiene vista
        view = IndexView(controller)  # Ahora le pasamos el controlador
        controller.view = view  # Asegúrate de que el controlador tiene la vista
        
        view.run()
    
    def buscar(self, texto,filter):
        """Lógica para la búsqueda."""
        index_model = IndexModel()
        resultados = index_model.search(texto, filter)
        if len(resultados) == 0:
            return None
        else:
            return resultados


    def mostrar_mas_leidos(self):
        """Lógica para mostrar los artículos más leídos."""
        resultados = self.model.buscar_mas_leidos()
        if len(resultados) == 0:
            return None
        else:
            return resultados 
        
       

    def mostrar_novedades(self):
        """Lógica para mostrar los artículos en novedades."""     
        resultados = self.model.buscar_novedades()
        if len(resultados) == 0:
            return None
        else:
            return resultados   
