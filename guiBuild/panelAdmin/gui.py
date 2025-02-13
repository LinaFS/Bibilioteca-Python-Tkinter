from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_translucent_rectangle(canvas, x1, y1, x2, y2, color, alpha):
    """
    Crea un rectángulo translúcido usando Pillow y lo dibuja en un Canvas de Tkinter.

    Args:
        canvas (Canvas): El lienzo de Tkinter donde se dibuja.
        x1, y1, x2, y2 (int): Coordenadas del rectángulo.
        color (str): Color hexadecimal del rectángulo (sin opacidad).
        alpha (float): Opacidad del rectángulo (0.0 a 1.0).
    """
    width, height = int(x2 - x1), int(y2 - y1)

    # Crear una imagen semitransparente con Pillow
    img = Image.new("RGBA", (width, height), color + f"{int(255 * alpha):02x}")
    img_tk = ImageTk.PhotoImage(img)

    # Dibujar la imagen en el canvas
    canvas_image = canvas.create_image(x1, y1, anchor="nw", image=img_tk)
    canvas.image_refs.append(img_tk)  # Evitar que Python limpie la referencia a la imagen


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
canvas.image_refs = []  # Lista para mantener referencias de imágenes

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(400.0, 250.0, image=image_image_1)

canvas.create_text(
    112.0,
    119.0,
    anchor="nw",
    text="Panel del administrador",
    fill="#000000",
    font=("IstokWeb Bold", 55 * -1)
)

# Crear un rectángulo translúcido
create_translucent_rectangle(canvas, 152, 211, 647, 339, "#342217", 0.6)

# Otros elementos del canvas
canvas.create_text(
    305.0,
    292.0,
    anchor="nw",
    text="Modificar",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(335.0, 263.0, image=image_image_2)

canvas.create_text(
    200.0,
    292.0,
    anchor="nw",
    text="Añadir",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(221.0, 262.0, image=image_image_3)

canvas.create_text(
    551.0,
    293.0,
    anchor="nw",
    text="Eliminar",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(577.0, 263.0, image=image_image_4)

canvas.create_text(
    425.0,
    292.0,
    anchor="nw",
    text="Consultar",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(457.0, 262.0, image=image_image_5)

window.resizable(False, False)
window.mainloop()
