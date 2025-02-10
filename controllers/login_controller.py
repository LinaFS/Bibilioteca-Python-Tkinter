from models.login_model import LoginModel
from tkinter import messagebox

class LoginController:
    def __init__(self, view):
        self.view = view
        self.model = LoginModel()
        
    def open_index_view(self, window):
        # Importar dentro del método
        from views.index_view import IndexView
        from controllers.index_controller import IndexController
        
        window.destroy()
        controller = IndexController(None)  # Inicialmente el controlador no tiene vista
        view = IndexView(controller)  # Ahora le pasamos el controlador
        controller.view = view  # Asegúrate de que el controlador tiene la vista
        
        view.run()
        
    def open_panelAdmin_view (self, window, user, passwd):
        event=self.model.create_session(user, passwd)
        
        if(event==True):
            from views.panel_admin_view import panelAdminView
            from controllers.admin_controller import AdminController

            window.destroy()
            controller = AdminController(None)
            view = panelAdminView(controller)
            controller.view = view
            
            view.run()
        else:
            messagebox.showwarning("Advertencia","Revise los datos de sesión")
        