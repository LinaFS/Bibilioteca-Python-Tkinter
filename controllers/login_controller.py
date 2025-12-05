from models.login_model import LoginModel
import tkinter as tk
from tkinter import messagebox # <--- Necesario para mostrar errores

class LoginController:
    def __init__(self, root, main_controller):
        # ... (código existente) ...
        self.root = root
        self.main_controller = main_controller  # IndexController
        self.model = LoginModel()
    
    def open_index_view(self):
        self.main_controller.open_index_page()

    def open_panelAdmin_view(self, user, passwd):
        # 1. Intentar crear la sesión (verifica credenciales)
        success = self.model.create_session(user, passwd) 
        
        if success:
            # 2. VERIFICACIÓN DE PERMISOS: Solo si las credenciales son correctas
            if self.model.is_admin():
                self.main_controller.open_admin_page()
            else:
                # 3. Acceso denegado: El usuario tiene credenciales, pero no permisos de admin (permisos != 1)
                messagebox.showerror("Acceso Denegado", "Sus credenciales no tienen permiso para acceder al Panel de Administrador.")
                self.model.close_session() # Cierra la sesión que acabamos de crear
                return False
        else:
            # 4. Error de credenciales (Manejado en LoginModel)
            messagebox.showerror("Error de Sesión", "Nombre de usuario o contraseña incorrectos.")
            return False