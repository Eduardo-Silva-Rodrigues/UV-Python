# Composição de classes
class Motor:
    def ligar(self):
        print('Motor ligado')

class Radio:
    def conectar(self):
        print('Radio ligado')

class Carro:
    def __init__(self):
        self.motor = Motor() # Para usar métodos e atributos de outras classes é necessário criar uma instância, e para fazer isso é necessário colcoar () no final do nome da classe para criar essa instância
        self.radio = Radio()

    def ligar(self):
        print('Carro está ligando...')
        self.motor.ligar()

    def conectar(self):
        self.radio.conectar()

carro = Carro()
carro.ligar()
carro.conectar()

'''Através do método construtor de classe 1 você coloca a classe 2 dentro do atributo da classe 1'''