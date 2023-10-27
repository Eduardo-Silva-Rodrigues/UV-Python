nome = str(input('Informe-nos o seu PRIMEIRO NOME: \n'))
sobrenome = str(input('Informe-nos o seu SOBRENOME: \n'))
idade = int(input('Informe-nos a sua IDADE: \n'))
altura = float(input('Informe-nos a sua ALTURA: \n'))
peso = float(input('Informe-nos o seu PESO: \n'))

if idade < 18:
    detalhe_idade = 'Menor de idade'
elif idade >= 18:
    detalhe_idade = 'Maior de idade'
else:
    detalhe_idade = 'Dado não encontrado'

if idade < 16:
    detalhe_idade2 = 'Não pode votar'
elif idade >= 16:
    detalhe_idade2 = 'Pode votar'
else:
    detalhe_idade2 = 'Dado não encontrado'

print(f'Ficha de Dados {nome} {sobrenome}: \n')
print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Idade: {idade}')
print(f'Altura: {altura}m')
print(f'Peso: {peso}kg\n')
print('Outros Detalhes:\n')
print(detalhe_idade)
print(detalhe_idade2,'\n')
