from tkinter import Tk, Canvas, Frame, Label, Button, Scrollbar
from PIL import Image, ImageTk
from pathlib import Path

class NewsView:
    def __init__(self, controller):
        self.controller = controller
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"../guiBuild/news/assets/frame0")

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
            text="Novedades",
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

        self.home = canvas.create_text(
            65.0,
            100.0,
            anchor="nw",
            text="Inicio",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )

        self.image_content = set_image("content.png")
        self.img_content = canvas.create_image(
            32.0,
            170.0,
            image=self.image_content
        )

        self.content = canvas.create_text(
            65.0,
            160.0,
            anchor="nw",
            text="Contenido",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )

        self.image_views = set_image("views.png")
        self.img_views = canvas.create_image(
            32.0,
            230.0,
            image=self.image_views
        )

        self.views = canvas.create_text(
            65.0,
            222.0,
            anchor="nw",
            text="Más leído",
            fill="#FFFFFF",
            font=("Inter", 15 * -1)
        )

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
        scrollbar = Scrollbar(results_frame, orient="vertical", command=self.results_canvas.yview)
        scrollable_frame = Frame(self.results_canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(
                scrollregion=self.results_canvas.bbox("all")
            )
        )

        self.results_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        self.results_canvas.configure(yscrollcommand=scrollbar.set)
        self.results_canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        # Empaquetar elementos
        self.results_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Agregar artículos dentro del área desplazable
        for i in range(10):  # Agregar 10 artículos de ejemplo
            resultado_item = Frame(scrollable_frame, bg="white", bd=1, relief="solid")
            resultado_item.pack(fill="x", padx=20, pady=10)

            # Título
            titulo_label = Label(
                resultado_item, text=f"Artículo {i+1}", font=("Arial", 14, "bold"), bg="white", anchor="w"
            )
            titulo_label.pack(fill="x", padx=10, pady=(10, 0))

            # Autor
            autor_label = Label(resultado_item, text="Autor desconocido", font=("Arial", 12), bg="white", anchor="w")
            autor_label.pack(fill="x", padx=10, pady=(0, 5))

            # Descripción
            descripcion_label = Label(
                resultado_item,
                text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                font=("Arial", 10),
                bg="white",
                anchor="w",
                wraplength=400,
                justify="left",
            )
            descripcion_label.pack(fill="x", padx=10, pady=(0, 10))

            # Pie de artículo con fecha y botón
            footer_frame = Frame(resultado_item, bg="white")
            footer_frame.pack(fill="x", padx=10, pady=(0, 10))

            fecha_label = Label(footer_frame, text="Fecha publicación: Hoy", font=("Arial", 10), bg="white", anchor="w")
            fecha_label.pack(side="left")

            flecha_button = Button(footer_frame, text="→", font=("Arial", 14, "bold"), bg="white", bd=0, cursor="hand2")
            flecha_button.pack(side="right")
    
    def _on_mouse_wheel(self, event):
        delta = -1 * (event.delta // 120)  # Normaliza el delta (Windows y Linux)
        if self.window.tk.call("tk", "windowingsystem") == "aqua":  # macOS
            delta = event.delta
        self.results_canvas.yview_scroll(delta, "units")
    
    def run(self):
        """Inicia el loop principal de Tkinter."""
        self.window.mainloop()
