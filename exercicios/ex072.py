"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

print('-'*30)
print('CABINE ELEITORAL')
print('-'*30)
voters = int(input('\nInsira o número total de eleitores ----> '))
print('-'*30)

count_1 = 0
count_2 = 0
count_3 = 0

for i in range(1, voters + 1):
    vote = int(input(
        '\nPara votar no CANDIDATO 1, insira [1].\nPara votar no CANDIDATO 2, insira [2].\nPara votar no CANDIDATO 3, insira [3].\nVOTO ----> '))
    if vote == 1:
        count_1 += 1
    elif vote == 2:
        count_2 += 1
    elif vote == 3:
        count_3 += 1

print('\n')
print('-'*30)
print(
    f'\nRESULTADO\nCandidato 1 ----> {count_1} votos.\nCandidato 2 ----> {count_2} votos.\nCandidato 3 ----> {count_3} votos.')
