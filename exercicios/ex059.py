"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem."""

base = int(input('Insira um valor para a base ----> '))
expo = int(input('Insira um valor para o expoente ----> '))
valor = 1

for i in range(1, expo + 1):
    valor *= base

print(f'A base {base} elevada ao expoente {expo} é igual a {valor}')
