from models.login_model import LoginModel
# Debes asegurar que este import funcione y AdminModel exista y tenga los métodos CRUD
from models.admin_model import AdminModel 
import tkinter as tk
from tkinter import messagebox

class AdminController:
    def __init__(self, root, main_controller):
        self.root = root
        self.main_controller = main_controller
        self.login_model = LoginModel()
        # Asumiendo que AdminModel ya existe y está configurado
        self.admin_model = AdminModel() 
        self.admin_view = None 
        self.article_to_edit = None # Usado para pasar datos al formulario de edición

    # --- MÉTODO CLAVE PARA SOLUCIONAR EL ERROR ---
    def set_admin_view(self, view_instance):
        """Asigna la instancia de PanelAdminView para control interno."""
        self.admin_view = view_instance
    
    def close_session(self):
        event = self.login_model.close_session()
        if event:
            self.main_controller.open_index_page()
            
    # --- Métodos de Navegación Interna (Switch de Frames) ---
    
    def switch_to_add(self, article_data=None):
        """Prepara los datos (si es edición) y notifica al PanelAdminView para mostrar el formulario Añadir/Editar."""
        self.article_to_edit = article_data 
        if self.admin_view:
            self.admin_view.show_frame("Add")
    
    def switch_to_consult(self):
        """Notifica al PanelAdminView para mostrar la tabla de Consulta/Gestión."""
        self.article_to_edit = None
        if self.admin_view:
            self.admin_view.show_frame("Consult")

    # --- Métodos de Lógica (CRUD) ---
    
    def get_articles_for_consult(self, search_term=None):
        """Obtiene y/o busca los artículos para la vista de consulta."""
        if search_term:
            return self.admin_model.search_articles(search_term)
        return self.admin_model.get_all_articles()

    def get_article_to_edit(self):
        """Retorna el objeto Articulo a editar o None para el formulario."""
        return self.article_to_edit

    def save_material(self, data):
        """Guarda o actualiza el material, dependiendo de si tiene ID."""
        article_id = data.pop('id_artic', None)
        success = False
        
        if article_id:
            success = self.admin_model.update_article(article_id, data)
            message = "actualizado"
        else:
            success = self.admin_model.create_article(data)
            message = "agregado"
            
        if success:
            messagebox.showinfo("Éxito", f"Material {message} correctamente.")
        else:
            messagebox.showerror("Error", f"Error al {message} el material.")
            
        # Volvemos a la vista de Consulta
        self.switch_to_consult()
        
    def start_edit_article(self, article_id):
        """Carga el artículo completo y redirige al formulario de edición."""
        article = self.admin_model.get_article_by_id(article_id)
        if article:
            # Convertir namedtuple a diccionario
            article_data = article._asdict()
            self.switch_to_add(article_data) # Redirige al formulario con datos
        else:
            messagebox.showerror("Error", "No se pudo cargar el artículo para editar.")

    def delete_article_action(self, article_id):
        """Elimina un artículo previa confirmación."""
        if messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar este artículo de forma permanente?"):
            success = self.admin_model.delete_article(article_id)
            if success:
                messagebox.showinfo("Éxito", "Artículo eliminado correctamente.")
            else:
                messagebox.showerror("Error", "Error al eliminar el artículo.")
            
            # Recargar la vista de consulta (asumiendo que está visible)
            if self.admin_view and self.admin_view.current_frame == "Consult":
                 self.admin_view.frames["Consult"].load_data()