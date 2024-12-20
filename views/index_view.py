from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage
from PIL import Image, ImageTk, ImageDraw


class IndexView:
    def __init__(self, controller):
        self.controller = controller
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"../guiBuild/index/assets/frame0")
        
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        print("Ruta:", relative_to_assets("image_1.png"))

        window = Tk()

        window.geometry("800x500")
        window.configure(bg="#C4C4C4")

        canvas = Canvas(
            window,
            bg="#C4C4C4",
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
            500.0,
            fill="#D9D9D9",
            outline=""
        )

        # Colocar la imagen principal
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            400.0,
            250.0,
            image=image_image_1
        )

        # Luego el rectángulo semi-transparente con Pillow
        width, height = 800, 500
        rect_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(rect_image)
        draw.rectangle([91, 137, 709, 333], fill=(30, 30, 30, 102))  # Color #1E1E1E con 60% de transparencia (102 alfa)

        # Convertir la imagen a un formato compatible con Tkinter
        tk_image = ImageTk.PhotoImage(rect_image)
        canvas.create_image(0, 0, anchor="nw", image=tk_image)

        # Añadir los demás rectángulos
        canvas.create_rectangle(
            469.0,
            137.0,
            702.0,
            328.0,
            fill="#1B1B1B",
            outline=""
        )

        canvas.create_rectangle(
            84.0,
            296.0,
            715.0,
            381.0,
            fill="#342217",
            outline=""
        )

        # Colocar el entry para la búsqueda
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            274.5,
            235.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#393939",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=144.0,
            y=212.0,
            width=261.0,
            height=45.0
        )

        # Añadir la lupa al lado derecho del Entry
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            440.0,  # Posición x ajustada para estar junto al Entry
            235.0,  # Centrado en la misma altura que el Entry
            image=image_image_2
        )

        # Añadir los textos
        canvas.create_text(
            135.0,
            185.0,
            anchor="nw",
            text="Buscar artículo, libro, tesis...",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )

        canvas.create_text(
            539.0,
            165.0,
            anchor="nw",
            text="Aplicar filtros",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )

        canvas.create_text(
            204.0,
            338.0,
            anchor="nw",
            text="Más leídos",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )

        canvas.create_text(
            502.0,
            333.0,
            anchor="nw",
            text="Novedades",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )

        # Añadir el banner superior con fondo y texto "Iniciar Sesión"
        canvas.create_rectangle(
            0.0,
            0.0,
            800.0,
            67.0,
            fill="#BC9585",
            outline=""
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            57.0,
            33.0,
            image=image_image_3
        )

        canvas.create_text(
            644.0,
            23.0,
            anchor="nw",
            text="Iniciar Sesión",
            fill="#FFFFFF",
            font=("IstokWeb Regular", 15 * -1)
        )

        # Añadir la lupa (imagen "image_2.png") sobre el panel
        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            764.0,
            31.0,
            image=image_image_4
        )

        window.resizable(False, False)
        window.mainloop()

    def run(self):
        self.window.mainloop()
