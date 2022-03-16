"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

value = int(input('\nInsira um valor: R$ '))
count_parcels = 0

# Formatação do Início
print('-'*110)
print('Valor da Dívida ---------- Valor dos Juros ----------- Quantidade de Parcelas ---------- Valor da Parcela')

# Usei um while aninhado para calcular o valor da parcela dentro do valor da dívida com juros
for i in range(10, 26, 5):
    value_increased = ((i / 100) * value) + value
    fees = value_increased - value
    print(f'R$ {value_increased}', end=' ')
    print(f'{fees:>27}', end=' ')

    while 0 <= 12:
        count_parcels += 3
        value_parcels = value_increased / count_parcels
        break

    print(f'{count_parcels:>27}', end=' ')
    print(f'{value_parcels:>32.2f}')

print('-'*110)
