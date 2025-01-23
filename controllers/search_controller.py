class SearchView:
    def __init__(self, view):
        self.view = view
        
    def open_index_view(self, window):
        from views.search_view import SearchView  # Importar la nueva clase SearchView
        window.destroy()
        view = SearchView(self)  # Pasar el controlador actual a la nueva vista
        view.run()

    def buscar(self, texto):
        """Lógica para la búsqueda."""
        print(f"Buscando: {texto}")

    def mostrar_mas_leidos(self):
        """Lógica para mostrar los artículos más leídos."""
        print("Mostrando los artículos más leídos...")

    def mostrar_novedades(self):
        """Lógica para mostrar novedades."""
        print("Mostrando las novedades...")