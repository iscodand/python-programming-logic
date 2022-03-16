"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros 
vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da 
gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros_vendidos = float(input('Insira a quantidade de litros desejada ----> '))
combustivel = (input(
    'Insira o tipo de combustível: [G] para GASOLINA e [A] para ÁLCOOL ----> '))

if combustivel == "A":
    if litros_vendidos <= 20:
        desconto = (1.9) - (1.9 * 0.03)
    else:
        desconto = (1.9) - (1.9 * 0.05)

elif combustivel == "G":
    if litros_vendidos <= 20:
        desconto = (2.5) - (2.5 * 0.04)
    else:
        desconto = (2.5) - (2.5 * 0.06)

else:
    print('A opção inserida é INVÁLIDA.')
    quit()

if combustivel == "G":
    print(
        f'Você vai pagar um total de R$ {desconto * litros_vendidos} por {litros_vendidos} litros de gasolina.')
else:
    print(
        f'Você vai pagar um total de R$ {desconto * litros_vendidos} por {litros_vendidos} litros de álcool.')
