"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

count = 0
total = 0

for i in range(1, 6):
    num = float(input(f'Insira o {i} número ----> '))
    count += 1
    total += num

soma = total
media = (total) / count

print(f'\nA soma dos {i} números é ----> {soma}')
print(f'A média dos {i} números é ---> {media}\n')
