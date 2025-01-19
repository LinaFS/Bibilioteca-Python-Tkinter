from views.login_view import LoginView
from controllers.login_controller import LoginController
from models.index_model import IndexModel
from views.search_view import SearchView

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
    
    def realizar_busqueda(self, window):
        
        print("Cambiando a la vista de búsqueda...")
        window.destroy()  # Cierra la ventana actual

        # Crear y mostrar la vista de búsqueda
        search_view = SearchView(self)
        self.view = search_view
        search_view.run()
        
    def open_index_view(self, window):
        # Importar dentro del método
        from views.index_view import IndexView
        from controllers.index_controller import IndexController
        
        window.destroy()
        controller = IndexController(None)  # Inicialmente el controlador no tiene vista
        view = IndexView(controller)  # Ahora le pasamos el controlador
        controller.view = view  # Asegúrate de que el controlador tiene la vista
        
        view.run()