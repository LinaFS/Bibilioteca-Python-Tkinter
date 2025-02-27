from models.views_model import ViewsModel

class ViewsController:
    def __init__(self, view):
        self.view = view
        self.model = ViewsModel()   
    
    def mostrar_leidos(self):
        """Lógica para mostrar los artículos en novedades."""     
        resultados = self.model.buscar_mas_leidos()
        if len(resultados) == 0:
            return None
        else:
            return resultados

    def open_news_view(self, window):
        from views.news_view import NewsView
        from controllers.news_controller import NewsController
        print("Cambiando a la vista de novedades...")
        window.destroy()  # Cierra la ventana actual
        controller = NewsController(None)
        view = NewsView(controller)
        controller.view = view
        view.run()

    def open_index_view(self, window):
        # Importar dentro del método
        from views.index_view import IndexView
        from controllers.index_controller import IndexController
        
        window.destroy()
        controller = IndexController(None)  # Inicialmente el controlador no tiene vista
        view = IndexView(controller)  # Ahora le pasamos el controlador
        controller.view = view  # Asegúrate de que el controlador tiene la vista
        
        view.run()

    def open_search_view(self, window, query):
        from views.search_view import SearchView
        from controllers.search_controller import SearchController
        print("Cambiando a la vista de búsqueda...")
        window.destroy()  # Cierra la ventana actual
        controller = SearchController(None, query)
        view = SearchView(controller)
        controller.view = view
        view.run()