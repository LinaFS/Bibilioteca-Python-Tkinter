class LoginModel:
    from models import conexion
    con = conexion.Conexion()
     
    def create_session(self, user, passwd):
        resultados = self.con.verificacion_usuario(user, passwd)
        
        if resultados != None:
            print(f"Iniciando sesión como {resultados}...")
            return True
        else:
            print("No se pudo iniciar sesión")
            return False