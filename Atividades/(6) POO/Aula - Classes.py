'''#Exemplo carro
class Carro:
    pneus = 4 #Atributo de classe

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 = Carro('Ford', 'Fiesta') 
carro2 = Carro('Honda', 'Civic')

print(carro1.pneus) #Mostrando o atributo de um objeto
print(carro2.pneus) #''
print(Carro.pneus) #''

Carro.pneus = 3 #Alterando o valor do atributo

print(Carro.pneus)'''

#Exemplo turma
class Turma:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def texto(self):
        print(f'O meu nome é {self.nome} e meu sobrenome é {self.sobrenome}')

aluno1 = Turma('Dieimes', 'Nunes')

print(aluno1.nome)
print(aluno1.sobrenome)

aluno1.texto()

'''#Exemplo animal
class Animal:
    Animal1 = 2

    def __init__(self, raça, espécie):
        self.raça = raça
        self.espécie = espécie

    def texto(self):
        print(f'Animal da raça {self.raça} da espécie {self.espécie}.')

Ab = Animal('Coelho', 'Pulador')

print(Ab.raça)
print(Ab.espécie)

Ab.texto()

print(1 + Animal.Animal1)

#Exemplo calculo
class Calculo:
    N1 = 2
    def __init__(self, *args):
        for arg in args:
            print(arg * Calculo.N1)

print(Calculo.__init__(1, 2, 3, 4, 5, 6))'''