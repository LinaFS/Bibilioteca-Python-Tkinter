from models.conexion import init_conexion
from collections import namedtuple
class IndexModel:        
    def search(self, data, filter):
        print(f"Buscando información para: {data} y filtro: {filter}")
        
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
            WHERE (titulo LIKE %s OR resumen LIKE %s)
            AND fuente_original LIKE %s
            """
            cursor.execute(query, (f"%{data}%",f"%{data}%", f"%{filter}%"))
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
    
    def registrar_consulta(self, cursor, id_artic):
        query_registro = "INSERT INTO consultas (id_artic) VALUES (%s)"
        cursor.execute(query_registro, (id_artic,))  # Debe ser una tupla
