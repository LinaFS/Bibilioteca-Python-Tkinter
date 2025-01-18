from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

class panelAdminView:
    def __init__(self, controller):
        self.controller = controller
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"../guiBuild/panelAdmin/assets/frame0")
        
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        def create_translucent_rectangle(canvas, x1, y1, x2, y2, color, alpha):
            width, height = int(x2 - x1), int(y2 - y1)
            # Crear una imagen semitransparente con Pillow
            img = Image.new("RGBA", (width, height), color + f"{int(255 * alpha):02x}")
            img_tk = ImageTk.PhotoImage(img)
            # Dibujar la imagen en el canvas
            canvas_image = canvas.create_image(x1, y1, anchor="nw", image=img_tk)
            canvas.image_refs.append(img_tk)
        
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.configure(bg="#C4C4C4")
        
        canvas = Canvas(
            self.window,
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
        
        self.closeSession = canvas.create_text(
            663.0,
            27.0,
            anchor="nw",
            text="Cerrar Sesión",
            fill= "#000000",
            font=("IstokWeb Bold", 15 * -1)
        )

        def on_hover(event):
            # Cambiar color y subrayar al pasar el mouse
            canvas.itemconfig(self.closeSession, fill="white", font=("IstokWeb Bold", 15 * -1, "underline"))

        def on_leave(event):
            # Restaurar el estilo original cuando el mouse salga
            canvas.itemconfig(self.closeSession, fill="black", font=("IstokWeb Bold", 15 * -1))

        if self.controller:
            print("Se encontró controlador (admin)")
            canvas.tag_bind(self.closeSession, "<Button-1>", lambda event: self.controller.close_session_view(self.window))
            canvas.tag_bind(self.closeSession, "<Enter>", on_hover)  # Cuando el mouse entra
            canvas.tag_bind(self.closeSession, "<Leave>", on_leave)  # Cuando el mouse sale
        else:
            print("No hay controlador (admin)")


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

        self.window.resizable(False, False)
        self.window.mainloop()
        
    def run(self):
        self.window.mainloop()

    
