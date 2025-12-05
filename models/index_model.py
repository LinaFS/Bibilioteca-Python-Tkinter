from models.firebase_config import get_firestore_db
from collections import namedtuple
from datetime import datetime

class IndexModel:
    def __init__(self):
        self.db = get_firestore_db()
        
    def search(self, data, filter):
        """
        Busca artículos en Firebase
        Args:
            data (str): Término de búsqueda
            filter (str): Tipo de filtro (articulo, libro, revista)
        Returns:
            list: Lista de artículos encontrados
        """
        print(f"🔍 Buscando información para: {data} y filtro: {filter}")
        
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
            
            # Obtener todos los documentos (Firestore no permite búsqueda LIKE directamente)
            docs = articulos_ref.stream()
            
            resultados = []
            data_lower = data.lower() if data else ""
            filter_lower = filter.lower() if filter else ""
            
            for doc in docs:
                doc_data = doc.to_dict()
                
                # Filtrar por tipo de fuente
                fuente = doc_data.get('fuente_original', '').lower()
                if filter_lower and filter_lower not in fuente:
                    continue
                
                # Filtrar por título o resumen
                titulo = doc_data.get('titulo', '').lower()
                resumen = doc_data.get('resumen', '').lower()
                
                if data_lower in titulo or data_lower in resumen:
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
                    resultados.append(articulo)
                    
                    # Registrar la consulta
                    self.registrar_consulta(doc.id)
            
            print(f"✅ Se encontraron {len(resultados)} resultados")
            return resultados if resultados else None
            
        except Exception as e:
            print(f"❌ Error al buscar: {e}")
            return None
    
    def registrar_consulta(self, id_artic):
        """
        Registra una consulta en Firebase
        Args:
            id_artic (str): ID del artículo consultado
        """
        try:
            if not self.db:
                return
            
            consultas_ref = self.db.collection('consultas')
            consultas_ref.add({
                'id_artic': id_artic,
                'fecha_consulta': datetime.now()
            })
            
            # Actualizar contador en el artículo
            articulo_ref = self.db.collection('articulos').document(id_artic)
            articulo = articulo_ref.get()
            
            if articulo.exists:
                data = articulo.to_dict()
                total_consultas = data.get('total_consultas', 0) + 1
                articulo_ref.update({'total_consultas': total_consultas})
                
        except Exception as e:
            print(f"⚠️ Error al registrar consulta: {e}")