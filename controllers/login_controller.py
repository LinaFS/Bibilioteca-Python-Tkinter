class LoginController:
    def __init__(self, view):
        self.view = view

    def on_login_click(self):
        username = self.view.entry_1.get()
        password = self.view.entry_2.get()
        
        # Aquí validas el usuario y contraseña
        if username == "admin" and password == "1234":
            print("Inicio de sesión exitoso")
        else:
            print("Error: Usuario o contraseña incorrectos")
