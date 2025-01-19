class SearchView:
    def __init__(self, view):
        self.view = view
        
    def open_index_view(self, window):
        from views.search_view import SearchView  # Importar la nueva clase SearchView
        window.destroy()
        view = SearchView(self)  # Pasar el controlador actual a la nueva vista
        view.run()
