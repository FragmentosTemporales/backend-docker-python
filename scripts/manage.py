import os
from faker import Faker

fake = Faker()


class Saludo:
    """Prueba para saludar"""

    def __init__(self):
        self.id = "123456"
        self.first_name: str = os.environ.get("FIRST_NAME")
        self.last_name: str = os.environ.get("LAST_NAME")
        self.mail = fake.email()

        self.full_name = self.set_fullname(self.first_name, self.last_name)

        self.retorna()

    def retorna(self):
        """Retorna la información del usuario"""
        mensaje = "Hola {}, tu ID es {}".format(self.full_name, self.id)
        print(mensaje)

    def set_fullname(self, first_name, last_name):
        """Set the user full_name"""
        full_name = f"{first_name} {last_name}"
        return full_name


if __name__ == "__main__":
    Saludo()
