"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

quantity = int(input('\nQuantos números você deseja calcular? '))
soma = 0
maior = 0
menor = 0

for i in range(1, quantity + 1):
    num = int(input(f'Insira o {i}° número ----> '))
    soma += num

    if i == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'\nA soma dos {quantity} números inseridos é {soma}')
print(f'O maior número é ----> {maior}')
print(f'O menor número é ----> {menor}\n')
