from models.conexion import init_conexion
from collections import namedtuple

class SearchModel:    
    def registrar_consulta(self, cursor, id_artic):
        query_registro = "INSERT INTO consultas (id_artic) VALUES (%s)"
        cursor.execute(query_registro, (id_artic,))
