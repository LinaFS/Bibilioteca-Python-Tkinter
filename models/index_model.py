class IndexModel:
    from models import conexion

    con = conexion.Conexion()
    def search(self, data, filter):
        print(f"Buscando información para: {data} y filtro: {filter}")
        resultados = self.con.buscar_xtitulo(data)
        for row in resultados:
                    print(row)