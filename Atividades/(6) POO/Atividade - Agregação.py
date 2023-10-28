class Endereco():
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
autor1 = Autor ('Josh Malerman', livro1.titulo)