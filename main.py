import sys
import os
import tkinter as tk
from tkinter import messagebox
from controllers.index_controller import IndexController
from models.conexion import init_conexion

def resource_path(relative_path):
    """Sistema de rutas mejorado para desarrollo y producción"""
    try:
        base_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.abspath(".")
        path = os.path.join(base_path, relative_path)
        return path
    except Exception as e:
        messagebox.showerror("Error", f"Error en resource_path: {str(e)}")
        return relative_path  # Fallback

def main():
    try:
        # Configuración inicial crítica
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        root = tk.Tk()
        root.title("Biblioteca App")
        root.geometry("800x600")  # Tamaño explícito
        
        # DEBUG: Marco de verificación
        debug_frame = tk.Frame(root, bd=2, relief="groove")
        debug_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        tk.Label(debug_frame, text="DEBUG: UI Principal Cargada", fg="green").grid(row=0, column=0)
        
        # Configuración de grid principal
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        # Inicialización controlador
        controller = IndexController(root)
        
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Error fatal", 
                           f"Error al iniciar la aplicación:\n{str(e)}")

if __name__ == "__main__":
    main()