num_1 = int(input('Insira um número:\n'))
num_2 = int(input('Insira um outro número:\n'))

if num_1 > num_2:
    print(f'O número {num_1} é maior que o número {num_2}')
elif num_2 > num_1:
    print(f'O número {num_2} é maior do que o número {num_1}')
else:
    print('Os números são iguais.')