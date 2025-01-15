import conexion

con = conexion.Conexion()

#con.mostrar_librerias()

#resultados = con.mostrar_articulos()
#for row in resultados:
#            print(row)

resultados = con.verificacion_usuario('Noemi', '1234')
for row in resultados:
            print(row)