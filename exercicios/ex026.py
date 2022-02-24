"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

preco1 = float(input('Informe o preço do primeiro produto: '))
preco2 = float(input('Informe o preço do segundo produto: '))
preco3 = float(input('Informe o preço do terceiro produto: '))

if preco1 < preco2 and preco1 < preco3:
    print('O primeiro produto é o mais barato, custando R$', preco1)
elif preco2 < preco1 and preco2 < preco3:
    print('O segundo produto é o mais barato, custando R$', preco2)
else:
    print('O terceiro produto é o mais barato, custando R$', preco3)
