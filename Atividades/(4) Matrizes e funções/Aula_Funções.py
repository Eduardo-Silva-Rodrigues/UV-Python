#Função sem parâmetro e sem retorno:
def limpartela():
    import os
    os.system("cls") #Limpar o terminal

limpartela()
print('Boa noite estudantes.')

#Função com passagem de parâmetro:
def soma (numero1, numero2):
    print(numero1 + numero2)

n1 = 2
n2 = 3

soma(n1, n2)

#Função com passagem de parâmetro com retorno:
def soma2 (numero1, numero2):
    return numero1 + numero2

resultado = soma2(3, 3)

print(resultado)

#Argumentos posicionais:
def exemplo(a, b, c):
    print(a, b, c)

exemplo(1, 2, 3)

#Argumentos nomeados:
def exemplo(a, b, c):
    print(a, b, c)

exemplo(a = 1, b = 3, c = 2)

#Argumentos posicionados e nomeados juntos:
def exemplo(a, b = 2, c = 3):
    print(a, b, c)

exemplo(1)
exemplo(1, c = 5)

#Múltiplos argumentos
def minha_funcao(*args):
    for arg in args:
        print(arg)
    print(type(args))

minha_funcao(1, 2, 3, 4)

#Multiplos argumentos 2:
def minha_funçao2(**kwargs):
    for chave, valor in kwargs.items(): #Função ".items" separa o índice e o valor de uma variável
        print(f'A chave é {chave} e o valor {valor}')
    print(type(kwargs))

minha_funçao2(nome = 'João', idade = 25, país = 'Brasil')

#IF __NAME__ == '__MAIN__':
def minha_funcao3():
    return "Função do módulo!"

if __name__ == '__main__':
    print('Este script está sendo executado sozinho!')
else:
    print('Este script foi importado!')