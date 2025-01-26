import mysql.connector
from mysql.connector import Error

def init_conexion():
    """
    Inicializa una conexión a la base de datos MySQL.
    Retorna la conexión si es exitosa, de lo contrario, devuelve None.
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",         
            user="root",              
            password="75913",          
            database="biblioteca"     
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None