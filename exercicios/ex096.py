"""
Faça um Programa que leia um vetor de 10 números reais e 
mostre-os na ordem inversa.
"""

numlist = []

for i in range(10):
    numlist.append(int(input('Insira um valor: ')))

print(f'\nNúmeros: {numlist}.')
numlist = numlist[::-1]
print(f'Inverso: {numlist}.\n')
