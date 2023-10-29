# Associação de professor para curso
class Estudante:
    def __init__(self, nome):
        self.nome = nome
    
    def estuda(self, materia):
        print(f'{self.nome} estuda {materia}')

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ensina(self, materia, estudante):
        print(f'{self.nome} ensina {materia} para {estudante.nome}')

estudante1 = Estudante('Eduardo')
estudante2 = Estudante('João')
professor = Professor('Michael')

professor.ensina('Análise', estudante2)
estudante1.estuda('Programação')

'''Através de um método a classe 1 usa um objeto da classe 2'''





















'''# Associação de caneta com pessoa
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
print(caneta1.dono)'''