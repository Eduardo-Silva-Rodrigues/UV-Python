#Pincher caramelo
class Modelo_Peso:
    def __init__(self, raça, peso):
        self.raça = raça
        self.peso = peso
    def texto(self):
        print(f'A raça do cachorro é {self.raça} e seu peso é {self.peso}')

Cachorro = Modelo_Peso('Caramelo', '500g')

print(Cachorro.raça)
print(Cachorro.peso)
Cachorro.texto()

#Gustavo São Jorge
class Gustavo:
    def __init__(self, beleza, estatura):
        self.beleza = beleza
        self.estatura = estatura
    def texto(self):
        print(f'O Gustavo é um ser {self.beleza} e um {self.estatura}')
    
SãoJorge = Gustavo('degradado, horrível, tenebras', 'exo-esqueleto de capivara')
print(SãoJorge.beleza)
print(SãoJorge.estatura)
SãoJorge.texto()