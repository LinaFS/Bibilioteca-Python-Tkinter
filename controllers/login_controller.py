class LoginController:
    def __init__(self, view):
        self.view = view
        
    def open_index_view(self, window):
        # Importar dentro del método
        from views.index_view import IndexView
        from controllers.index_controller import IndexController
        
        window.destroy()
        controller = IndexController(None)  # Inicialmente el controlador no tiene vista
        view = IndexView(controller)  # Ahora le pasamos el controlador
        controller.view = view  # Asegúrate de que el controlador tiene la vista
        
        view.run()
