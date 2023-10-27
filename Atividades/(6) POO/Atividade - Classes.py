#Atividade 01

class Estudante:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def texto(self):
        print(f'O nome do estudante é {self.nome} e ele tem {self.idade} anos.')

Dados = Estudante('Eduardo', '18')

print(Dados.nome)
print(Dados.idade)
Dados.texto()

#Atividade 02

class Livro:
    título = 'Clube da luta'
    autor = 'Chuck Palahniuk'
    ano_publicação = 2012

    def __init__(self, título, autor, ano_publicação):
        self.título	= título
        self.autor = autor
        self.ano_publicação = ano_publicação

    def descrição(self):
        print(f'Título: {self.título}\nAutor: {self.autor}\nAno de publicação: {self.ano_publicação}\n')

CaixaDePássaros = Livro('Caixa de pássaros', 'Josh Malerman', 2015)
OsGarotosCorvos = Livro('Os garotos corvos', 'Maggie Stiefvater', 2013)

CaixaDePássaros.descrição()
OsGarotosCorvos.descrição()

#Atividade 03

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    def Depositar(self, valor):
        self.valor = valor
        self.saldo += self.valor
        print(f'{self.titular} depositou R${self.saldo} na sua conta bancária')
    def Sacar(self, valor):
        self.valor = valor
        if self.saldo < self.valor:
            print('Saldo insuficiente para realizar saque!')
        else:
            self.saldo -= self.valor
            print(f'{self.titular} sacou R${self.saldo} da sua conta bancária')

titular = ContaBancaria('Eduardo')
titular.Depositar(100)
titular.Sacar(70)