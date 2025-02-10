from models.login_model import LoginModel

class AdminController:
    def __init__(self, view):
        self.view = view
        self.model = LoginModel()

    def close_session_view (self, window):
        event = self.model.close_session()
        if event==True:
            from views.index_view import IndexView
            from controllers.index_controller import IndexController
        
            window.destroy()
            controller = IndexController(None)  # Inicialmente el controlador no tiene vista
            view = IndexView(controller)  # Ahora le pasamos el controlador
            controller.view = view  # Asegúrate de que el controlador tiene la vista
            
            view.run()