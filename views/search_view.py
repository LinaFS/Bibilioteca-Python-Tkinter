from tkinter import Tk, Frame, Label, Entry, Button, Radiobutton, StringVar, Scrollbar, Canvas
from pathlib import Path


class SearchView:
    def __init__(self, controller):
        self.controller = controller
        OUTPUT_PATH = Path(__file__).parent

        data=self.controller.get_data()
        
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
        
        def buscar_articulos(texto, filter):
            query = self.controller.buscar(texto,filter)
            if query:
                    self.generar_resultados(query)
            else:
                self.generar_resultados(None)

        self.lupa_boton = Button(
            self.busqueda_frame,
            text="🔍",
            bg=self.fondo_rojo,
            fg=self.texto_negro,
            font=("Arial", 12),
            command=lambda: buscar_articulos(self.entrada_busqueda.get(), self.filtro_var.get()),
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
        self.filtros_label.pack(pady=(10,0), padx=(10,0))

        # Radios para filtros
        self.opciones = ["Articulo", "Libro", "Revista"]
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
        self.resultados_frame.pack(side="left", expand=True, fill="both", padx=20, pady=20)

        # Scrollbar y Canvas para resultados
        self.canvas = Canvas(self.resultados_frame, bg=self.fondo_resultados)
        self.scrollbar = Scrollbar(
            self.resultados_frame, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = Frame(self.canvas, bg=self.fondo_resultados)

        # Configuración del scrollbar
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Crear la ventana dentro del canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configuración del scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Agregar widgets a la ventana del canvas
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="left", fill="y")
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        
        self.generar_resultados(data)
    
    def generar_resultados(self, articulos):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        resultado_item = Frame(self.scrollable_frame, bg="white", bd=1, relief="solid")
        resultado_item.pack(fill="x", padx=60, pady=10)
            
        if articulos:
            for articulo in articulos:
                
                # Título
                titulo_label = Label(
                    resultado_item,
                    text=articulo.titulo,
                    font=("Arial", 14, "bold"),
                    bg="white",
                    anchor="w",
                    wraplength=500,
                    justify= "left"
                )
                titulo_label.pack(fill="x", padx=10, pady=(10, 0))

                # Autor
                autor_label = Label(
                    resultado_item,
                    text=articulo.autor,
                    font=("Arial", 12),
                    bg="white",
                    anchor="w",
                    wraplength=500,
                    justify= "left"
                )
                autor_label.pack(fill="x", padx=10, pady=(0, 5))

                # Descripción
                descripcion_label = Label(
                    resultado_item,
                    text=articulo.resumen,
                    font=("Arial", 10),
                    bg="white",
                    anchor="w",
                    wraplength=500,
                    justify="center",
                )
                descripcion_label.pack(fill="x", padx=10, pady=(0, 10))

                # Fecha y flecha (lado derecho)
                footer_frame = Frame(resultado_item, bg="white")
                footer_frame.pack(fill="x", padx=10, pady=(0, 10))

                fecha_label = Label(
                    footer_frame,
                    text=articulo.fecha,
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
            
        else:
            self.sin_coincidencias = Label(
                self.scrollable_frame,
                resultado_item,
                text= "No se encontraron resultados.",
                font= ("Arial",20, "bold"),
                fg="gray",
                bg= self.fondo_resultados,
                anchor="center"
            )

    def regresar_index(self):
        if self.controller:
            print("Regresando al índice...")
            self.controller.open_index_view(self.window)
        else:
            print("No hay índice...")
    def _on_mouse_wheel(self, event):
    # Ajuste de desplazamiento (positivos son hacia abajo, negativos hacia arriba)
        delta = -1 * (event.delta // 120)  # Normaliza el delta (Windows y Linux)
        if self.window.tk.call("tk", "windowingsystem") == "aqua":  # macOS
            delta = event.delta
        self.canvas.yview_scroll(delta, "units")


    def run(self):
        self.window.mainloop()
