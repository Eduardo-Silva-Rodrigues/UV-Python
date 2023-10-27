opçao = input('Escolha uma opção:\n \n 1 - Maçã\n 2 - Banana\n 3 - Manga\n 4 - Uva\n \n Selecione:')

try:
    opçao = int(opçao)
except:
    print('Opção inválida!')

if opçao == 1:
    print('\nVocê escolheu uma maçã!')
elif opçao == 2:
    print('\nVocê escolheu uma banana!')
elif opçao == 3:
    print('\nVocê escolheu uma manga!')
elif opçao == 4:
    print('\nVocê escolheu uma uva!')
else:
    print('\nEscolha uma das opções citadas anteriormente.')