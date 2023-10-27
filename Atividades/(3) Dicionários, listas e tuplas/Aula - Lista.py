#Lista

Lista1 = ['Eduardo', 'Marcelo', 'Davi', 'Sofia', 'Josi']

print(type(Lista1))
print(len(Lista1))
print(Lista1[4])

Lista2 = Lista1 * 2

print(Lista2)

Lista1.append('Rose') #Adiciona um novo item no final da lista

print(Lista1)

Lista1.remove('Eduardo') #Remove um item da lista

print(Lista1)

Lista1.pop(3)

print(Lista1) #Remove um item a partir da sua posição
