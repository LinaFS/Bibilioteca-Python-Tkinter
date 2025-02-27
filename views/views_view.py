from tkinter import Tk, Canvas, Frame, Label, Button, Scrollbar
from PIL import Image, ImageTk
from pathlib import Path

class ViewsView:
    def __init__(self, controller):
        self.controller = controller
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"../guiBuild/views/assets/frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        self.window = Tk()

        self.window.geometry("800x500")
        self.window.configure(bg="#FFFFFF")

        def set_image(path):
            image_path = relative_to_assets(path)
            image = image = Image.open(image_path)
            image = image.resize((40, 40)) 
            setImage = ImageTk.PhotoImage(image)
            return setImage

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            0.0,
            0.0,
            800.0,
            70.0,
            fill="#342217",
            outline=""
        )

        # Texto sobre el rectángulo

        canvas.create_text(
            315.0,
            13.0,
            anchor="nw",
            text="Más leídos",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 30 * -1)
        )

        canvas.create_rectangle(
            0.0,
            70.0,
            155.0,
            500.0,
            fill="#BC9585",
            outline=""
        )

        self.image_home = set_image("home.png")
        self.img_home = canvas.create_image(
            32.0, 
            106.0, 
            image=self.image_home
        )

        self.image_home_black = set_image("home_black.png")

        canvas.tag_bind(self.img_home, "<Button-1>", lambda e: self.controller.open_index_view(self.window))


        self.home = canvas.create_text(
            65.0,
            100.0,
            anchor="nw",
            text="Inicio",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )

        canvas.tag_bind(self.home, "<Button-1>", lambda e: self.controller.open_index_view(self.window))

        self.image_content = set_image("content.png")
        self.img_content = canvas.create_image(
            32.0,
            170.0,
            image=self.image_content
        )

        self.image_content_black = set_image("content_black.png")

        canvas.tag_bind(self.img_content, "<Button-1>", lambda e: self.controller.open_search_view(self.window, None))

        self.content = canvas.create_text(
            65.0,
            160.0,
            anchor="nw",
            text="Contenido",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )

        canvas.tag_bind(self.content, "<Button-1>", lambda e: self.controller.open_search_view(self.window, None))

        self.image_news = set_image("news.png")
        self.img_news = canvas.create_image(
            32.0,
            230.0,
            image=self.image_news
        )

        self.image_news_black = set_image("news_black.png")

        self.news = canvas.create_text(
            65.0,
            222.0,
            anchor="nw",
            text="Novedades",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )

        canvas.tag_bind(self.img_news, "<Button-1>", lambda e: self.controller.open_news_view(self.window))
        canvas.tag_bind(self.news, "<Button-1>", lambda e: self.controller.open_news_view(self.window))

        def apply_hover_effect_combined(canvas, image_id, text_id, image_hover, image_default, text_hover="black", text_default="white"):
            """Cambia la imagen y el color del texto simultáneamente al pasar el mouse."""
            def on_enter(event):
                canvas.itemconfig(image_id, image=image_hover)
                canvas.itemconfig(text_id, fill=text_hover)

            def on_leave(event):
                canvas.itemconfig(image_id, image=image_default)
                canvas.itemconfig(text_id, fill=text_default)

            canvas.tag_bind(image_id, "<Enter>", on_enter)
            canvas.tag_bind(text_id, "<Enter>", on_enter)
            canvas.tag_bind(image_id, "<Leave>", on_leave)
            canvas.tag_bind(text_id, "<Leave>", on_leave)



        apply_hover_effect_combined(canvas, self.img_home, self.home, self.image_home_black, self.image_home)
        apply_hover_effect_combined(canvas, self.img_content, self.content, self.image_content_black, self.image_content)
        apply_hover_effect_combined(canvas, self.img_news, self.news, self.image_news_black, self.image_news)


        # Results area

        results_frame = Frame(
            self.window, 
            bg="#FFFFFF"
        )

        results_frame.place(
            x=156, 
            y=70, 
            width=644, 
            height=430
        )

        self.results_canvas = Canvas(results_frame, bg="white")
        self.scrollbar = Scrollbar(results_frame, orient="vertical", command=self.results_canvas.yview)
        self.scrollable_frame = Frame(self.results_canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(
                scrollregion=self.results_canvas.bbox("all")
            )
        )

        self.results_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.results_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.results_canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        # Empaquetar elementos
        self.results_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        query = self.controller.mostrar_leidos()
            
        if query:
            self.generar_resultados(query)
        else:
            self.generar_resultados(None)
        
    def generar_resultados(self, articulos):
        # Limpiar los widgets existentes
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Ajustar el ancho del frame para evitar desbordes
        self.scrollable_frame.update_idletasks()

        if articulos:
            for articulo in articulos:
                resultado_item = Frame(self.scrollable_frame, bg="white", bd=1, relief="solid")
                resultado_item.pack(fill="x", padx=20, pady=10)  # Más margen a la derecha (20px)

                # Título
                titulo_label = Label(
                    resultado_item, 
                    text=articulo.titulo, 
                    font=("Arial", 14, "bold"), 
                    bg="white", 
                    anchor="w", 
                    wraplength=540  
                )
                titulo_label.pack(fill="x", padx=10, pady=(0, 10))  # Más margen a la derecha

                # Autor
                autor_label = Label(
                    resultado_item, 
                    text=articulo.autor, 
                    font=("Arial", 12), 
                    bg="white", 
                    anchor="w",
                    wraplength=540
                )
                autor_label.pack(fill="x", padx=10, pady=(0, 5))  # Más margen a la derecha

                # Descripción
                descripcion_label = Label(
                    resultado_item,
                    text=articulo.resumen,
                    font=("Arial", 10),
                    bg="white",
                    anchor="w",
                    wraplength=540,
                    justify="left"
                )
                descripcion_label.pack(fill="x", padx=10, pady=(0, 10))  # Más margen a la derecha

                # Pie con fecha y botón
                footer_frame = Frame(resultado_item, bg="white")
                footer_frame.pack(fill="x", padx=10, pady=(0, 10))  # Más margen a la derecha

                fecha_label = Label(
                    footer_frame, 
                    text=f"Fecha publicación: {articulo.fecha}", 
                    font=("Arial", 10), 
                    bg="white", 
                    anchor="w"
                )
                fecha_label.pack(side="left")

                flecha_button = Button(
                    footer_frame, 
                    text="→", 
                    font=("Arial", 14, "bold"), 
                    bg="white", 
                    bd=0, 
                    cursor="hand2"
                )
                flecha_button.pack(side="right")
        else:
            print("No hay")

    def _on_mouse_wheel(self, event):
        delta = -1 * (event.delta // 120)  # Normaliza el delta (Windows y Linux)
        if self.window.tk.call("tk", "windowingsystem") == "aqua":  # macOS
            delta = event.delta
        self.results_canvas.yview_scroll(delta, "units")
    
    def run(self):
        """Inicia el loop principal de Tkinter."""
        self.window.mainloop()


