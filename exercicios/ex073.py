"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

classes = int(input('\nInsira a quantidade de turmas ----> '))
total = 0
media = 0

for i in range(1, classes + 1):
    students = int(
        input(f'Insira a quantidade de alunos da {i}° turma ----> '))
    while students > 40:
        print('\nUma turma não pode ter mais de 40 alunos.')
        students = int(
            input(f'Insira a quantidade de alunos da {i}° turma ----> '))
    total += students
    media = total / classes

print(f'\nA média de alunos por turma é de {media:.0f} alunos.\n')
