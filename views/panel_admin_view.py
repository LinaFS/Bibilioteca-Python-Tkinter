from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Tk
from PIL import Image, ImageTk
import tkinter as tk

class PanelAdminView(tk.Frame):
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
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"../guiBuild/panelAdmin/assets/frame0")
    
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def _configure_window(self):
        self.configure(bg="#C4C4C4")
    
    def _load_images(self):
        """Carga todas las imágenes necesarias"""
        self.background_image = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.add_icon = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.modify_icon = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.consult_icon = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.delete_icon = PhotoImage(file=self.relative_to_assets("image_4.png"))
    
    def _create_translucent_rectangle(self, x1, y1, x2, y2, color, alpha):
        """Crea un rectángulo semitransparente en el canvas"""
        width, height = int(x2 - x1), int(y2 - y1)
        img = Image.new("RGBA", (width, height), color + f"{int(255 * alpha):02x}")
        img_tk = ImageTk.PhotoImage(img)
        canvas_image = self.canvas.create_image(x1, y1, anchor="nw", image=img_tk)
        self.canvas.image_refs.append(img_tk)
        return canvas_image
    
    def _create_main_canvas(self):
        """Crea el canvas principal y los elementos base"""
        self.canvas = Canvas(
            self.parent,
            bg="#C4C4C4",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.image_refs = []  # Lista para mantener referencias de imágenes
        
        # Fondo
        self.canvas.create_image(400.0, 250.0, image=self.background_image)
        
        # Título principal
        self.canvas.create_text(
            112.0,
            119.0,
            anchor="nw",
            text="Panel del administrador",
            fill="#000000",
            font=("IstokWeb Bold", 55 * -1)
        )
    
    def _create_ui_elements(self):
        """Crea los elementos de la interfaz de usuario"""
        # Rectángulo translúcido
        self._create_translucent_rectangle(152, 211, 647, 339, "#342217", 0.6)
        
        # Botón de cerrar sesión
        self.close_session_text = self.canvas.create_text(
            663.0,
            27.0,
            anchor="nw",
            text="Cerrar Sesión",
            fill="#000000",
            font=("IstokWeb Bold", 15 * -1)
        )
        
        # Iconos y textos de opciones
        # Añadir
        self.canvas.create_image(221.0, 262.0, image=self.add_icon)
        self.canvas.create_text(
            200.0,
            292.0,
            anchor="nw",
            text="Añadir",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )
        
        # Modificar
        self.canvas.create_image(335.0, 263.0, image=self.modify_icon)
        self.canvas.create_text(
            305.0,
            292.0,
            anchor="nw",
            text="Modificar",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )
        
        # Consultar
        self.canvas.create_image(457.0, 262.0, image=self.consult_icon)
        self.canvas.create_text(
            425.0,
            292.0,
            anchor="nw",
            text="Consultar",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )
        
        # Eliminar
        self.canvas.create_image(577.0, 263.0, image=self.delete_icon)
        self.canvas.create_text(
            551.0,
            293.0,
            anchor="nw",
            text="Eliminar",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )
    
    def _setup_event_handlers(self):
        """Configura los manejadores de eventos"""
        # Eventos para el texto de cerrar sesión
        def on_hover(event):
            self.canvas.itemconfig(self.close_session_text, fill="white", font=("IstokWeb Bold", 15 * -1, "underline"))
        
        def on_leave(event):
            self.canvas.itemconfig(self.close_session_text, fill="black", font=("IstokWeb Bold", 15 * -1))
        
        if self.controller:
            self.canvas.tag_bind(self.close_session_text, "<Button-1>", lambda event: self.controller.close_session())
            self.canvas.tag_bind(self.close_session_text, "<Enter>", on_hover)
            self.canvas.tag_bind(self.close_session_text, "<Leave>", on_leave)
    
    def run(self):
        self.parent.mainloop()