"""Altere o programa anterior para mostrar no final a soma dos números."""

num = int(input('Insira o 1° número ----> '))
num2 = int(input('Insira o 2° número ----> '))
soma = 0

for i in range(num + 1, num2):
    soma += i

print(f'A soma entre os números do intervalo é ----> {soma}')
