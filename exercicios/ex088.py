"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos 
deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
"""

count_25 = 0
count_50 = 0
count_75 = 0
count_100 = 0

while True:
    num = int(input('\nInsira um número: '))
    print('Insira um número negativo para parar.')
    if num < 0:
        break
    if num < 25:
        count_25 += 1
    elif num < 50:
        count_50 += 1
    elif num < 75:
        count_75 += 1
    elif num < 100:
        count_100 += 1

print(f'\nPossui {count_25} números entre 0 e 25.')
print(f'Possui {count_50} números entre 25 e 50.')
print(f'Possui {count_75} números entre 50 e 75.')
print(f'Possui {count_100} números entre 75 e 100.\n')
