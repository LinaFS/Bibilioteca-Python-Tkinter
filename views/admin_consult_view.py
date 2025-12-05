# views/admin_consult_view.py (Tabla de Gestión Integrada)
import tkinter as tk
from tkinter import ttk, Frame, Entry, Button, Scrollbar, Label, messagebox

class AdminConsultView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.configure(bg="#FFFFFF")
        
        self.search_var = tk.StringVar()
        
        self._setup_ui()
        # La primera carga de datos se hace en PanelAdminView.show_frame("Consult")

    def _setup_ui(self):
        self.grid_rowconfigure(0, weight=0) # Fila de título
        self.grid_rowconfigure(1, weight=0) # Fila de búsqueda
        self.grid_rowconfigure(2, weight=1) # Fila de tabla
        self.grid_columnconfigure(0, weight=1)

        # --- Título ---
        Label(self, text="Gestión de Materiales (CRUD)", 
            bg="#FFFFFF", fg="#342217", font=("IstokWeb Regular", 20)
        ).grid(row=0, column=0, pady=(10, 0), padx=20, sticky="w")
        
        # --- Frame de Búsqueda ---
        search_frame = Frame(self, bg="#FFFFFF")
        search_frame.grid(row=1, column=0, pady=(10, 10), padx=20, sticky="ew")
        
        search_entry = Entry(
            search_frame, 
            textvariable=self.search_var, 
            font=("Arial", 12)
        )
        search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        ttk.Button(
            search_frame, 
            text="Buscar", 
            command=lambda: self.load_data(self.search_var.get())
        ).pack(side="left", padx=(0, 5))

        ttk.Button(
            search_frame,
            text="Limpiar",
            command=self.clear_search
        ).pack(side="left")

        # --- Tabla de Resultados (Treeview) ---
        table_container = Frame(self)
        table_container.grid(row=2, column=0, sticky="nsew", padx=20, pady=(0, 20))

        # Definir columnas de la tabla + 2 columnas para acciones
        columns = ("#", "Título", "Autor", "Fecha", "ID_DOC", "Editar", "Eliminar")
        self.tree = ttk.Treeview(table_container, columns=columns, show='headings')
        
        # Definir encabezados y anchos
        self.tree.heading("#", text="N°", anchor="center")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Fecha", text="Año", anchor="center")
        self.tree.heading("ID_DOC", text="ID (Oculto)")
        self.tree.heading("Editar", text="")
        self.tree.heading("Eliminar", text="")
        
        self.tree.column("#", width=30, anchor="center")
        self.tree.column("Título", width=250, anchor="w")
        self.tree.column("Autor", width=120, anchor="w")
        self.tree.column("Fecha", width=60, anchor="center")
        self.tree.column("ID_DOC", width=0, stretch=tk.NO) # Ocultar
        self.tree.column("Editar", width=70, anchor="center")
        self.tree.column("Eliminar", width=70, anchor="center")
        
        vscroll = Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        hscroll = Scrollbar(table_container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vscroll.set, xscrollcommand=hscroll.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        vscroll.grid(row=0, column=1, sticky="ns")
        hscroll.grid(row=1, column=0, sticky="ew")
        
        table_container.grid_rowconfigure(0, weight=1)
        table_container.grid_columnconfigure(0, weight=1)

        self.tree.bind("<ButtonRelease-1>", self.on_action_click) # Captura de clics en acciones

    def clear_search(self):
        self.search_var.set("")
        self.load_data()

    def load_data(self, search_term=None):
        """Carga los datos en el Treeview, con paginación implícita por scroll."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        articles = self.controller.get_articles_for_consult(search_term)
        
        if not articles:
            self.tree.insert('', 'end', values=("", "No se encontraron resultados.", "", "", "", "", ""), tags=('no_results',))
            return
            
        for i, article in enumerate(articles, 1):
            
            action_values = (
                i, 
                article.titulo, 
                article.autor, 
                article.fecha, 
                article.id_artic,
                "✏️ Editar",
                "❌ Eliminar"
            )
            
            self.tree.insert(
                '', 
                'end', 
                values=action_values,
                tags=('odd' if i % 2 != 0 else 'even', article.id_artic)
            )
            
        self.tree.tag_configure('odd', background='#f5f5f5')
        self.tree.tag_configure('even', background='#e0e0e0')


    def on_action_click(self, event):
        """Maneja el clic en las celdas de Editar o Eliminar y llama al controlador."""
        try:
            item = self.tree.identify_row(event.y)
            if not item: return

            column_number = int(self.tree.identify_column(event.x).replace('#', ''))
            
            item_values = self.tree.item(item, 'values')
            article_id = item_values[4] # El ID_DOC está en la columna 4

            if column_number == 6: # Columna "Editar"
                self.controller.start_edit_article(article_id)
            elif column_number == 7: # Columna "Eliminar"
                self.controller.delete_article_action(article_id)

        except Exception as e:
            # print(f"Error al procesar el clic de acción: {e}")
            pass