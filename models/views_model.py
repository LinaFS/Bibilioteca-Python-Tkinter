from models.conexion import init_conexion
from collections import namedtuple

class ViewsModel:
    def buscar_mas_leidos(self):
        Articulo = namedtuple(
            "Articulo", 
            ["id_artic", "titulo", "resumen", "fecha", "palabras_clave", "fuente_original", 
            "autor", "descriptor_1", "descriptor_2", "descriptor_3"]
        )
        
        conexion = init_conexion()
        if conexion:
            cursor = conexion.cursor()
            
            query = """
            SELECT 
                art.id_artic, 
                art.titulo, 
                art.resumen, 
                art.fecha, 
                art.palabras_clave, 
                art.fuente_original, 
                art.autor,
                art.descriptor_1, 
                art.descriptor_2, 
                art.descriptor_3
            FROM Articulo art
            LEFT JOIN (
                SELECT id_artic, COUNT(*) AS total_consultas
                FROM CONSULTAS
                GROUP BY id_artic
                UNION ALL
                SELECT id_artic, SUM(total_consultas) 
                FROM CONSULTAS_RESUMEN
                GROUP BY id_artic
            ) consultas_totales ON art.id_artic = consultas_totales.id_artic
            GROUP BY art.id_artic
            ORDER BY SUM(consultas_totales.total_consultas) DESC
            LIMIT 10;
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            articulos = [Articulo(*fila) for fila in resultados]
            
            cursor.close()
            conexion.close()

            return articulos
        else:
            print("No se pudo conectar a la base de datos")
            return None