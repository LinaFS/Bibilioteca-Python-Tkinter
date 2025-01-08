class IndexModel:
<<<<<<< HEAD
    from models import conexion

    con = conexion.Conexion()
    
    def search(self, data):
        print(f"Buscando información para: {data}")
        resultados = self.con.buscar_xtitulo(data)
        for row in resultados:
                    print(row)
        
=======
    def search(self, data):
        print(f"Buscando información para: {data}")
>>>>>>> parent of 0c8761e (Actualización 07/01/25)
