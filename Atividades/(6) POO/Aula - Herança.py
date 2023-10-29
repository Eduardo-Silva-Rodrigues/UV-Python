# Herança de classes:
class Animal: # Esta é a superclasse da qual compartilhará seus atributos e métodos com as subclasses
    def __init__(self, nome):
        self.nome = nome # Atributo

    def Disse(): # Método
        pass

class Chachorro(Animal): # Subclasse Cachorro que herdará os atributos e métodos
    def Disse(self):
        return f'{self.nome} disse Au Au!'

class Gato(Animal): # Subclasse Gato que herdará os atributos e métodos
    def Disse(self):
        return f'{self.nome} disse Miau!'
    
cachorro = Chachorro('Mel')
gato = Gato('Milo')

print(gato.Disse())
print(cachorro.Disse())