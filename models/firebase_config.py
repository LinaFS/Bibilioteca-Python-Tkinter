import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

class FirebaseConfig:
    _instance = None
    _db = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirebaseConfig, cls).__new__(cls)
            cls._instance._initialize_firebase()
        return cls._instance
    
    def _initialize_firebase(self):
        """Inicializa la conexión con Firebase"""
        try:
            # Ruta al archivo de credenciales
            cred_path = os.path.join(os.path.dirname(__file__), '..', 'firebase-credentials.json')
            
            # Inicializar Firebase Admin SDK
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            
            # Obtener referencia a Firestore
            self._db = firestore.client()
            
            print("✅ Firebase inicializado correctamente")
        except Exception as e:
            print(f"❌ Error al inicializar Firebase: {e}")
            self._db = None
    
    def get_db(self):
        """Retorna la instancia de Firestore"""
        return self._db
    
    def is_connected(self):
        """Verifica si hay conexión con Firebase"""
        return self._db is not None


def get_firestore_db():
    """Función helper para obtener la base de datos de Firestore"""
    config = FirebaseConfig()
    return config.get_db()