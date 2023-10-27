números = []

for contador in range(1, 6):
    n = int(input('Digite um número: '))
    números.append(n)        

print(números)

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

print (somalista(números))
