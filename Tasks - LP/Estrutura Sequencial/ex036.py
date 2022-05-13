"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data 
válida.
"""

print('Insira uma data no formato dd/mm/aaaa.')

dia = int(input('Dia ----> '))
if dia > 31:
    print('O dia não é válido.')
    quit()

mes = int(input('Mês ----> '))
if mes > 12:
    print('O mês não é válido.')
    quit()

ano = int(input('Ano ----> '))
if ano > 2022:
    print('O ano não é válido.')
    quit()

print(f'A data {dia}/{mes}/{ano} inserida é válida.')
