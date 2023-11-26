from faker import Faker

fake = Faker()

class GenerateList:
    """
    Genera una lista de 100 usuarios
    """
    def __init__(self):
        self.users_list = []

        for _ in range(100):
            persona = {
                'name': fake.name(),
                'address' : fake.address(),
                'email': fake.email(),
                'age' : fake.random_int(min=14, max=99),
                'phone' : fake.phone_number(),
            }
            self.users_list.append(persona)
        
        self.get_list()
        
    def get_list(self):
        """Retorna la lista de usuarios"""
        list_to_return = self.users_list
                
        return list_to_return

if __name__ == "__main__":
    GenerateList()
