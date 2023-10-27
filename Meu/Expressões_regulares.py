import re 

'''
string = "Caio"

# Pattern == Padrão
pattern = re.compile('^[a-zA-Z]{4}')

# Verifica se a string corresponde ao padrão (pattern)
x = re.findall(pattern, string)

print(x)
'''


# Compile cria um padrão


# . representa qualquer caracter que não seja \n

# ^ representa o inicio de uma string

# $ representa o final de uma string

# [^] Diferente de um caracter

# \w é um alfanum
# \W não é um alfam

# \s é um espaço    
# \S não é um espaço

# \d números de 0-9
# \D caracteres não numéricos

# [] conjunto de possibilidades


# + um ou mais possibilidades

# * 0 ou mais possibilidades

# ? 0 a 1 possibilidades

# {x} x vezes

# {z,y} z mínimo y máximo


# Fullmatch compara se a string inteira segue o padrão definido


# Exercícios

#CPF
'''
string = '222.222.222.22'

pattern = re.compile('[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}')

x = re.findall(pattern, string)

print(x)'''

#Email

String = 'aleatorio123@gmail.com.br'

pattern = re.compile('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com\.[a-zA-Z]{0,5}')

x = re.findall(pattern, String)

print(x)