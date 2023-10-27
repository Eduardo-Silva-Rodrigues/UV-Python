altura = float(input('Insira a sua ALTURA para o calculo de IMC: \n'))
peso = float(input('Insira seu PESO para o calculo de IMC: \n'))

imc = peso / (altura ** 2)

print(f'O resultado do seu IMC é: {imc:,.2f}')