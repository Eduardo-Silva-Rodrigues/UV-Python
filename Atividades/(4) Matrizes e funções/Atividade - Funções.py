#Função sem parâmetro e sem retorno
def Olá_mundo():
    print('Olá Mundo!')

Olá_mundo()

#Função sem parâmetro com retorno
def soma():
    soma = 2 + 2
    return soma

print(soma())

#Função com parâmetro e com retorno
def Calculo(a, b):
    Resultado = a * b
    return Resultado

print(Calculo(4, 2))

def Coleta_Dados(nome, idade, cep):
    dado1 = nome
    dado2 = idade
    dado3 = cep
    return (dado1, dado2, dado3)

print(Coleta_Dados('Eduardo', 18, '86938-000'))Atividades/Atividade 8 - Funções.py