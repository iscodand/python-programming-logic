"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por 
resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o 
sistema. Após todos os alunos terem respondido informar:

Total de Alunos que utilizaram o sistema;
Maior e Menor Acerto;
A Média das Notas da Turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o 
gabarito da prova antes dos alunos usarem o programa.
"""

from math import inf

count_corrects = 0
count_corrects_total = 0
count_students = 0

high_count_corrects = -inf
low_count_corrects = inf
student_high_count_corrects = ""
student_low_count_corrects = ""

while True:
    student = str(input('\nNome do estudante: '))
    for i in range(1, 11):
        answer = str(input(f'{i}° Questão - ').upper())
        if i == 1 and answer == "A":
            count_corrects += 1
        if i == 2 and answer == "B":
            count_corrects += 1
        if i == 3 and answer == "C":
            count_corrects += 1
        if i == 4 and answer == "D":
            count_corrects += 1
        if i == 5 and answer == "E":
            count_corrects += 1
        if i == 6 and answer == "E":
            count_corrects += 1
        if i == 7 and answer == "D":
            count_corrects += 1
        if i == 8 and answer == "C":
            count_corrects += 1
        if i == 9 and answer == "B":
            count_corrects += 1
        if i == 10 and answer == "A":
            count_corrects += 1
    
    print(f'Acertos ({student}) - {count_corrects}/10')

    if count_corrects > high_count_corrects:
        high_count_corrects = count_corrects
        student_high_count_corrects = student
    if count_corrects < low_count_corrects:
        low_count_corrects = count_corrects
        student_low_count_corrects = student

    count_corrects_total += count_corrects
    count_students += 1
    count_corrects = 0
        
    end = str(input('\nAlgum outro aluno irá usar o programa? [S/N] ----> ').upper())
    if end != "S":
        break

print(f'\nTotal de alunos: {count_students} alunos.')
print(f'\nAluno com a maior nota: {student_high_count_corrects} - {high_count_corrects}/10')
print(f'Aluno com a menor nota: {student_low_count_corrects} - {low_count_corrects}/10')

media_corrects = count_corrects_total / count_students
print(f'\nMédia de Pontuação: {media_corrects}/10\n')