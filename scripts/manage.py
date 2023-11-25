import os
from faker import Faker

fake = Faker()


class Saludo:
    """Prueba para saludar"""

    def __init__(self):
        
        self.id = "123456"
        self.first_name = os.environ.get("FIRST_NAME")
        self.last_name = os.environ.get("LAST_NAME")
        
        self.api_key = os.environ.get("API_KEY")
        self.age = 21
        
        self.mail = fake.email()

        self.full_name = self.set_fullname(self.first_name, self.last_name)
        
        self.lista_personas()

    def retorna(self):
        """Retorna la información del usuario"""
        mensaje = "Hola {}, tu ID es {}".format(self.full_name, self.id)
        print(mensaje)
        
        print(f"esto no se debería ver: {self.api_key}")

    def set_fullname(self, first_name, last_name):
        """Set the user full_name"""
        full_name = f"{first_name} {last_name}"
        #print(f'este es el nombre completo: {full_name}')
        return full_name
    
    def autorizacion(self):
        """ Verifica si es mayor de edad """
        if (self.age >= 18):
            print("es mayor")
        else:
            print("Es menor")

    def lista_personas(self):
        """Generar una lista de 100 personas"""
        
        lista_personas = []

        for _ in range(100):
            persona = {
                'nombre': fake.name(),
                'direccion' : fake.address(),
                'correo': fake.email(),
            }
            lista_personas.append(persona)

        return lista_personas
    
if __name__ == "__main__":
    Saludo()
