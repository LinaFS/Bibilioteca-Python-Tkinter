from tkinter import Canvas, Tk


class gui:
    def __init__(self, search_term):
        self.search_term = search_term
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.configure(bg="#EAEAEA")

        canvas = Canvas(
            self.window,
            bg="#EAEAEA",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Título con el término de búsqueda
        canvas.create_text(
            100.0,
            50.0,
            anchor="nw",
            text=f"Resultados para: {self.search_term}",
            fill="#000000",
            font=("Arial", 20 * -1)
        )

        # Ejemplo de contenido dinámico
        canvas.create_text(
            100.0,
            100.0,
            anchor="nw",
            text="Aquí se mostrarían los resultados relacionados con tu búsqueda.",
            fill="#333333",
            font=("Arial", 15 * -1)
        )

        self.window.resizable(False, False)
        self.window.mainloop()
