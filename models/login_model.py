from models.conexion import init_conexion

class LoginModel:
    def create_session(self, user, passwd):
        conexion = init_conexion()
        if conexion:
            cursor = conexion.cursor()
            
            query = """
            SELECT id
            FROM Usuario
            WHERE nombre = %s
            AND contrasenia = %s
            """
            cursor.execute(query, (user, passwd))
            results = cursor.fetchone()
            results = results[0] if results else None
            
            if results != None:
                print(f"Iniciando sesión como {results}...")
                return True
            else:
                print("No se pudo iniciar sesión")
                return False
        else:
            print("No se pudo conectar a la base de datos")
            return None