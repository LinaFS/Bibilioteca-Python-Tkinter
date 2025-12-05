from models.firebase_config import get_firestore_db
from collections import namedtuple
from datetime import datetime

class AdminModel:
    def __init__(self):
        self.db = get_firestore_db()
        
        # CORRECCIÓN CLAVE: Agregar "total_consultas" al namedtuple
        self.Articulo = namedtuple(
            "Articulo", 
            ["id_artic", "titulo", "resumen", "fecha", "palabras_clave", "fuente_original", 
            "autor", "descriptor_1", "descriptor_2", "descriptor_3", "total_consultas", "created_at"]
        )

    # CREATE (Añadir)
    def create_article(self, data):
        """Guarda un nuevo artículo."""
        try:
            if not self.db: return False
            article_data = {
                'titulo': data.get('titulo', ''),
                'fecha': data.get('fecha', ''),
                'autor': data.get('autor', ''),
                'palabras_clave': data.get('palabras_clave', ''),
                'resumen': data.get('resumen', ''),
                'descriptor_1': data.get('descriptor_1', ''),
                'descriptor_2': data.get('descriptor_2', ''),
                'descriptor_3': data.get('descriptor_3', ''),
                'fuente_original': data.get('fuente_original', 'Articulo'), 
                'created_at': datetime.now(),
                'total_consultas': 0
            }
            self.db.collection('articulos').add(article_data)
            return True
        except Exception as e:
            print(f"❌ Error al crear artículo: {e}")
            return False

    # READ (Consultar/Buscar)
    def get_all_articles(self):
        """Obtiene todos los artículos."""
        try:
            if not self.db: return []
            docs = self.db.collection('articulos').stream()
            # El Articulo corregido ahora acepta el argumento 'total_consultas'
            return [self.Articulo(id_artic=doc.id, **doc.to_dict()) for doc in docs]
        except Exception as e:
            print(f"❌ Error al obtener todos los artículos: {e}")
            return []

    def get_article_by_id(self, article_id):
        """Obtiene un solo artículo por su ID de documento."""
        try:
            if not self.db: return None
            doc_ref = self.db.collection('articulos').document(article_id)
            doc = doc_ref.get()
            if doc.exists:
                return self.Articulo(id_artic=doc.id, **doc.to_dict())
            return None
        except Exception as e:
            print(f"❌ Error al obtener artículo: {e}")
            return None
            
    def search_articles(self, search_term):
        """Busca artículos en todos los campos textuales."""
        all_articles = self.get_all_articles()
        if not search_term: return all_articles
            
        search_term_lower = search_term.lower()
        results = []
        
        for article in all_articles:
            fields_to_search = [
                article.titulo, article.resumen, article.autor, 
                article.palabras_clave, article.fuente_original,
                article.descriptor_1, article.descriptor_2, article.descriptor_3
            ]
            
            # Busqueda simple de subcadena en cualquier campo
            if any(search_term_lower in str(field).lower() for field in fields_to_search if field):
                results.append(article)
                
        return results

    # UPDATE (Modificar)
    def update_article(self, article_id, data):
        """Actualiza un artículo existente."""
        try:
            if not self.db: return False
            doc_ref = self.db.collection('articulos').document(article_id)
            
            update_data = {
                k: data.get(k) for k in data if k != 'id_artic'
            }
            doc_ref.update(update_data)
            return True
        except Exception as e:
            print(f"❌ Error al actualizar artículo: {e}")
            return False

    # DELETE (Eliminar)
    def delete_article(self, article_id):
        """Elimina un artículo por su ID."""
        try:
            if not self.db: return False
            self.db.collection('articulos').document(article_id).delete()
            return True
        except Exception as e:
            print(f"❌ Error al eliminar artículo: {e}")
            return False