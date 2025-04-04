from tkinter import Tk, Canvas, Frame, Label, Button, Scrollbar
from PIL import Image, ImageTk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def set_image(path):
    image_path = relative_to_assets(path)
    image = image = Image.open(image_path)
    image = image.resize((40, 40)) 
    setImage = ImageTk.PhotoImage(image)
    return setImage

def _on_mouse_wheel(event):
    delta = -1 * (event.delta // 120)  # Normaliza el delta (Windows y Linux)
    if window.tk.call("tk", "windowingsystem") == "aqua":  # macOS
        delta = event.delta
    results_canvas.yview_scroll(delta, "units")

window = Tk()

window.geometry("800x500")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
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

image_home = set_image("home.png")
img_home = canvas.create_image(
    32.0, 
    106.0, 
    image=image_home
)

home = canvas.create_text(
    65.0,
    100.0,
    anchor="nw",
    text="Inicio",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

image_content = set_image("content.png")
img_content = canvas.create_image(
    32.0,
    170.0,
    image=image_content
)

content = canvas.create_text(
    65.0,
    160.0,
    anchor="nw",
    text="Contenido",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

image_views = set_image("news.png")
img_views = canvas.create_image(
    32.0,
    230.0,
    image=image_views
)

news = canvas.create_text(
    65.0,
    222.0,
    anchor="nw",
    text="Novedades",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

# Results area

results_frame = Frame(
    window, 
    bg="#FFFFFF"
)

results_frame.place(
    x=156, 
    y=70, 
    width=644, 
    height=430
)

results_canvas = Canvas(results_frame, bg="white")
scrollbar = Scrollbar(results_frame, orient="vertical", command=results_canvas.yview)
scrollable_frame = Frame(results_canvas, bg="white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: results_canvas.configure(
        scrollregion=results_canvas.bbox("all")
    )
)

results_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
results_canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# Empaquetar elementos
results_canvas.pack(side="left", fill="both", expand=True)
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


window.update_idletasks()

window.resizable(False, False)
window.mainloop()
