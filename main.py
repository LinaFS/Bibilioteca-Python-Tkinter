import sys
import os
import tkinter as tk
from tkinter import messagebox
from controllers.index_controller import IndexController
from models.firebase_config import FirebaseConfig

def resource_path(relative_path):
    """Sistema de rutas mejorado para desarrollo y producción"""
    try:
        base_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.abspath(".")
        path = os.path.join(base_path, relative_path)
        return path
    except Exception as e:
        messagebox.showerror("Error", f"Error en resource_path: {str(e)}")
        return relative_path

def main():
    try:
        # Configuración inicial crítica
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Inicializar Firebase
        print("🔥 Inicializando Firebase...")
        firebase = FirebaseConfig()
        
        if not firebase.is_connected():
            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar a Firebase.\n\n"
                "Verifica que:\n"
                "1. El archivo firebase-credentials.json existe\n"
                "2. Las credenciales son correctas\n"
                "3. Tienes conexión a internet"
            )
            return
        
        print("✅ Firebase conectado correctamente")
        
        # Crear ventana principal
        root = tk.Tk()
        root.title("Biblioteca App")
        root.geometry("800x600")
        
        # Configuración de grid principal
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        # Inicialización controlador
        controller = IndexController(root)
        
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror(
            "Error fatal", 
            f"Error al iniciar la aplicación:\n{str(e)}\n\n"
            f"Asegúrate de que Firebase está configurado correctamente."
        )

if __name__ == "__main__":
    main()