from tkinter import Canvas, Frame, Label, Button, Scrollbar
from PIL import Image, ImageTk
from pathlib import Path
import tkinter as tk

class ViewsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        
        # Configuración inicial
        self._setup_paths()
        self._configure_window()
        self._load_images()
        self._create_main_canvas()
        self._create_sidebar()
        self._create_results_area()
        self._display_results()
    
    def _setup_paths(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"../guiBuild/views/assets/frame0")
    
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def _configure_window(self):
        self.configure(bg="#FFFFFF")
    
    def _load_images(self):
        """Carga y prepara todas las imágenes necesarias"""
        def load_and_resize_image(path, size=(40, 40)):
            image = Image.open(self.relative_to_assets(path))
            image = image.resize(size)
            return ImageTk.PhotoImage(image)
        
        # Imágenes normales
        self.image_home = load_and_resize_image("home.png")
        self.image_content = load_and_resize_image("content.png")
        self.image_news = load_and_resize_image("news.png")
        
        # Imágenes para hover
        self.image_home_black = load_and_resize_image("home_black.png")
        self.image_content_black = load_and_resize_image("content_black.png")
        self.image_news_black = load_and_resize_image("news_black.png")
    
    def _create_main_canvas(self):
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
        
        # Crear rectángulo superior
        self.canvas.create_rectangle(0.0, 0.0, 800.0, 70.0, fill="#342217", outline="")
        self.canvas.create_text(
            315.0, 13.0,
            anchor="nw",
            text="Más leídos",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 30 * -1)
        )
    
    def _create_sidebar(self):
        """Crea la barra lateral con los elementos de navegación"""
        # Fondo de la barra lateral
        self.canvas.create_rectangle(0.0, 70.0, 155.0, 500.0, fill="#BC9585", outline="")
        
        # Elementos de navegación
        self._create_nav_item("Inicio", 106.0, self.image_home, self.image_home_black, 
                             lambda: self.controller.open_index_view())
        self._create_nav_item("Contenido", 170.0, self.image_content, self.image_content_black, 
                             lambda: self.controller.open_search_view(None))
        self._create_nav_item("Novedades", 230.0, self.image_news, self.image_news_black, 
                             lambda: self.controller.open_news_view())
    
    def _create_nav_item(self, text, y_pos, image, hover_image, command):
        """Crea un elemento de navegación en la barra lateral"""
        # Icono
        img_id = self.canvas.create_image(32.0, y_pos, image=image)
        
        # Texto
        text_id = self.canvas.create_text(
            65.0, y_pos - 6.0,
            anchor="nw",
            text=text,
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )
        
        # Eventos de clic
        self.canvas.tag_bind(img_id, "<Button-1>", lambda e: command())
        self.canvas.tag_bind(text_id, "<Button-1>", lambda e: command())
        
        # Efectos hover
        self._setup_hover_effects(img_id, text_id, image, hover_image)
    
    def _setup_hover_effects(self, image_id, text_id, normal_image, hover_image):
        """Configura los efectos hover para un elemento de navegación"""
        def on_enter(event):
            self.canvas.itemconfig(image_id, image=hover_image)
            self.canvas.itemconfig(text_id, fill="black")

        def on_leave(event):
            self.canvas.itemconfig(image_id, image=normal_image)
            self.canvas.itemconfig(text_id, fill="#FFFFFF")

        self.canvas.tag_bind(image_id, "<Enter>", on_enter)
        self.canvas.tag_bind(text_id, "<Enter>", on_enter)
        self.canvas.tag_bind(image_id, "<Leave>", on_leave)
        self.canvas.tag_bind(text_id, "<Leave>", on_leave)
    
    def _create_results_area(self):
        """Crea el área desplazable para mostrar los resultados"""
        self.results_frame = Frame(self.parent, bg="#FFFFFF")
        self.results_frame.place(x=156, y=70, width=644, height=430)
        
        # Canvas y scrollbar
        self.results_canvas = Canvas(self.results_frame, bg="white")
        self.scrollbar = Scrollbar(self.results_frame, orient="vertical", command=self.results_canvas.yview)
        
        # Frame desplazable
        self.scrollable_frame = Frame(self.results_canvas, bg="white")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))
        )
        
        # Configuración del canvas
        self.results_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.results_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.results_canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        
        # Empaquetado
        self.results_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
    
    def _display_results(self):
        """Muestra los resultados en el área designada"""
        query = self.controller.mostrar_leidos()
        self.generar_resultados(query if query else None)
    
    def generar_resultados(self, articulos):
        """Genera los widgets para mostrar los artículos"""
        # Limpiar resultados anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not articulos:
            no_results = Label(
                self.scrollable_frame,
                text="No se encontraron artículos",
                font=("Arial", 14),
                bg="white"
            )
            no_results.pack(pady=50)
            return
        
        for articulo in articulos:
            self._create_article_widget(articulo)
    
    def _create_article_widget(self, articulo):
        """Crea un widget para mostrar un artículo individual"""
        # Frame principal del artículo
        item_frame = Frame(self.scrollable_frame, bg="white", bd=1, relief="solid")
        item_frame.pack(fill="x", padx=20, pady=10)
        
        # Título
        Label(
            item_frame, 
            text=articulo.titulo, 
            font=("Arial", 14, "bold"), 
            bg="white", 
            anchor="w", 
            wraplength=540
        ).pack(fill="x", padx=10, pady=(0, 10))
        
        # Autor
        Label(
            item_frame, 
            text=articulo.autor, 
            font=("Arial", 12), 
            bg="white", 
            anchor="w",
            wraplength=540
        ).pack(fill="x", padx=10, pady=(0, 5))
        
        # Descripción
        Label(
            item_frame,
            text=articulo.resumen,
            font=("Arial", 10),
            bg="white",
            anchor="w",
            wraplength=540,
            justify="left"
        ).pack(fill="x", padx=10, pady=(0, 10))
        
        # Pie de artículo (fecha y botón)
        footer = Frame(item_frame, bg="white")
        footer.pack(fill="x", padx=10, pady=(0, 10))
        
        Label(
            footer, 
            text=f"Fecha publicación: {articulo.fecha}", 
            font=("Arial", 10), 
            bg="white", 
            anchor="w"
        ).pack(side="left")
        
        Button(
            footer, 
            text="→", 
            font=("Arial", 14, "bold"), 
            bg="white", 
            bd=0, 
            cursor="hand2"
        ).pack(side="right")
    
    def _on_mouse_wheel(self, event):
        """Maneja el scroll con la rueda del mouse"""
        delta = -1 * (event.delta // 120)  # Normaliza para Windows/Linux
        if self.parent.tk.call("tk", "windowingsystem") == "aqua":  # macOS
            delta = event.delta
        self.results_canvas.yview_scroll(delta, "units")
    
    def run(self):
        self.parent.mainloop()