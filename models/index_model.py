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
            
            resultados_array = []

            for row in resultados:
                resultado = {
                    "id_artic": row[0],
                    "titulo": row[1],
                    "resumen": row[2],
                    "fecha": row[3],
                    "palabras_clave": row[4],
                    "fuente_original": row[5],
                    "autor": row[6],
                    "descriptor_1": row[7],
                    "descriptor_2": row[8],
                    "descriptor_3": row[9]
                }
                resultados_array.append(resultado)

            return resultados_array
        else:
            print("No se pudo conectar a la base de datos")
            return None