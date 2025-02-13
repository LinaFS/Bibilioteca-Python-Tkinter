from models.conexion import init_conexion
from collections import namedtuple

class SearchModel:
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
            ORDER BY id DESC limit 10
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            articulos = [Articulo(*fila) for fila in resultados]
            
            if len(resultados) != 0:
                for articulo in articulos:
                    self.registrar_consulta(cursor, articulo.id_artic)
                    
            conexion.commit()
            cursor.close()
            conexion.close()

            return articulos
        else:
            print("No se pudo conectar a la base de datos")
            return None
        
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
            SELECT art.id_artic, art.titulo, art.resumen, art.fecha, art.palabras_clave, art.fuente_original, art.autor, 
                art.descriptor_1, art.descriptor_2, art.descriptor_3, conres.total_consultas
            FROM Articulo  art
            JOIN consultas_resumen conres ON art.id_artic = conres.id_artic
            ORDER BY conres.total_consultas DESC
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
    
    def registrar_consulta(self, cursor, id_artic):
        query_registro = "INSERT INTO consultas (id_artic) VALUES (%s)"
        cursor.execute(query_registro, (id_artic,))  # Debe ser una tupla
