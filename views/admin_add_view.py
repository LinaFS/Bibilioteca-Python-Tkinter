# views/admin_add_view.py (Formulario unificado - Usado para Añadir y Editar)
import tkinter as tk
from tkinter import ttk, messagebox

class AdminAddView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.configure(bg="#FFFFFF")
        
        self.current_article_id = None 

        self.fields_info = [
            ("Título", "titulo", 1),
            ("Fecha de publicación", "fecha", 1),
            ("Autor", "autor", 1),
            ("Fuente Original (Revista, Libro, etc.)", "fuente_original", 1), 
            ("Palabras clave", "palabras_clave", 1),
            ("Resumen", "resumen", 5),
            ("Descriptor 1", "descriptor_1", 1),
            ("Descriptor 2", "descriptor_2", 1),
            ("Descriptor 3", "descriptor_3", 1),
        ]
        self.entries = {}
        
        self._setup_ui()

    # ... (métodos _setup_ui, _create_scrollable_form, clear_form, load_form, validar_y_guardar del plan anterior) ...
    
    # [El código de estos métodos es extenso y se asume que se ha pegado de la respuesta anterior
    # ya que maneja la lógica de cargar/limpiar/validar para Añadir y Editar.]
    
    def _setup_ui(self):
        self.form_container = ttk.Frame(self, padding="20")
        self.form_container.pack(fill="both", expand=True)

        self.header_label = ttk.Label(self.form_container, text="Agregar Nuevo Material", font=("Arimo", 24))
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="w")
        
        self._create_scrollable_form()
        
        self.save_button = ttk.Button(
            self.form_container, text="Guardar Material", command=self.validar_y_guardar
        )
        self.save_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    def _create_scrollable_form(self):
        self.scroll_canvas = tk.Canvas(self.form_container, highlightthickness=0)
        self.scroll_canvas.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.form_container.grid_rowconfigure(1, weight=1)
        self.form_container.grid_columnconfigure(0, weight=1)
        
        self.scrollable_frame = ttk.Frame(self.scroll_canvas, padding="5")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.scroll_canvas.configure(
                scrollregion=self.scroll_canvas.bbox("all")
            )
        )
        self.scroll_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=500)
        
        self.scrollbar = ttk.Scrollbar(self.form_container, orient="vertical", command=self.scroll_canvas.yview)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky="ns")
        
        for i, (label_text, var_name, height) in enumerate(self.fields_info):
            lbl = ttk.Label(self.scrollable_frame, text=label_text + ":", font=("Arimo", 14))
            lbl.grid(row=i * 2, column=0, sticky="w", padx=10, pady=(10, 0))

            entry = tk.Text(self.scrollable_frame, width=60, height=height, bg="#d9d7d5", font=("Arial", 12))
            entry.grid(row=i * 2 + 1, column=0, padx=10, pady=(0, 10), sticky="ew")
            self.entries[var_name] = entry

    def clear_form(self):
        self.current_article_id = None
        for entry in self.entries.values():
            entry.delete("1.0", tk.END)

    def load_form(self):
        article_data = self.controller.get_article_to_edit()
        self.clear_form() 

        if article_data:
            self.header_label.config(text="Modificar Material")
            self.save_button.config(text="Actualizar Material")
            self.current_article_id = article_data.get('id_artic')
            
            for var_name, entry in self.entries.items():
                value = article_data.get(var_name, '')
                if value:
                    entry.insert("1.0", str(value))
        else:
            self.header_label.config(text="Agregar Nuevo Material")
            self.save_button.config(text="Guardar Material")

    def validar_y_guardar(self):
        data = {}
        missing_fields = []
        required_fields = ["titulo", "autor", "resumen"]
        
        for var_name, entry_widget in self.entries.items():
            content = entry_widget.get("1.0", "end-1c").strip()
            data[var_name] = content
            
            if var_name in required_fields and not content:
                missing_fields.append(var_name)
        
        if missing_fields:
            messagebox.showwarning("Advertencia", f"Los siguientes campos son obligatorios: {', '.join(missing_fields)}.")
            return

        if self.current_article_id:
            data['id_artic'] = self.current_article_id

        self.controller.save_material(data)