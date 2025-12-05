from models.firebase_config import get_firestore_db
# Necesitamos importar ViewsModel porque tu controlador de búsqueda (SearchController)
# llama a la función de artículos más leídos desde este modelo.
from models.views_model import ViewsModel 

class SearchModel:
    def __init__(self):
        # Usamos la configuración de Firebase
        self.db = get_firestore_db()
        self.views_model = ViewsModel() 
        
    def registrar_consulta(self, id_artic):
        # Esta función ya no es necesaria aquí; la lógica de registro
        # se centralizó en IndexModel.search() para que se hiciera en Firebase.
        pass
    
    def buscar_mas_leidos(self):
        """Delega la búsqueda de artículos más leídos al ViewsModel."""
        return self.views_model.buscar_mas_leidos()