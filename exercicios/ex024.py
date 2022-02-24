"""Faça um Programa que leia três números e mostre o maior deles."""

a = float(input('Insira o primeiro número: '))
b = float(input('Insira o segundo número: '))
c = float(input('Insira o terceiro número: '))

if a > b and a > c:
    print(a, 'é o maior número.')
elif b > a and b > c:
    print(b, 'é o maior número.')
else:
    print(c, 'é o maior número.')
