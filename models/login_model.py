from models.conexion import init_conexion

class LoginModel:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def create_session(self, user, passwd):
        self.conexion = init_conexion()
        if self.conexion:
            self.cursor = self.conexion.cursor()
            
            query = """
            SELECT id
            FROM Usuario
            WHERE nombre = %s
            AND contrasenia = %s
            """
            self.cursor.execute(query, (user, passwd))
            results = self.cursor.fetchone()
            results = results[0] if results else None
            
            if results is not None:
                print(f"Iniciando sesión como {results}...")
                return True
            else:
                print("No se pudo iniciar sesión")
                return False
        else:
            print("No se pudo conectar a la base de datos")
            return None

    def close_session(self):
        if self.cursor:
            self.cursor.close()  # Cierra el cursor
            self.cursor = None
        if self.conexion:
            self.conexion.close()  # Cierra la conexión
            self.conexion = None
        return True
