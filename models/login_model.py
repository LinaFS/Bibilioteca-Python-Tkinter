class LoginModel:
    def create_session(self, user, passwd):
        print("Iniciando sesión como admin...")
        if user == "Usuario" and passwd == "Contraseña":
            return True
        else:
            print("No se pudo iniciar sesión")
            return False