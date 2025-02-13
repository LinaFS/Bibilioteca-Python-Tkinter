from views.login_view import LoginView
from controllers.login_controller import LoginController
from models.index_model import IndexModel
from views.search_view import SearchView
from controllers.search_controller import SearchController

class IndexController:
    def __init__(self, view):
        self.view = view
        self.model = IndexModel()

    def iniciar_sesion(self, window):
        print("Cambiando a la vista de inicio de sesión...")
        window.destroy()

        # Crear y configurar el controlador y la vista de inicio de sesión
        controller = LoginController(None)
        view = LoginView(controller)
        controller.view = view
        view.run()  # Ejecutar la vista de inicio de sesión
    
    def realizar_busqueda(self, window, query):
        print("Cambiando a la vista de búsqueda...")
        window.destroy()  # Cierra la ventana actual
        controller = SearchController(None, query)
        view = SearchView(controller)
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

    def open_news_page(self, window):
        from views.news_view import NewsView
        from controllers.news_controller import NewsController
        
        print("Cambiando a página de novedades...")
        window.destroy()
        controller = NewsView(None)
        view = NewsController(controller)
        controller.run()

