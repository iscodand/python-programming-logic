"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

valor = int(input('Insira o valor do saque ----> '))

if valor < 10 or valor > 600:
    print('Por favor, insira um valor entre 10 e 600 reais.')
    quit()

else:
    cem = valor // 100
    cinquenta = (valor % 100) // 50
    dez = (valor % 50) // 10
    cinco = (valor % 10) // 5
    um = (valor % 5) // 1

    print(f'Para sacar o valor de R$ {valor}, você receberá:')

    if cem > 0:
        print(f'{cem} Notas de R$ 100.')
    if cinquenta > 0:
        print(f'{cinquenta} Notas de R$ 50.')
    if dez > 0:
        print(f'{dez} Notas de R$ 10.')
    if cinco > 0:
        print(f'{cinco} Notas de R$ 5.')
    if um > 0:
        print(f'{um} Notas de R$ 1.')
