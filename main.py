from views.login_view import LoginView
from controllers.login_controller import LoginController
from controllers.index_controller import IndexController
from views.index_view import IndexView

def main():
    # Crear vista y controlador
    view = IndexView(IndexController)
    controller = IndexController
    #view = LoginView(LoginController) vistas del login
    #controller = LoginController(view) controller del login
    
    # Vincular controlador a vista
    #view.controller = controller
    view.controller = controller
    # Ejecutar aplicación
    view.run()

if __name__ == "__main__":
    main()