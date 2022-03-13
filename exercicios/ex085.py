"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas."""

from cmath import inf

# Declaração de variáveis
high_height = -inf
low_height = inf
number_high_height = 0
number_low_height = 0

for i in range(1, 11):
    student_number = int(input(f'\nInsira seu número (Aluno {i}): '))
    student_height = int(input(f'Insira seu altura em CM (Aluno {i}): '))

    # ----> Verificar qual aluno mais alto e qual aluno mais baixo, juntamente com seus respectivos números
    if student_height > high_height:
        high_height = student_height
        number_high_height = student_number

    if student_height < low_height:
        low_height = student_height
        number_low_height = student_number

print(f'\nO aluno mais alto é o número = {number_high_height}.')
print(f'Ele possui {high_height} cm.')
print(f'\nO aluno mais baixo é o número = {number_low_height}.')
print(f'Ele possui {low_height} cm.\n')
