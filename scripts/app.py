from manage import Saludo

class Exec:
    """ Esta función se ejecuta """
    def __init__(self):
        self.saludo = Saludo()
        self.lista = self.saludo.lista_personas()
        self.conteo = 1
        
        for item in self.lista:
            print(f'#{self.conteo}.- {item}')
            self.conteo += 1
        
        
if __name__ == "__main__":
    Exec()