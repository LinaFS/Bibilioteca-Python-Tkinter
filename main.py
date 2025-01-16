from controllers.index_controller import IndexController
from views.index_view import IndexView
from models.conexion import init_conexion

def main():
    # Crear el controlador
    controller = IndexController(None)  # Inicialmente el controlador no tiene vista
    
    # Crear la vista y pasarle el controlador
    view = IndexView(controller)  # Ahora le pasamos el controlador
    
    # Vincular el controlador a la vista
    controller.view = view  # Asegúrate de que el controlador tiene la vista
    
    conexion = init_conexion()
    
    # Ejecutar la aplicación
    view.run()

if __name__ == "__main__":
    main()
