from models.login_model import LoginModel

class LoginController:
    def __init__(self, root, main_controller):
        self.root = root
        self.main_controller = main_controller  # IndexController
        self.model = LoginModel()
    
    def open_index_view(self):
        self.main_controller.open_index_page()

    def open_panelAdmin_view(self, user, passwd):
        success = self.model.create_session(user, passwd)
        
        if success:
            self.main_controller.open_admin_page()
        else:
            return False