"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

a = int(input('Insira um número inteiro: '))
b = int(input('Insira mais um número inteiro: '))
c = float(input('Agora insira um número real: '))

primeiro = (a * 2) * (b / 2)
segundo = (a * 3) + c
terceiro = (c ** 3)

print('O resultado do produto do dobro do primeiro com metade do segundo é igual a', primeiro)
print('O resultado da soma do triplo do primeiro com o terceiro é igual a', segundo)
print('O resultado do terceiro elevado ao cubo é igual a', terceiro)
