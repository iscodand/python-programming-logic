"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""

numlist = []
pair = []
odd = []

for i in range(20):
    num = int(input('Insira um valor: '))
    numlist.append(num)
    if num % 2 == 0:
        pair.append(num)
    else:
        odd.append(num)

print(f'\nNúmeros: {numlist}')
print(f'Pares: {pair}')
print(f'Ímpares: {odd}\n')