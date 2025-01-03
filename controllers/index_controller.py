from views.login_view import LoginView
from controllers.login_controller import LoginController

class IndexController:
    def __init__(self, view):
        self.view = view

    def iniciar_sesion(self, window):
        print("Cambiando de pantalla...")
        window.destroy()

        # Crear la vista de Login
        login_view = LoginView(None)
        login_controller = LoginController(login_view)
        login_view.controller = login_controller

        # Ejecutar la vista de Login
        login_view.run()

