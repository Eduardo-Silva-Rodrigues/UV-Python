lista_compras = []
valor = 0
preço = [(0 + valor)]
chave = ''

def inicio(chave):
    chave = input('\n\n\n\nBem-vindo ao mercadinho do Michael! Escolha seus produtos: \n\n1 - Coca-Cola Lata (R$ 3,00)\n2 - Pilha (R$ 5,00)\n3 - Paçoca (R$ 1,50)\n4 - Amido de milho (R$ 12,00)\n0 - Para finalizar a compra\n\nEscolha ao digitar o número do item: ')
    print('\n\n\n\n\n\n\n\n')
    def painel(chave): 
        if chave == '1':
            lista_compras.append('Coca-Cola Lata')
            print('\n\n\n\n\n=======================================================\n', lista_compras,'\n=======================================================')
        elif chave == '2':
            lista_compras.append('Pilha')
            print('\n\n\n\n\n=======================================================\n', lista_compras,'\n=======================================================')
        elif chave == '3':
            lista_compras.append('Paçoca')
            print('\n\n\n\n\n=======================================================\n', lista_compras,'\n=======================================================')
        elif chave == '4':
            lista_compras.append('Amido de milho')
            print('\n\n\n\n\n=======================================================\n', lista_compras,'\n=======================================================')
        elif chave == '0':
            n_item = input('\n\n\n\n\n\nOpções de finalização:\n\n0 - Finalizar as compras\n\n(Número do item) - Remover item\n\nSelecione a opção desejada: ')
            print('\n\n\n\n\n\n\n\n\n')
            if n_item == '1':
                lista_compras.remove('Coca-Cola Lata')
                print('\n\n\n\n\n=======================================================\n', lista_compras,'\n=======================================================')
                return painel(chave)
            elif n_item == '2':
                lista_compras.remove('Pilha')
                print('\n\n\n\n\n=======================================================\n',lista_compras,'\n=======================================================')
                return painel(chave)
            elif n_item == '3':
                lista_compras.remove('Paçoca')
                print('\n\n\n\n\n=======================================================\n', lista_compras,'\n=======================================================')
                return painel(chave)
            elif n_item == '4':
                lista_compras.remove('Amido de milho')
                print('\n\n\n\n\n=======================================================\n', lista_compras,'\n=======================================================')
                return painel(chave)
            elif n_item == '0':
                print('\nCompra finalizada!\n\nSua lista de compras é:\n\n',lista_compras,'\n\n\n\n\n\n')
                exit()
            else:
                print('Dado inválido!')
        else:
            print('Dado inválido!')    
    painel(chave)
    return inicio(chave)

inicio(chave)
