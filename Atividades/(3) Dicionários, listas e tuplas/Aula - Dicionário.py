dados_cliente = {
    'Nome': 'Eduardo',
    'Endereço': 'Rua ABC, 123',
    'Telefone': '4565654687'
}

print(dados_cliente['Nome'])

dados_cliente['Cidade'] = 'Godoy Moreira' # Adiciona mais um tópico no dicionário
print(dados_cliente)

dados_cliente.pop('Telefone') # Remove um tópico do dicionário
print(dados_cliente)

for indice, valor in dados_cliente.items():
    print(f'Indice: {indice}, valor: {valor}')
    print('---------------------------------')
