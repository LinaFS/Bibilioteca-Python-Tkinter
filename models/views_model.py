from models.firebase_config import get_firestore_db
from collections import namedtuple

class ViewsModel:
    def __init__(self):
        self.db = get_firestore_db()
        
    def buscar_mas_leidos(self):
        """
        Obtiene los artículos más leídos
        Returns:
            list: Lista de artículos ordenados por número de consultas
        """
        Articulo = namedtuple(
            "Articulo", 
            ["id_artic", "titulo", "resumen", "fecha", "palabras_clave", "fuente_original", 
            "autor", "descriptor_1", "descriptor_2", "descriptor_3"]
        )
        
        try:
            if not self.db:
                print("❌ No hay conexión con Firebase")
                return None
            
            articulos_ref = self.db.collection('articulos')
            
            # Ordenar por total_consultas descendente y limitar a 10
            query = articulos_ref.order_by('total_consultas', direction='DESCENDING').limit(10)
            docs = query.stream()
            
            articulos = []
            for doc in docs:
                doc_data = doc.to_dict()
                articulo = Articulo(
                    id_artic=doc.id,
                    titulo=doc_data.get('titulo', ''),
                    resumen=doc_data.get('resumen', ''),
                    fecha=doc_data.get('fecha', ''),
                    palabras_clave=doc_data.get('palabras_clave', ''),
                    fuente_original=doc_data.get('fuente_original', ''),
                    autor=doc_data.get('autor', ''),
                    descriptor_1=doc_data.get('descriptor_1', ''),
                    descriptor_2=doc_data.get('descriptor_2', ''),
                    descriptor_3=doc_data.get('descriptor_3', '')
                )
                articulos.append(articulo)
            
            print(f"✅ Se encontraron {len(articulos)} artículos más leídos")
            return articulos if articulos else None
            
        except Exception as e:
            print(f"❌ Error al buscar más leídos: {e}")
            return None