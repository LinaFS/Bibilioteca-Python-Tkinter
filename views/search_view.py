from tkinter import Tk, Frame, Label, Entry, Button, Radiobutton, StringVar
from pathlib import Path


class SearchView:
    def __init__(self, controller):
        self.controller = controller
        OUTPUT_PATH = Path(__file__).parent

        self.window = Tk()
        self.window.geometry("800x500")  # Dimensiones de la ventana
        self.window.configure(bg="#FFFFFF")  # Fondo blanco
        self.window.title("Search View")  # Título de la ventana
        self.window.resizable(False, False)

        # Colores personalizados
        self.fondo_rojo = "#BC9585" 
        self.fondo_azul = "#1B1B1B"  # Color oscuro para el fondo
        self.fondo_marron = "#5a3d31" 
        self.fondo_texto = "#828282"
        self.fondo_resultados = "#f5f5f5"  # Color claro para resultados
        self.texto_blanco = "#ffffff"
        self.texto_negro = "#000000"

        # Barra superior
        self.barra_superior = Frame(self.window, bg=self.fondo_rojo, height=60)
        self.barra_superior.pack(side="top", fill="x")

        # Botón de regreso a índice (casita)
        self.boton_casita = Button(
            self.barra_superior,
            text="🏠",
            bg=self.fondo_rojo,
            fg=self.texto_negro,
            font=("nw", 16),
            bd=0,
            command=self.regresar_index,
        )
        self.boton_casita.pack(side="left", padx=10, pady=10)

        # Barra de búsqueda sin título
        self.busqueda_frame = Frame(self.barra_superior, bg=self.fondo_rojo)
        self.busqueda_frame.pack(side="right", padx=10)

        self.entrada_busqueda = Entry(
            self.busqueda_frame, font=("nw", 10), width=40
        )
        self.entrada_busqueda.pack(side="left", padx=10)

        self.lupa_boton = Button(
            self.busqueda_frame,
            text="🔍",
            bg=self.fondo_rojo,
            fg=self.texto_blanco,
            font=("Arial", 12),
            command=lambda: self.buscar(self.entrada_busqueda.get()),
        )
        self.lupa_boton.pack(side="left")

        # Área principal
        self.area_principal = Frame(self.window, bg=self.fondo_azul)
        self.area_principal.pack(expand=True, fill="both")

        # Filtros de búsqueda (lado izquierdo)
        self.filtros_frame = Frame(self.area_principal, bg=self.fondo_azul, width=200)
        self.filtros_frame.pack(side="left", fill="y")

        self.filtros_label = Label(
            self.filtros_frame,
            text="Filtros de búsqueda",
            bg=self.fondo_azul,
            fg=self.texto_blanco,
            font=("nw", 12, "bold"),
        )
        self.filtros_label.pack(pady=10)

        # Radios para filtros
        self.opciones = ["Artículos", "Libros", "Tesis"]
        self.filtro_var = StringVar(value=self.opciones[0])

        for opcion in self.opciones:
            Radiobutton(
                self.filtros_frame,
                text=opcion,
                variable=self.filtro_var,
                value=opcion,
                bg=self.fondo_azul,
                fg=self.texto_blanco,
                selectcolor=self.fondo_marron,
            ).pack(anchor="w", padx=10, pady=5)

        # Área de resultados (lado derecho)
        self.resultados_frame = Frame(self.area_principal, bg=self.fondo_resultados)
        self.resultados_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

        # Cuadro para resultados
        self.cuadro_resultados = Frame(self.resultados_frame, bg=self.fondo_resultados, bd=2, relief="flat")
        self.cuadro_resultados.pack(expand=True, fill="both", padx=10, pady=10)

        # Cada resultado (similar al diseño de la imagen)
        for i in range(3):  # Ejemplo de tres resultados
            resultado_item = Frame(self.cuadro_resultados, bg="white", bd=1, relief="solid")
            resultado_item.pack(fill="x", padx=10, pady=10)

            # Título
            titulo_label = Label(
                resultado_item,
                text="Título del artículo/libro/tesis",
                font=("Arial", 14, "bold"),
                bg="white",
                anchor="w",
            )
            titulo_label.pack(fill="x", padx=10, pady=(10, 0))

            # Autor
            autor_label = Label(
                resultado_item,
                text="Autor",
                font=("Arial", 12),
                bg="white",
                anchor="w",
            )
            autor_label.pack(fill="x", padx=10, pady=(0, 5))

            # Descripción
            descripcion_label = Label(
                resultado_item,
                text="Lorem ipsum dolor sit amet consectetur adipiscing elit, "
                     "pellentesque suscipit odio, et posuere vehicula tellus.",
                font=("Arial", 10),
                bg="white",
                anchor="w",
                wraplength=400,
                justify="left",
            )
            descripcion_label.pack(fill="x", padx=10, pady=(0, 10))

            # Fecha y flecha (lado derecho)
            footer_frame = Frame(resultado_item, bg="white")
            footer_frame.pack(fill="x", padx=10, pady=(0, 10))

            fecha_label = Label(
                footer_frame,
                text="Fecha publicación",
                font=("Arial", 10),
                bg="white",
                anchor="w",
            )
            fecha_label.pack(side="left")

            flecha_button = Button(
                footer_frame,
                text="→",
                font=("Arial", 14, "bold"),
                bg="white",
                bd=0,
                cursor="hand2",
            )
            flecha_button.pack(side="right")

        
        
        # Botones "Más leídos" y "Novedades" en la barra superior
        self.botones_superior_frame = Frame(self.barra_superior, bg=self.fondo_rojo)
        self.botones_superior_frame.pack(side="right", padx=10)

        self.boton_mas_leidos = Label(
            self.botones_superior_frame,
            text="Más leídos",
            bg=self.fondo_rojo,
            fg=self.texto_negro,
            font=("nw", 10, "underline"),
            cursor="hand2",
        )
        self.boton_mas_leidos.pack(side="left", padx=5)
        self.boton_mas_leidos.bind("<Button-1>", lambda e: self.mostrar_mas_leidos())

        self.boton_novedades = Label(
            self.botones_superior_frame,
            text="Novedades",
            bg=self.fondo_rojo,
            fg=self.texto_negro,
            font=("nw", 10, "underline"),
            cursor="hand2",
        )
        self.boton_novedades.pack(side="left", padx=5)
        self.boton_novedades.bind("<Button-1>", lambda e: self.mostrar_novedades())
        
    def regresar_index(self):
        if self.controller:
            print("Regresando al índice...")
            self.controller.open_index_view(self.window)
        else:
            print("No hay indice...")

    def buscar(self, texto):
        """Lógica para la búsqueda."""
        print(f"Buscando: {texto}")

    def mostrar_mas_leidos(self):
        """Lógica para mostrar los artículos más leídos."""
        print("Mostrando los artículos más leídos...")

    def mostrar_novedades(self):
        """Lógica para mostrar novedades."""
        print("Mostrando las novedades...")

    def run(self):
        self.window.mainloop()

