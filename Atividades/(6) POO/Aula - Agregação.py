class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
    
    def adicionar_professor(self, professor):
        self.professores.append(professor)
    
    def listar_professores(self):
        for professor in self.professores: # O parâmetro "professor" é a representação do objeto dentro da lista
            print(f'{professor.nome} trabalha no departamento de {self.nome}')

class Professor:
    def __init__(self, nome):
        self.nome = nome

departamento_matematica = Departamento('Matemática')
departamento_fisica = Departamento('Física')
professor1 = Professor('Giulius')
professor2 = Professor('Paulo')

departamento_matematica.adicionar_professor(professor1)
departamento_fisica.adicionar_professor(professor2)

departamento_matematica.listar_professores()
departamento_fisica.listar_professores()

'''Através de um método a classe 1 pode unir o objeto da classe 2 com o seu objeto'''























'''class Endereco():
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class Pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        print(f'Pessoa {nome} mora do endereço {endereco}')

endereco1 = Endereco('Joaquim Marques', 'São Paulo')
pessoa1 = Pessoa('Eduardo', endereco1.cidade)

class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
class Autor():
    def __init__(self, nome, livro):
        self.nome = nome
        self.livro = livro
        print(f'O autor {self.nome} escreveu o livro {self.livro}')

livro1 = Livro('Caixa de pássaros', 'Josh Malerman')
autor1 = Autor ('Josh Malerman', livro1.titulo)'''