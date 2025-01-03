from views.login_view import LoginView
from controllers.login_controller import LoginController
from models.index_model import IndexModel

class IndexController:
    def __init__(self, view):
        self.view = view
        self.model = IndexModel()

    def iniciar_sesion(self, window):
        print("Cambiando de pantalla...")
        window.destroy()

        controller = LoginController(None)
        view = LoginView(controller)
        controller.view = view
        # Ejecutar la vista de Login
        view.run()