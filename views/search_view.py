from tkinter import Frame, Label, Entry, Button, Radiobutton, StringVar, Scrollbar, Canvas
from pathlib import Path
import tkinter as tk


class SearchView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        
        # Configuración inicial
        self._setup_colors()
        self._configure_grid()
        self._create_ui_structure()
        self._setup_results_area()
        self._display_initial_results()
    
    def _setup_colors(self):
        """Define los colores personalizados"""
        self.colors = {
            'red_bg': "#BC9585",
            'blue_bg': "#1B1B1B",
            'brown_bg': "#5a3d31",
            'text_bg': "#828282",
            'results_bg': "#f5f5f5",
            'white_text': "#ffffff",
            'black_text': "#000000",
            'white_bg': "#FFFFFF"
        }
    
    def _configure_grid(self):
        """Configura el sistema de grid principal"""
        self.grid(row=0, column=0, sticky="nsew")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.configure(bg=self.colors['white_bg'])
    
    def _create_ui_structure(self):
        """Crea la estructura principal de la interfaz"""
        self._create_top_bar()
        self._create_main_area()
    
    def _create_top_bar(self):
        """Crea la barra superior con el buscador"""
        # Frame principal
        self.top_bar = Frame(self, bg=self.colors['red_bg'], height=60)
        self.top_bar.grid(row=0, column=0, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
        
        # Configuración de columnas
        self.top_bar.grid_columnconfigure(0, weight=1)
        self.top_bar.grid_columnconfigure(1, weight=0)
        
        # Botón de inicio
        self.home_button = Button(
            self.top_bar,
            text="🏠",
            bg=self.colors['red_bg'],
            fg=self.colors['black_text'],
            font=("nw", 16),
            bd=0,
            command=self._return_to_index,
        )
        self.home_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Frame de búsqueda
        self.search_frame = Frame(self.top_bar, bg=self.colors['red_bg'])
        self.search_frame.grid(row=0, column=1, padx=10, sticky="e")
        self.search_frame.grid_columnconfigure(0, weight=1)
        
        # Campo de búsqueda
        self.search_entry = Entry(
            self.search_frame, 
            font=("nw", 10), 
            width=40
        )
        self.search_entry.grid(row=0, column=0, padx=10)
        
        # Botón de búsqueda
        self.search_button = Button(
            self.search_frame,
            text="🔍",
            bg=self.colors['red_bg'],
            fg=self.colors['black_text'],
            font=("Arial", 12),
            command=self._perform_search,
        )
        self.search_button.grid(row=0, column=1)
    
    def _create_main_area(self):
        """Crea el área principal con filtros y resultados"""
        self.main_area = Frame(self, bg=self.colors['blue_bg'])
        self.main_area.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        
        # Configuración de columnas
        self.main_area.grid_columnconfigure(0, weight=0)  # Filtros
        self.main_area.grid_columnconfigure(1, weight=1)  # Resultados
        self.main_area.grid_rowconfigure(0, weight=1)
        
        self._create_filters_section()
        self._create_results_section()
    
    def _create_filters_section(self):
        """Crea la sección de filtros"""
        self.filters_frame = Frame(
            self.main_area, 
            bg=self.colors['blue_bg'], 
            width=200
        )
        self.filters_frame.grid(row=0, column=0, sticky="ns")
        
        # Título
        Label(
            self.filters_frame,
            text="Filtros de búsqueda",
            bg=self.colors['blue_bg'],
            fg=self.colors['white_text'],
            font=("nw", 12, "bold"),
        ).grid(row=0, column=0, pady=(10, 0), padx=10, sticky="w")
        
        # Radio buttons
        self.filter_var = StringVar(value="Articulo")
        self.filter_options = ["Articulo", "Libro", "Revista"]
        
        for i, option in enumerate(self.filter_options, start=1):
            Radiobutton(
                self.filters_frame,
                text=option,
                variable=self.filter_var,
                value=option,
                bg=self.colors['blue_bg'],
                fg=self.colors['white_text'],
                selectcolor=self.colors['brown_bg'],
            ).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    def _create_results_section(self):
        """Crea la sección de resultados"""
        self.results_container = Frame(
            self.main_area, 
            bg=self.colors['results_bg']
        )
        self.results_container.grid(
            row=0, column=1, 
            sticky="nsew", 
            padx=20, pady=20
        )
        
        # Canvas y scrollbar
        self.results_canvas = Canvas(
            self.results_container, 
            bg=self.colors['results_bg']
        )
        self.scrollbar = Scrollbar(
            self.results_container, 
            orient="vertical", 
            command=self.results_canvas.yview
        )
        
        # Frame desplazable
        self.scrollable_frame = Frame(
            self.results_canvas, 
            bg=self.colors['results_bg']
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(
                scrollregion=self.results_canvas.bbox("all")
            )
        )
        
        # Configuración del canvas
        self.results_canvas.create_window(
            (0, 0), 
            window=self.scrollable_frame, 
            anchor="nw"
        )
        self.results_canvas.configure(
            yscrollcommand=self.scrollbar.set
        )
        
        # Layout
        self.results_canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.results_container.grid_rowconfigure(0, weight=1)
        self.results_container.grid_columnconfigure(0, weight=1)
        
        # Evento de scroll con rueda del mouse
        self.results_canvas.bind_all(
            "<MouseWheel>", 
            self._on_mouse_wheel
        )
    
    def _setup_results_area(self):
        """Configuración adicional del área de resultados"""
        pass
    
    def _display_initial_results(self):
        """Muestra los resultados iniciales"""
        initial_data = self.controller.get_data()
        self._generate_results(initial_data)
    
    def _generate_results(self, articles):
        """Genera los widgets para mostrar los resultados"""
        # Limpiar resultados anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not articles:
            self._show_no_results_message()
            return
        
        for i, article in enumerate(articles):
            self._create_article_widget(i, article)
    
    def _create_article_widget(self, index, article):
        """Crea un widget para un artículo individual"""
        # Frame principal
        article_frame = Frame(
            self.scrollable_frame,
            bg=self.colors['white_bg'],
            bd=1,
            relief="solid"
        )
        article_frame.grid(
            row=index, column=0, 
            sticky="ew", 
            padx=30, pady=10
        )
        article_frame.grid_columnconfigure(0, weight=1)
        
        # Título
        title_label = Label(
            article_frame,
            text=article.titulo,
            font=("Arial", 14, "bold"),
            bg=self.colors['white_bg'],
            anchor="w",
            wraplength=500,
            justify="left",
        )
        title_label.grid(
            row=0, column=0, 
            sticky="w", 
            padx=10, pady=(10, 0)
        )
        
        # Autor
        author_label = Label(
            article_frame,
            text=article.autor,
            font=("Arial", 12),
            bg=self.colors['white_bg'],
            anchor="w",
            wraplength=500,
            justify="left",
        )
        author_label.grid(
            row=1, column=0, 
            sticky="w", 
            padx=10, pady=(0, 5)
        )
        
        # Descripción
        description_label = Label(
            article_frame,
            text=article.resumen,
            font=("Arial", 10),
            bg=self.colors['white_bg'],
            anchor="w",
            wraplength=500,
            justify="center",
        )
        description_label.grid(
            row=2, column=0, 
            sticky="w", 
            padx=10, pady=(0, 10)
        )
        
        # Pie de artículo
        footer = Frame(article_frame, bg=self.colors['white_bg'])
        footer.grid(
            row=3, column=0, 
            sticky="ew", 
            padx=10, pady=(0, 10)
        )
        footer.grid_columnconfigure(0, weight=1)
        
        # Fecha
        date_label = Label(
            footer,
            text=article.fecha,
            font=("Arial", 10),
            bg=self.colors['white_bg'],
            anchor="w",
        )
        date_label.grid(row=0, column=0, sticky="w")
        
        # Botón de flecha
        arrow_button = Button(
            footer,
            text="→",
            font=("Arial", 14, "bold"),
            bg=self.colors['white_bg'],
            bd=0,
            cursor="hand2",
        )
        arrow_button.grid(row=0, column=1, sticky="e")
    
    def _show_no_results_message(self):
        """Muestra un mensaje cuando no hay resultados"""
        Label(
            self.scrollable_frame,
            text="No se encontraron resultados.",
            font=("Arial", 20, "bold"),
            fg="gray",
            bg=self.colors['results_bg'],
            anchor="center",
        ).grid(row=0, column=0, sticky="nsew", pady=20)
    
    def _perform_search(self):
        """Realiza una búsqueda con los parámetros actuales"""
        search_text = self.search_entry.get()
        filter_type = self.filter_var.get()
        results = self.controller.buscar(search_text, filter_type)
        self._generate_results(results)
    
    def _return_to_index(self):
        """Regresa a la vista de índice"""
        if self.controller:
            self.controller.open_index_view()
    
    def _on_mouse_wheel(self, event):
        """Maneja el scroll con la rueda del mouse"""
        delta = -1 * (event.delta // 120)  # Normaliza para Windows/Linux
        if self.parent.tk.call("tk", "windowingsystem") == "aqua":  # macOS
            delta = event.delta
        self.results_canvas.yview_scroll(delta, "units")
    
    def run(self):
        self.parent.mainloop()