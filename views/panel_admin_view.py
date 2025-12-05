from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Tk, Frame, Label, ttk, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import os
import sys


def _get_resource_path(relative_path: str) -> str:
    base_path = getattr(sys, '_MEIPASS', None)
    if base_path is None:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base_path, relative_path)

# IMPORTANTE: Asegúrate de que estas clases existan en sus archivos correspondientes
# Ya que PanelAdminView las necesita para crear los frames internos.
from views.admin_add_view import AdminAddView 
from views.admin_consult_view import AdminConsultView 

class PanelAdminView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        
        # 1. Asigna la instancia al controlador (para comunicación interna)
        self.controller.set_admin_view(self) 

        self.frames = {}
        self.current_frame = None
        self.resized_images = [] # Lista para evitar que las imágenes redimensionadas se eliminen
        
        # 2. Configuración inicial y carga de recursos (¡Corregido!)
        self._configure_window() # Mantenido de tu código base
        self._load_images()
        
        # 3. Configuración de Grid (Barra Lateral + Contenido)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0) # Barra lateral
        self.grid_columnconfigure(1, weight=1) # Contenido dinámico
        
        # 4. Creación de componentes
        self._create_sidebar()
        self._create_content_container()
        self._setup_frames(AdminAddView, AdminConsultView)
        
        # 5. Inicia en la vista de Consulta
        self.show_frame("Consult") 
        self._setup_event_handlers() # Se mantiene para consistencia, aunque esté vacío

    # --- PATH SETUP METHODS (Añadidos para corregir el AttributeError) ---
    def relative_to_assets(self, path: str) -> str:
        rel = os.path.join("guiBuild", "panelAdmin", "assets", "frame0", path)
        return _get_resource_path(rel)
    # --- END PATH SETUP METHODS ---

    def _configure_window(self):
        self.configure(bg="#C4C4C4")

    def _load_images(self):
        """Carga las rutas de las imágenes que se usarán en la barra lateral."""
        # Se necesita PIL para las miniaturas dinámicas, pero aquí solo guardamos las rutas.
        self.add_icon_path = self.relative_to_assets("image_3.png")
        self.modify_icon_path = self.relative_to_assets("image_2.png")
        self.consult_icon_path = self.relative_to_assets("image_5.png")
        self.delete_icon_path = self.relative_to_assets("image_4.png")
        # Cargar imagen de fondo si fuera necesaria, aunque ya no se usa en esta vista centralizada
        # self.background_image = PhotoImage(file=self.relative_to_assets("image_1.png"))

    def _create_sidebar(self):
        """Crea la barra lateral de navegación con iconos CRUD."""
        self.sidebar_frame = Frame(self, bg="#342217", width=150)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_propagate(False) 

        # Título
        Label(self.sidebar_frame, text="Admin", bg="#342217", fg="white", 
              font=("IstokWeb Bold", 20)).pack(pady=(20, 10))
        
        # Botones CRUD: Añadir y Consultar/Gestión
        self._create_nav_button("Añadir", self.add_icon_path, 
                                 self.controller.switch_to_add)
        # El botón Consultar/Gestionar combina Consultar, Modificar y Eliminar
        self._create_nav_button("Gestionar", self.consult_icon_path, 
                                 self.controller.switch_to_consult)
        
        # Cerrar Sesión
        self._create_nav_button("Cerrar Sesión", None, 
                                 self.controller.close_session, is_bottom=True)

    def _create_nav_button(self, text, icon_path, command, is_bottom=False):
        """Crea un botón de navegación con ícono y texto."""
        btn = Frame(self.sidebar_frame, bg="#342217")
        if is_bottom:
            btn.pack(side="bottom", fill="x", pady=(20, 10))
        else:
            btn.pack(fill="x", pady=5)
        
        if icon_path:
            # Uso de PIL para cargar y redimensionar el ícono
            try:
                img = Image.open(icon_path) 
                icon_small = ImageTk.PhotoImage(img.resize((30, 30), Image.LANCZOS))
            except Exception as e:
                print(f"Error al cargar ícono en PanelAdminView: {e}")
                icon_small = PhotoImage(file=icon_path).subsample(2) 

            icon_label = Label(btn, image=icon_small, bg="#342217")
            icon_label.pack(side="left", padx=10)
            self.resized_images.append(icon_small) 
        
        text_label = Label(btn, text=text, bg="#342217", fg="white", font=("Inter", 12))
        text_label.pack(side="left", padx=5)
        
        # Asignar comando de clic a todos los elementos del botón
        btn.bind("<Button-1>", lambda e: command())
        for child in btn.winfo_children():
            child.bind("<Button-1>", lambda e: command())
            
        return btn

    def _create_content_container(self):
        """Crea el frame donde se mostrarán las vistas CRUD."""
        self.content_container = Frame(self, bg="#FFFFFF")
        self.content_container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.content_container.grid_rowconfigure(0, weight=1)
        self.content_container.grid_columnconfigure(0, weight=1)

    def _setup_frames(self, AdminAddView, AdminConsultView):
        """Instancia todas las vistas CRUD internas (Frames)."""

        # Frame de Consulta (Gestionar, Editar, Eliminar)
        frame_consult = AdminConsultView(self.content_container, self.controller)
        self.frames["Consult"] = frame_consult
        frame_consult.grid(row=0, column=0, sticky="nsew")

        # Frame de Añadir/Editar
        frame_add = AdminAddView(self.content_container, self.controller)
        self.frames["Add"] = frame_add
        frame_add.grid(row=0, column=0, sticky="nsew")


    def show_frame(self, page_name):
        """Muestra el frame solicitado y llama a la función de carga de datos."""
        frame = self.frames.get(page_name)
        if frame:
            frame.tkraise() 
            self.current_frame = page_name
            
            if page_name == "Consult" and hasattr(frame, 'load_data'):
                frame.load_data() 
            elif page_name == "Add" and hasattr(frame, 'load_form'):
                # Carga el formulario en modo Añadir o Editar
                frame.load_form() 
        else:
            messagebox.showerror("Error de Navegación", f"La vista '{page_name}' no se encontró.")

    def _setup_event_handlers(self):
        pass

    def run(self):
        self.parent.mainloop()