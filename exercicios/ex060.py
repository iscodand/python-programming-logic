"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""

count_par = 0
count_impar = 0

for i in range(1, 11):
    number = int(input(f'Insira o {i}° número ----> '))
    if number % 2 == 0:
        count_par += 1
    else:
        count_impar += 1

print(f'\nO programa leu {count_par} números pares.')
print(f'O programa leu {count_impar} números ímpares.')
