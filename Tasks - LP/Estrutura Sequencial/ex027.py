"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

if a > b > c:
    print('A ordem decrescente dos números é: ', a, b, c)
elif a > c > b:
    print('A ordem decrescente dos números é: ', a, c, b)
elif b > a > c:
    print('A ordem decrescente dos números é: ', b, a, c)
elif b > c > a:
    print('A ordem decrescente dos números é: ', b, c, a)
elif c > a > b:
    print('A ordem decrescente dos números é: ', c, a, b)
else:
    print('A ordem decrescente dos números é: ', c, b, a)
