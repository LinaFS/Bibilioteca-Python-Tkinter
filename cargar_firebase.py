import csv
from datetime import datetime
from models.firebase_config import FirebaseConfig # Usamos tu clase para la conexión
from io import StringIO
import os

# Define la estructura de tu archivo TSV (datos.txt limpio)
# Debe coincidir con el orden de las columnas en tu archivo .txt
FIELD_NAMES = [
    "id_articulo", "titulo", "resumen", "fecha", "palabras_clave", 
    "fuente_original", "autor", "descriptor_1", "descriptor_2", "descriptor_3"
]

def cargar_articulos_a_firestore(file_path):
    """Procesa un archivo TSV y carga los documentos en Firestore."""
    
    # 1. Inicializa Firebase (usando tu configuración)
    firebase_config = FirebaseConfig()
    db = firebase_config.get_db()

    if not db:
        print("❌ Error: No se pudo conectar a Firestore.")
        return

    articulos_ref = db.collection('articulos')
    batch = db.batch() # Usar batch para cargas masivas eficientes
    batch_count = 0
    total_articulos = 0
    
    try:
        # Nota: Asegúrate de que 'datos.txt' esté en formato TSV plano (una línea por registro)
        with open(file_path, 'r', encoding='latin1') as file:
            # Usamos el módulo csv con el delimitador de tabulador
            # Cuidado: Si tu archivo no es un TSV estándar, esta parte necesitará ajustes de parseo.
            reader = csv.DictReader(file, fieldnames=FIELD_NAMES, delimiter='\t')
            
            # Saltamos la primera línea si es una cabecera, si no, elimina este 'next'
            # next(reader) 

            for row in reader:
                # 2. Crea el documento para Firestore
                
                # Prepara el documento con valores por defecto para NoSQL
                # Es importante añadir 'total_consultas' y 'created_at' para las vistas de la app
                articulo_data = {
                    'titulo': row.get('titulo', '').strip(),
                    'resumen': row.get('resumen', '').strip(),
                    'fecha': row.get('fecha', '').strip(),
                    'palabras_clave': row.get('palabras_clave', '').strip(),
                    'fuente_original': row.get('fuente_original', '').strip(),
                    'autor': row.get('autor', '').strip(),
                    'descriptor_1': row.get('descriptor_1', '').strip(),
                    'descriptor_2': row.get('descriptor_2', '').strip(),
                    'descriptor_3': row.get('descriptor_3', '').strip(),
                    'total_consultas': 0, # Campo para la función de 'Más Leídos'
                    'created_at': datetime.now() # Campo para 'Novedades'
                }
                
                # Limpia los valores NULL (o crea tu propia lógica para manejo de NULLs)
                for key, value in articulo_data.items():
                    if isinstance(value, str) and value.upper() in ('NULL', ''):
                        articulo_data[key] = None
                
                # 3. Agrega la operación al lote
                # Usamos el ID original del SQL como un campo de metadato, o puedes usarlo como ID de documento si lo deseas (pero es mejor dejar que Firestore genere el ID)
                
                # Dejamos que Firestore genere un ID aleatorio y único:
                doc_ref = articulos_ref.document()
                batch.set(doc_ref, articulo_data)
                
                batch_count += 1
                total_articulos += 1
                
                # 4. Ejecuta el lote cada 500 operaciones
                if batch_count >= 500:
                    batch.commit()
                    batch = db.batch()
                    batch_count = 0
                    print(f"-> 500 artículos cargados. Total: {total_articulos}")

        # Ejecuta el lote final si hay operaciones pendientes
        if batch_count > 0:
            batch.commit()
        
        print(f"✅ Carga finalizada. Total de artículos cargados: {total_articulos}")

    except FileNotFoundError:
        print(f"❌ Error: Archivo no encontrado en la ruta: {file_path}")
    except Exception as e:
        print(f"❌ Ocurrió un error durante la carga: {e}")

from models.firebase_config import get_firestore_db
import hashlib

def cargar_usuarios_a_firestore():
    db = get_firestore_db()
    if not db:
        return

    usuarios_ref = db.collection('usuarios')

    # Los datos de tu SQL original
    usuarios = [
        {"nombre": "Admin", "contrasenia": "1234", "permisos": 1},
        {"nombre": "Usuario", "contrasenia": "1234", "permisos": 2},
        # Los que tenías en la consulta original:
        {"nombre": "noemi", "contrasenia": "1234", "permisos": 1},
        {"nombre": "noemiuser", "contrasenia": "1234", "permisos": 2},
    ]

    print("Cargando usuarios...")
    for user_data in usuarios:
        # En una aplicación real, usarías Firebase Authentication para la contraseña,
        # pero aquí simplemente replicamos el campo 'contrasenia' de tu modelo.
        # Asegúrate de que el campo 'permisos' sea un número, no un string.
        
        # Firestore generará un ID automáticamente.
        usuarios_ref.add(user_data)
        print(f"   -> Usuario {user_data['nombre']} cargado.")

# Llama a la función
# cargar_usuarios_a_firestore()

# Ruta al archivo datos.txt
# Asegúrate de que esta ruta sea la correcta en tu sistema
data_file_path = os.path.join(os.path.dirname(__file__), 'datos.txt') 

# Llama a la función
cargar_articulos_a_firestore(data_file_path)
cargar_usuarios_a_firestore() 
# NOTA: Comenta la línea anterior para que no se ejecute en mi entorno.