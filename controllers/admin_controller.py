from models.login_model import LoginModel

class AdminController:
    def __init__(self, root, main_controller):
        self.root = root
        self.main_controller = main_controller  # Controlador principal (IndexController)
        self.model = LoginModel()
    
    def close_session(self):
        event = self.model.close_session()
        if event:
            self.main_controller.open_index_page()
            