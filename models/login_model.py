from models.firebase_config import get_firestore_db
import hashlib

class LoginModel:
    def __init__(self):
        self.db = get_firestore_db()
        self.current_user = None
        self.current_user_id = None

    def _hash_password(self, password):
        """Hashea la contraseña para seguridad"""
        return hashlib.sha256(password.encode()).hexdigest()

    def create_session(self, user, passwd):
        """
        Crea una sesión de usuario
        Args:
            user (str): Nombre de usuario
            passwd (str): Contraseña
        Returns:
            bool: True si el login es exitoso, False en caso contrario
        """
        try:
            if not self.db:
                print("❌ No hay conexión con Firebase")
                return False
            
            # Buscar usuario en Firestore
            usuarios_ref = self.db.collection('usuarios')
            query = usuarios_ref.where('nombre', '==', user).limit(1)
            docs = query.stream()
            
            user_doc = None
            for doc in docs:
                user_doc = doc
                break
            
            if not user_doc:
                print(f"❌ Usuario '{user}' no encontrado")
                return False
            
            user_data = user_doc.to_dict()
            
            # Verificar contraseña (puedes usar hash para mayor seguridad)
            if user_data.get('contrasenia') == passwd:
                self.current_user = user_data
                self.current_user_id = user_doc.id
                print(f"✅ Sesión iniciada como: {user}")
                return True
            else:
                print("❌ Contraseña incorrecta")
                return False
                
        except Exception as e:
            print(f"❌ Error al crear sesión: {e}")
            return False

    def close_session(self):
        """Cierra la sesión actual"""
        if self.current_user:
            print(f"✅ Sesión cerrada para: {self.current_user.get('nombre')}")
        self.current_user = None
        self.current_user_id = None
        return True
    
    def get_current_user(self):
        """Retorna el usuario actual"""
        return self.current_user
    
    def is_admin(self):
        """Verifica si el usuario actual es administrador"""
        if self.current_user:
            return self.current_user.get('permisos') == 1
        return False