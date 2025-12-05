from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage, BooleanVar
import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        
        # Configuración inicial
        self._setup_paths()
        self._configure_window()
        self._load_images()
        self._create_main_canvas()
        self._create_ui_elements()
        self._setup_event_handlers()
    
    def _setup_paths(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"../guiBuild/login/assets/frame0")
    
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def _configure_window(self):
        self.configure(bg="#C4C4C4")
    
    def _load_images(self):
        """Carga todas las imágenes necesarias"""
        self.background_image = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.login_icon = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.password_icon = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.login_button_img = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.entry_bg_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
    
    def _create_main_canvas(self):
        """Crea el canvas principal y los elementos base"""
        self.canvas = Canvas(
            self.parent,
            bg="#FFFFFF",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        # Fondo
        self.canvas.create_image(400.0, 250.0, image=self.background_image)
        self.canvas.create_rectangle(400.0, 0.0, 800.0, 500.0, fill="#BC9585", outline="")
        
        # Texto del panel
        self.canvas.create_text(
            26.0, 167.0,
            anchor="nw",
            text="Panel del\nAdministrador",
            fill="#FFFFFF",
            font=("Inter", 48 * -1)
        )
        
        # Icono de login
        self.canvas.create_image(599.0, 75.0, image=self.login_icon)
    
    def _create_ui_elements(self):
        """Crea los elementos de la interfaz de usuario"""
        # Campo de nombre de usuario
        self.canvas.create_image(599.5, 195.5, image=self.entry_bg_1)
        self.username_entry = Entry(
            self.parent,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 12)
        )
        self.username_entry.place(x=466.0, y=172.0, width=267.0, height=45.0)
        
        # Campo de contraseña
        self.canvas.create_image(575.0, 278.5, image=self.entry_bg_2)
        self.password_entry = Entry(
            self.parent,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            show="●",
            font=("Inter", 12)
        )
        self.password_entry.place(x=466.0, y=255.0, width=218.0, height=45.0)
        
        # Botón de login
        self.login_button = Button(
            self.parent,
            image=self.login_button_img,
            borderwidth=0,
            highlightthickness=0,
            command=self._attempt_login,
            relief="flat"
        )
        self.login_button.place(x=521.0, y=338.0, width=158.0, height=56.0)
        
        # Botón de cerrar
        self.close_button = Button(
            self.parent,
            text="X",
            font=("Inter", 12),
            bg="#BC9585",
            fg="#FFFFFF",
            command=self.close_and_open_index
        )
        self.close_button.place(x=760, y=10, width=30, height=30)
        
        # Textos descriptivos
        self.canvas.create_text(
            451.0, 149.0,
            anchor="nw",
            text="Nombre de usuario:",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )
        
        self.canvas.create_text(
            451.0, 232.0,
            anchor="nw",
            text="Contraseña:",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )
        
        # Icono para mostrar/ocultar contraseña
        self.password_icon_ref = self.canvas.create_image(723.0, 278.0, image=self.password_icon)
        self.password_visible = BooleanVar(value=False)
    
    def _setup_event_handlers(self):
        """Configura los manejadores de eventos"""
        self.canvas.tag_bind(self.password_icon_ref, "<Button-1>", lambda e: self._toggle_password_visibility())
    
    def _toggle_password_visibility(self):
        """Alterna entre mostrar y ocultar la contraseña"""
        if self.password_visible.get():
            self.password_entry.config(show="●")
        else:
            self.password_entry.config(show="")
        self.password_visible.set(not self.password_visible.get())
    
    def _attempt_login(self):
        """Intenta iniciar sesión con las credenciales proporcionadas"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.open_panelAdmin_view(username, password)
    
    def close_and_open_index(self):
        """Cierra la vista actual y abre la vista de índice"""
        if self.controller:
            self.controller.open_index_view()
    
    def run(self):
        self.parent.mainloop()