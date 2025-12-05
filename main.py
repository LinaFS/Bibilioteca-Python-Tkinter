import tkinter as tk
from views.index_view import IndexView
from controllers.login_controller import LoginController
from views.login_view import LoginView
from controllers.search_controller import SearchController
from views.search_view import SearchView
from controllers.news_controller import NewsController
from views.news_view import NewsView
from controllers.views_controller import ViewsController
from views.views_view import ViewsView
from controllers.admin_controller import AdminController
from views.panel_admin_view import PanelAdminView
# Ya no se importa AdminAddView o AdminConsultView, se manejan internamente

class IndexController:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        
        # Configuración de la ventana principal
        self.root.title("Biblioteca")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        
        # Configuración del grid principal
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Contenedor principal para todas las vistas
        self.main_container  = tk.Frame(self.root)
        self.main_container .grid(row=0, column=0, sticky="nsew")
        self.main_container .grid_rowconfigure(0, weight=1)
        self.main_container .grid_columnconfigure(0, weight=1)
        
        # Creamos una única instancia del AdminController para todas sus vistas
        admin_controller_instance = AdminController(self.root, self)

        self.view_classes = {
            "IndexView": IndexView,
            "LoginView": LoginView,
            "SearchView": SearchView,
            "NewsView": NewsView,
            "ViewsView": ViewsView,
            # Solo mantenemos la vista principal del administrador
            "PanelAdminView": PanelAdminView,
        }

        self.controllers = {
            "IndexView": self,
            "LoginView": LoginController(self.root, self),
            "SearchView": SearchController(self.root, self, None),
            "NewsView": NewsController(self.root, self),
            "ViewsView": ViewsController(self.root, self),
            # Asignamos la única instancia del controlador de administración
            "PanelAdminView": admin_controller_instance, 
        }

        self.open_index_page()

    def show_view(self, view_name):
        # Destruir vista actual correctamente
        if self.current_view is not None:
            self.current_view.destroy()
            self.current_view = None

        # Verificar si la vista existe
        if view_name not in self.view_classes:
            raise ValueError(f"Vista no encontrada: {view_name}")

        # Crear nueva vista EN EL CONTENEDOR PRINCIPAL
        view_class = self.view_classes[view_name]
        controller = self.controllers[view_name]
        
        self.current_view = view_class(parent=self.main_container, controller=controller)
        self.current_view.grid(row=0, column=0, sticky="nsew")
        
        # Forzar actualización
        self.main_container.update_idletasks()
        
        # DEBUG: Mostrar nombre de la vista actual
        print(f"Vista actual: {view_name}")

    # Métodos de navegación
    def open_index_page(self):
        self.show_view("IndexView")

    def iniciar_sesion(self):
        self.show_view("LoginView")

    def realizar_busqueda(self, query):
        # Actualizar el controlador de búsqueda con la nueva query
        self.controllers["SearchView"] = SearchController(self.root, self, query)
        self.show_view("SearchView")

    def open_news_page(self):
        self.show_view("NewsView")

    def open_views_page(self):
        self.show_view("ViewsView")
    
    def open_admin_page(self):
        self.show_view("PanelAdminView")


if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = IndexController(root)
        print("Iniciando aplicación Biblioteca...")
        root.mainloop()
    except Exception as e:
        # Mostrar traceback en consola para ayudar al debug
        import traceback
        print("Error al iniciar la aplicación:")
        traceback.print_exc()
        raise