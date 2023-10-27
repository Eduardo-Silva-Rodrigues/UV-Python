#                       Comando Match simples

'''match command:
    case 'Hello World!':
        print('Hello World Too!')
    case 'Good Bye World!':
        print('See you later')
    case other:
        print('No match found')'''




def command(cond):
    match cond:
        case 'Sim':
            return print('Você aceitou a solicitação de amizade!')
        case 'Não':
            return print('Você recusou a solicitação de amizade!')
        case _:
            return print('Você tem uma solicitação de amizade pendente!')

resp = input('Insira algo:')

command(resp)




#                       Comando Match com função Def

'''def file_handler_v1(command):
  match command.split():
     case ['show']:
         print('List all files and directories: ')
         # code to list files
     case ['remove', *files]:
         print('Removing files: {}'.format(files))
         # code to remove files
     case _:
         print('Command not recognized')

file_handler_v1('r')'''


'''def file_handler_v2(command):
     match command.split():
         case ['show']:
             print('List all files and directories: ')
             # code to list files
         case ['remove' | 'delete', *files] if '--ask' in files:
             del_files = [f for f in files if len(f.split('.'))>1]
             print('Please confirm: Removing files: {}'.format(del_files))
             # code to accept user input, then remove files
         case ['remove' | 'delete', *files]:
             print('Removing files: {}'.format(files))
             # code to remove files
         case _:
             print('Command not recognized')

file_handler_v2('remove list1 list2 --ask')'''




#                       Loop For com lista

'''students_countries = ['Belgium', 'Czech Republic', 'France',
                      'Germany', 'Hungary', 'Ireland',
'Netherlands', 'Spain']
new_countries = 0
new_students_countries = {'Brazil', 'Brazil', 'Russian'}
for country in new_students_countries:
    if country not in students_countries:
        new_countries += 1
print('We have students from', new_countries, 'new countries.')'''




#                       Loop For com tupla

'''new_students = ('James Bond', 'Adele Schmidt', 'Leonardo Ferrari')
for name in new_students:
    print('Where does', name, 'come from?') '''




#                       Loop for com dicionário

'''new_students_countries_dict = {'James Bond': 'Great Britain',
                               'Adele Schmidt': 'Germany',
                               'Leonardo Ferrari': 'Italy'}
for key, value in new_students_countries_dict.items():
    print(key, ' is from ', value, '.', sep = '')'''



#                       Função Def Básica

'''def hello(meu_nome,idade):
    print('Olá', meu_nome, '\nSua idade é:', idade)

hello('Eduardo',18)'''



#                       Função Def com cálculo

'''def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))
    return salario

horas_trabalhadas = input('Insira a quantidade de horas trabalhadas:\n')
v_horas = input('Insira agora o valor da hora trabalhada:\n')

total_salario = calcular_pagamento(horas_trabalhadas, v_horas)  

print('O valor total do seu salário é de: ', total_salario)'''