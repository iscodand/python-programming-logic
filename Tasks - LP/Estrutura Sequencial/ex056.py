"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no 
intervalo compreendido por eles.
"""

num = int(input('Insira o 1° número ----> '))
num2 = int(input('Insira o 2° número ----> '))

for i in range(num + 1, num2):
    print(i)
