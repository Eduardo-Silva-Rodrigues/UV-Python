# Associação de caneta com pessoa
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.dono = None

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.caneta = None

    def Pegar_Caneta(self, caneta):
        caneta.dono = self.nome
        print(f'O {self.nome} pegou a caneta {self.caneta}')

pessoa1 = Pessoa('Eduardo')
caneta1 = Caneta('azul')

pessoa1.Pegar_Caneta(caneta1)
print(caneta1.dono)

# Associação de professor para curso
class Curso:
    def __init__(self, curso):
        self.curso = curso
        self.professor = []

class Professor:
    def __init__(self, nome):
        self.nome = nome
