import numpy as np #Importando a biblioteca Numpy

dieimes_matriz = np.array([[3, 4, 1], [3, 2, 1]]) #Criando a matriz

soma = 0 #Criando variável para soma

for linha in dieimes_matriz: #Repetição para cada linha da matriz
    for numero in linha: #Repetição para cada número da matriz
        soma += numero #Atribuição e soma dos números na variável "soma"
        print(soma) #Print da soma de todos os números da matriz