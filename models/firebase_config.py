import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

class FirebaseConfig:
    _instance = None
    _db = None
    
    # 1. MODIFICACIÓN: Aceptar la ruta de credenciales en el constructor
    def __new__(cls, cred_path=None): 
        if cls._instance is None:
            cls._instance = super(FirebaseConfig, cls).__new__(cls)
            # Pasamos la ruta al método de inicialización
            cls._instance._initialize_firebase(cred_path)
        return cls._instance
    
    # 2. MODIFICACIÓN: Usar la ruta proporcionada, sin calcularla internamente
    def _initialize_firebase(self, cred_path):
        """Inicializa la conexión con Firebase usando la ruta proporcionada."""
        try:
            # Si no se proporciona ruta, buscar el archivo en el root del proyecto
            if not cred_path:
                possible = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'firebase-credentials.json'))
                if os.path.exists(possible):
                    cred_path = possible

            # Validación de la ruta para manejo de errores
            if not cred_path or not os.path.exists(cred_path):
                raise FileNotFoundError(f"Archivo de credenciales no encontrado en: {cred_path}")
            
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
    """Función helper para obtener la base de datos de Firestore.
       Llamar a esta función sin argumentos asume que Firebase ya fue inicializado por main.py."""
    config = FirebaseConfig()
    return config.get_db()