
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\981011476\OneDrive\Documentos\Python\servicio\guiBuild\index\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x500")
window.configure(bg = "#C4C4C4")


canvas = Canvas(
    window,
    bg = "#C4C4C4",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    500.0,
    fill="#D9D9D9",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    250.0,
    image=image_image_1
)

canvas.create_rectangle(
    91.0,
    137.0,
    709.0,
    333.0,
    fill="#1E1E1E",
    outline="")

canvas.create_rectangle(
    469.0,
    137.0,
    702.0,
    328.0,
    fill="#1B1B1B",
    outline="")

canvas.create_rectangle(
    84.0,
    296.0,
    715.0,
    381.0,
    fill="#342217",
    outline="")

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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    442.0,
    235.0,
    image=image_image_2
)

canvas.create_text(
    533.0,
    199.0,
    anchor="nw",
    text="Artículo Libro Tesis",
    fill="#AFA1A1",
    font=("IstokWeb Regular", 15 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    67.0,
    fill="#BC9585",
    outline="")

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

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    764.0,
    31.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()