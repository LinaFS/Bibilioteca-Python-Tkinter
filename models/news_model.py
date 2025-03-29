from models.conexion import init_conexion
from collections import namedtuple
class NewsModel:
    def buscar_novedades(self):
        """Lógica para mostrar los artículos en novedades."""
        Articulo = namedtuple(
            "Articulo", 
            ["id_artic", "titulo", "resumen", "fecha", "palabras_clave", "fuente_original", 
            "autor", "descriptor_1", "descriptor_2", "descriptor_3"]
        )
        
        conexion = init_conexion()
        if conexion:
            cursor = conexion.cursor()
            
            query = """
            SELECT id_artic, titulo, resumen, fecha, palabras_clave, fuente_original, autor, 
                descriptor_1, descriptor_2, descriptor_3 
            FROM Articulo 
            ORDER BY id_artic DESC limit 10
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            articulos = [Articulo(*fila) for fila in resultados]
                    
            conexion.commit()
            cursor.close()
            conexion.close()

            return articulos
        else:
            print("No se pudo conectar a la base de datos")
            return None
        
    