"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e 
armazene num vetor a média de cada aluno, imprima o número de 
alunos com média maior ou igual a 7.0.
"""

note_list = []
count_media = 0

for i in range(1, 3):
    student = str(input('\nInsira seu nome: '))

    for i in range(1, 5):
        note = int(input(f'Insira sua {i}° nota: '))
        note_list.append(note)
        media = sum(note_list) / len(note_list)

    print(f'\nSua média é: {media:.2f}')
    if media >= 7:
        count_media += 1

print(f'\nAlunos Aprovados: {count_media}\n')
