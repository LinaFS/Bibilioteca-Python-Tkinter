from models.news_model import NewsModel

class NewsController:
    def __init__(self, view):
        self.view = view
        self.model = NewsModel()

    def mostrar_novedades(self):
        """Lógica para mostrar los artículos en novedades."""     
        resultados = self.model.buscar_novedades()
        if len(resultados) == 0:
            return None
        else:
            return resultados   