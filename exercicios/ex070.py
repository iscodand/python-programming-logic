"""Faça um programa que calcule o mostre a média aritmética de N notas."""

quantity = int(input('\nInsira a quantidade de notas ----> '))
media = 0
total = 0

for i in range(1, quantity + 1):
    grades = float(input(f'Insira a {i}° nota ----> '))
    total += grades
    media = (total) / quantity

print(f'\nAs {quantity} notas inseridas tem uma média igual a {media:.2f}.\n')
