from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, BooleanVar

class LoginView:
    def __init__(self, controller):
        self.controller = controller

        # Ruta para los assets
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"../guiBuild/login/assets/frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        self.window = Tk()

        self.window.geometry("800x500")
        self.window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            self.window,
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
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
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
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            show= "●"
        )
        self.entry_2.place(
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
            command=lambda: self.controller.open_panelAdmin_view(
                self.window,
                self.entry_1.get(),
                self.entry_2.get(),
            ),
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
        
        self.password_visible = BooleanVar(value=False)

        # Función para alternar entre mostrar/ocultar la contraseña
        def toggle_password():
            if self.password_visible.get():
                self.entry_2.config(show="●")  # Ocultar contraseña
                image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
            else:
                self.entry_2.config(show="")  # Mostrar contraseña
                image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
            self.password_visible.set(not self.password_visible.get())  # Cambiar el estado

        # Evento para cambiar entre mostrar/ocultar
        canvas.tag_bind(image_3, "<Button-1>", lambda e: toggle_password())
        
        close_button = Button(
            self.window,
            text="X",
            font=("Inter", 12),
            bg="#BC9585",
            fg="#FFFFFF",
            command=self.close_and_open_index
        )
        close_button.place(x=760, y=10, width=30, height=30)
        

        self.window.resizable(False, False)
        self.window.mainloop()

        # Evitar que la ventana cambie de tamaño
        self.window.resizable(False, False)
            
        
    def close_and_open_index(self):
        if self.controller:
            print("Se encontró controlador (login)")
            self.controller.open_index_view(self.window)
        else:
            print("No hay controlador (login)")

    # Método para correr la aplicación
    def run(self):
        self.window.mainloop()
