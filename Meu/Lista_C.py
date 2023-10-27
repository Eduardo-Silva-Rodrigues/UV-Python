carrinho = {

            }

#     Função para acessar painel de compras
def compras(setores):
#     Função de autorização para acessar painel de compras e efetuar as compras
    def painel():
        resp = input('\nDeseja iniciar uma compra neste setor?\n\nDigite "Sim" ou "Não" para fazer sua escolha: ')
        qtd_item = 0
        if resp == 'Sim':

            print('\nSetor > Açougue:')
            print('\n 1 - Carne moída (R$ 14,80 - KG)\n 2 - Carne de porco (R$ 19,90 - KG)\n 3 - Carne de boi (R$ 26,40 - KG)\n 4 - Patinho (R$ 40,99 - KG)\n \n=================================\n')
            item = input('\nEscolha o número do item que deseja comprar: ')
            qtd_item = input('Escolha a quantidade que você quer: ')
            
            if item == '1' and qtd_item != 0:
                qtd = float(qtd_item)
                carrinho['Item'] = 'Carne moída'
                carrinho['Quantidade'] = qtd_item
                carrinho['Preço'] = (14.80 * qtd)
                for indice, valor in carrinho.items():
                    print(f'\n{indice}: {valor}')
                    print('-----------------------------')
                return(painel())
            elif item == '2' and qtd_item != 0:
                qtd = float(qtd_item)
                carrinho['Item'] = 'Carne de porco'
                carrinho['Quantidade'] = qtd_item
                carrinho['Preço'] = (14.80 * qtd)
                for indice, valor in carrinho.items():
                    print(f'\n{indice}: {valor}')
                    print('-----------------------------')
                return(painel())
            elif item == '3' and qtd_item != 0:
                qtd = float(qtd_item)
                carrinho['Item'] = 'Carne de boi'
                carrinho['Quantidade'] = qtd_item
                carrinho['Preço'] = (14.80 * qtd)
                for indice, valor in carrinho.items():
                    print(f'\n{indice}: {valor}')
                    print('-----------------------------')
                return(painel())
            elif item == '4' and qtd_item != 0:
                qtd = float(qtd_item)
                carrinho['Item'] = 'Patinho'
                carrinho['Quantidade'] = qtd_item
                carrinho['Preço'] = (14.80 * qtd)
                for indice, valor in carrinho.items():
                    print(f'\n{indice}: {valor}')
                    print('-----------------------------')
                return(painel())
            elif item != '1' or '2' or '3' or '4':
                print('\nDado inválido!')
                return(painel())
        else:
            return(compras(setores))
#     #Match Case para exibir cada tipo de setor
    match setores:
        case '1':
            print('\nSetor > Açougue:')
            print('\n 1 - Carne moída (R$ 14,80 - KG)\n 2 - Carne de porco (R$ 19,90 - KG)\n 3 - Carne de boi (R$ 26,40 - KG)\n 4 - Patinho (R$ 40,99 - KG)\n \n=================================\n')

            painel()
        case '2':
            print('\nSetor > Produtos de limpeza:')
            print('\n 1 - Detergente Ype 500ml (R$ 2,69)\n 2 - Amaciante Downy 1,5L (R$ 28,12)\n 3 - Sabão em pó Omo (R$ 29,99)\n 4 - Água sanitária Ype 1L (R$ 6,06)\n')
        case '3':
            print('\nSetor > Massa e condimentos:')
            print('\n 1 - Macarrão Paganini Spaghetti 500g (R$ 9,99)\n 2 - Miojo Nissin 85g (R$ 2,69)\n 3 - Lasanha com Ovos Renata 500g (R$ 9,57)\n 4 - Molho De Tomate Sacciali Sachê Tradicional 300ml (R$ 18,69)\n 5 - Ketchup Heinz 567g (R$ 18,99)\n 6 - Ervilha QueroLata 170g (R$ 2,99)\n')
        case '4':
            print('\nSetor > Grãos:')
            print('\n 1 - Arroz Branco tipo 1 Camil 5kg (R$ 34,85)\n 2 - Feijão Carioca Camil 1kg (R$ 10,99)\n 3 - Feijão Preto Camil 1kg (R$ 10,99)\n 4 - Milho de pipoca Premiun Yoki 500g (R$ 10,39)\n 5 - Canjica Branca Viva Salute 200g (R$ 3,95)\n')
        case '5':
            print('\nSetor > Higiene:')
            print('\n 1 - Sabonete Barra Lux 85g (R$ 2,99)\n 2 - Shampoo 400ml + Condicioador 200ml Dove (R$ 24,99)\n 3 - Shampoo Anticaspa Clear Men 2 em 1 400ml (R$ 20,93)\n 4 - Kit 3 Escovas de dente Colgate (R$ 11,99)\n 5 - Pasta de dente Oral-b 70g (R$ 3,99)\n')
        case '6':
            print('\nSetor > Doce:')
            print('\n 1 - Bolacha Passatempo 130g (R$ 2,99)\n 2 - Chocolate Lacta ao Leite Shot 80g (R$ 6,99)\n 3 - Bala de gelatia Minhoca Cítrica Fini 90g (R$ 6,99)\n 4 - Brigadeiro Pronto Alispec 380g (R$ 12,59)\n')
        case '7':
            print('\nSetor > Hortifrúti:')
            print('\n 1 - Espinafre (R$ 3,79)\n 2 - Melão doce (R$ 29,98)\n 3 - Manga Palmer (R$ 3,84)\n 4 - Mamão Papaia (R$ 10,39)\n 5 - Cebola Nacional (R$ 1,62)\n')
        case _:
            print('\nDigite um número válido!\n')

#     Tela inicial para escolher o setor que deseja acessar
def inicio():
    print('Bem-Vindo! Escolha seu setor de compra para iniciar suas compras:\n')
    print(' 1 - Açougue\n 2 - Produtos de limpeza\n 3 - Massas e condimentos\n 4 - Grãos\n 5 - Higiene\n 6 - Doces\n 7 - Hortifrúti')
    setor = input('\n Escolha seu setor inserindo um número (1-7): ')

    if setor != 0:
        compras(setor)
    else:
        print('Digite um número válido!')

inicio()