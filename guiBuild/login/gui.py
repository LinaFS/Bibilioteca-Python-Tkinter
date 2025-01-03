
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\981011476\OneDrive\Documentos\Python\servicio\guiBuild\login\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    250.0,
    image=image_image_1
)

canvas.create_rectangle(
    400.0,
    0.0,
    800.0,
    500.0,
    fill="#BC9585",
    outline="")

canvas.create_text(
    26.0,
    167.0,
    anchor="nw",
    text="Panel del\nAdministrador",
    fill="#FFFFFF",
    font=("Inter", 48 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    599.5,
    195.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=466.0,
    y=172.0,
    width=267.0,
    height=45.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    575.0,
    278.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=466.0,
    y=255.0,
    width=218.0,
    height=45.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    599.0,
    75.0,
    image=image_image_2
)

canvas.create_text(
    1194.0,
    322.0,
    anchor="nw",
    text="Inicio de sesión",
    fill="#FFFFFF",
    font=("IstokWeb Bold", 45 * -1)
)

canvas.create_text(
    451.0,
    149.0,
    anchor="nw",
    text="Nombre de usuario:",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=521.0,
    y=338.0,
    width=158.0,
    height=55.79148864746094
)

canvas.create_text(
    451.0,
    232.0,
    anchor="nw",
    text="Contraseña:",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    723.0,
    278.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
