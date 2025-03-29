from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage, Radiobutton, StringVar
from PIL import Image, ImageTk, ImageDraw
from models.index_model import IndexModel
import tkinter as tk


class IndexView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent

        # Configuración inicial
        self._setup_paths()
        self._configure_window()
        self._create_widgets()
        self._setup_model()
        
    def _setup_paths(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"../guiBuild/index/assets/frame0")
        
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def _configure_window(self):
        self.configure(bg="#C4C4C4")
    
    def _create_widgets(self):
        self._create_canvas()
        self._create_background()
        self._create_transparent_rect()
        self._create_rectangles()
        self._create_search_entry()
        self._create_text_elements()
        self._create_radio_buttons()
        self._create_top_banner()
    
    def _create_canvas(self):
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
        self.canvas.create_rectangle(0.0, 0.0, 800.0, 500.0, fill="#D9D9D9", outline="")
    
    def _create_background(self):
        self.background_image = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(400, 250, image=self.background_image)
    
    def _create_transparent_rect(self):
        rect_image = Image.new("RGBA", (800, 500), (0, 0, 0, 0))
        draw = ImageDraw.Draw(rect_image)
        draw.rectangle([91, 137, 709, 333], fill=(30, 30, 30, 102))
        self.transparent_rect_image = ImageTk.PhotoImage(rect_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.transparent_rect_image)
    
    def _create_rectangles(self):
        self.canvas.create_rectangle(469.0, 137.0, 702.0, 328.0, fill="#1B1B1B", outline="")
        self.canvas.create_rectangle(84.0, 296.0, 715.0, 381.0, fill="#342217", outline="")
    
    def _create_search_entry(self):
        self.entry_bg_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(274.5, 235.5, image=self.entry_bg_image)
        
        self.entry_1 = Entry(
            self.parent,
            bd=0,
            bg="#393939",
            fg="#FFFFFF",
            highlightthickness=0,
            insertbackground="white",
            font=("IstokWeb Regular", 12)
        )
        self.entry_1.place(x=144.0, y=212.0, width=261.0, height=45.0)
        
        self.lupa_image = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.lupa_icon = self.canvas.create_image(440.0, 235.0, image=self.lupa_image)
        self.canvas.tag_bind(self.lupa_icon, "<Button-1>", lambda e: self.search_item())
    
    def _create_text_elements(self):
        self.canvas.create_text(
            135.0, 185.0,
            anchor="nw",
            text="Buscar artículo, libro, revista...",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )

        self.canvas.create_text(
            539.0, 165.0,
            anchor="nw",
            text="Aplicar filtros",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )

        self.leidos_text = self.canvas.create_text(
            204.0, 338.0,
            anchor="nw",
            text="Más leídos",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )
        self.canvas.tag_bind(self.leidos_text, "<Button-1>", 
                           lambda e: self.controller.open_views_page())

        self.novedades_text = self.canvas.create_text(
            502.0, 338.0,
            anchor="nw",
            text="Novedades",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )
        self.canvas.tag_bind(self.novedades_text, "<Button-1>", 
                           lambda e: self.controller.open_news_page())
    
    def _create_radio_buttons(self):
        self.radio_var = StringVar(value="articulo")
        
        self.radio_buttons = []
        options = [
            ("Artículos", "articulo", 540, 200),
            ("Libros", "libro", 540, 225),
            ("Revistas", "revista", 540, 250)
        ]
        
        for text, value, x, y in options:
            rb = Radiobutton(
                self.parent,
                text=text,
                variable=self.radio_var,
                value=value,
                bg="#1B1B1B",
                fg="white",
                activebackground="#393939",
                activeforeground="white",
                font=("IstokWeb Regular", 12),
                selectcolor="#393939"
            )
            rb.place(x=x, y=y)
            self.radio_buttons.append(rb)
    
    def _create_top_banner(self):
        self.canvas.create_rectangle(0.0, 0.0, 800.0, 67.0, fill="#BC9585", outline="")
        
        self.logo_image = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.canvas.create_image(57.0, 33.0, image=self.logo_image)
        
        self.login_text = self.canvas.create_text(
            644.0, 23.0,
            anchor="nw",
            text="Iniciar Sesión",
            fill="black",
            font=("IstokWeb Regular", 15 * -1)
        )
        
        self.search_icon_image = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.canvas.create_image(764.0, 31.0, image=self.search_icon_image)
        
        self.canvas.tag_bind(self.login_text, "<Button-1>", self.on_login_click)
        self.canvas.tag_bind(self.login_text, "<Enter>", self._on_hover_login)
        self.canvas.tag_bind(self.login_text, "<Leave>", self._on_leave_login)
    
    def _setup_model(self):
        self.model = IndexModel()
    
    def _on_hover_login(self, event):
        self.canvas.itemconfig(self.login_text, fill="white", 
                             font=("IstokWeb Bold", 15 * -1, "underline"))

    def _on_leave_login(self, event):
        self.canvas.itemconfig(self.login_text, fill="black", 
                             font=("IstokWeb Bold", 15 * -1))
    
    def handle_radio_selection(self):
        return self.radio_var.get()
    
    def search_item(self):
        filter_type = self.handle_radio_selection()
        search_term = self.entry_1.get()
        query = self.model.search(search_term, filter_type)
        self.controller.realizar_busqueda(query if query else None)
    
    def on_login_click(self, event):
        if self.controller:
            self.controller.iniciar_sesion()
        else:
            print("Error: No hay controlador asignado")
    
    def run(self):
        self.parent.mainloop()