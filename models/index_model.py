from models.conexion import init_conexion
class IndexModel:
    def search(self, data, filter):
        print(f"Buscando información para: {data} y filtro: {filter}")
        
        conexion = init_conexion()
        if conexion:
            cursor = conexion.cursor()
            
            query = """
            SELECT id_artic, titulo, resumen, fecha, palabras_clave, fuente_original, autor, 
                descriptor_1, descriptor_2, descriptor_3 
            FROM Articulo 
            WHERE titulo LIKE %s
            AND fuente_original LIKE %s
            """
            cursor.execute(query, (f"%{data}%", f"%{filter}%"))
            resultados = cursor.fetchall()
            
            for row in resultados:
                        print(row)
        else:
            print("No se pudo conectar a la base de datos")
            return None