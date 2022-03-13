"""Faça um programa que leia 5 números e informe o maior número."""

maior = 0

for i in range(1, 6):
    num = int(input(f'Insira o {i}° número ----> '))
    if i == 1:
        maior = num
    else:
        if num > maior:
            maior = num

print(f'O maior número é {maior}.')
