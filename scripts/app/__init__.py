from utils.generate_user_list import GenerateList

class Exec:
    """ Esta función se ejecuta """
    def __init__(self):

        self.generate = GenerateList()
        client_list = self.generate.get_list()
        self.count = 1

        for client in client_list:
            self.user = client['name']
            self.age = client['age']
            confirmation = self.auth(self.age)

            if confirmation == True:
                print(f'#{self.count} - El usuario {self.user}, puede ingresar')
                self.count += 1
            else:
                print(f'#{self.count} - El usuario {self.user}, es menor de edad')
                self.count += 1

    def auth(self, age):
        """Verifica si el usuario es mayor de edad"""
        if age >= 18:
            return True
        else:
            return False
        

if __name__ == "__main__":
    Exec()