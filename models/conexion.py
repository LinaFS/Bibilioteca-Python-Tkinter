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
        
    def mostrar_librerias(self):
        self.cursor.execute("SHOW DATABASES")
        results = self.cursor.fetchall()
        
        for row in results:
            print(row)