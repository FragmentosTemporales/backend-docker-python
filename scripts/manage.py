import os
from app import Exec

class Main():
    """Clase principal que ejecuta la función"""
    
    def __init__(self):
        """Iniciamos la aplicación"""
        self.first_name = os.environ.get('FIRST_NAME')
        self.last_name = os.environ.get('LAST_NAME')
        
        print(f"Hola {self.first_name} {self.last_name}!")

        print('Creando lista...')

        self.create_app()

        print('Vuelve pronto!')

    def create_app(self):
        Exec()

if __name__ == "__main__":
    Main()
