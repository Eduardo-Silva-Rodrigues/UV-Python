Notas_Alunos = {'aluno 1' : 0,'aluno 2' : 0,'aluno 3' : 0}

for i in Notas_Alunos:
    valor = 0
    valor = float(input(f'Insira a nota do {i}:\n'))
    Notas_Alunos[i] = valor

soma = 0

for i, v in Notas_Alunos.items():
    soma = soma + v

media = soma / 2

print('A média dos alunos é de: ',media)