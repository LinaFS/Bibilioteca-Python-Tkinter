import sys
import os
import tkinter as tk
from tkinter import messagebox
from controllers.index_controller import IndexController
from models.firebase_config import FirebaseConfig

def resource_path(relative_path):
    """
    Sistema de rutas mejorado para desarrollo y producción.
    Busca el archivo dentro de la carpeta temporal de PyInstaller (sys._MEIPASS)
    o en el directorio actual (os.path.abspath(".")).
    """
    try:
        # Si la app está "congelada" (ejecutable), usa sys._MEIPASS
        base_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.abspath(".")
        path = os.path.join(base_path, relative_path)
        return path
    except Exception as e:
        messagebox.showerror("Error de Ruta", f"Error en resource_path: {str(e)}")
        return relative_path 

def main():
    try:
        # Configuración inicial crítica
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # 1. Obtener la ruta del archivo de credenciales usando resource_path
        relative_cred_path = "firebase-credentials.json"
        final_cred_path = resource_path(relative_cred_path)
        
        # 2. Inicializar Firebase, pasando la ruta del archivo de credenciales
        print("🔥 Inicializando Firebase...")
        # *** CAMBIO CLAVE: Pasamos la ruta resuelta ***
        firebase = FirebaseConfig(final_cred_path) 
        
        if not firebase.is_connected():
            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar a Firebase.\n\n"
                "Verifica que:\n"
                f"1. El archivo firebase-credentials.json existe en {final_cred_path}\n"
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