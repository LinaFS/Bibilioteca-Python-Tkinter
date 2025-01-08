import mysql.connector

def init_conexion():
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1234",
        )
        return conexion

class Conexion:    
    def __init__(self):
        self.conexion = init_conexion()
        self.cursor = self.conexion.cursor()
        self.cursor.execute("USE Biblioteca")
    
    def mostrar_articulos(self):
        self.cursor.execute("SELECT id_artic, titulo, resumen, fecha, palabras_clave, fuente_original, autor, descriptor_1, descriptor_2 , descriptor_3 FROM Articulo")
        results = self.cursor.fetchall()
        
        return results
    
    def buscar_xtitulo(self, data):
        query = """
        SELECT id_artic, titulo, resumen, fecha, palabras_clave, fuente_original, autor, 
            descriptor_1, descriptor_2, descriptor_3 
        FROM Articulo 
        WHERE titulo LIKE %s
        """
        self.cursor.execute(query, (f"%{data}%",))
        results = self.cursor.fetchall()
        
        return results
    
    def mostrar_all_usuarios(self):
        self.cursor.execute("SELECT id, nombre, contrasenia, permisos FROM Usuario")
        results = self.cursor.fetchall()
        return results
    
    def verificacion_usuario(self, user, password):
        self.cursor.execute(f'SELECT id FROM Usuario WHERE (nombre = "{user}" AND contrasenia = "{password}")')
        results = self.cursor.fetchall()
        return results
    
    def mostrar_us_admins(self):
        self.cursor.execute("SELECT id, nombre, contrasenia, permisos FROM Usuario WHERE permisos = 1")
        results = self.cursor.fetchall()
        return results
    
    def mostrar_us_usuarios(self):
        self.cursor.execute("SELECT id, nombre, contrasenia, permisos FROM Usuario WHERE permisos = 2")
        results = self.cursor.fetchall()
        return results