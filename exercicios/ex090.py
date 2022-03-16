"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de 
código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos 
tem-se o valor zero.
"""

print('\nVotação\n')
print('-'*30)
print('\nCaio - 1\nCarlos - 2\nIsco - 3\nMiguel - 4\nPaulo - 5\n')
print('\nVoto Nulo - 6\nVoto em Branco - 7\nEncerrar Programa - 0')

count_total = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0

while True:
    vote = int(input('\nSeu voto é: '))
    if vote == 0:
        break
    elif vote == 1:
        count_1 += 1
    elif vote == 2:
        count_2 += 1
    elif vote == 3:
        count_3 += 1
    elif vote == 4:
        count_4 += 1
    elif vote == 5:
        count_5 += 1
    elif vote == 6:
        count_6 += 1
    elif vote == 7:
        count_7 += 1
    else:
        print('\nEsse número inválido. Vote novamente.')
        vote = int(input('Seu voto é: '))
    count_total += 1

print(f'\n Caio = {count_1} votos.\nCarlos = {count_2} votos.\nIsco = {count_3} votos.\nMiguel = {count_4} votos.\nPaulo = {count_5} votos.')
print(f'Votos Nulos = {count_6}.\nVotos em Branco = {count_7}.\n')

percent_null = (count_6 / count_total) * 100
print(f'\nPorcentagem de votos nulos = {percent_null:.0f}%.\n')
percent_white = (count_7 / count_total) * 100
print(f'Porcentagem de votos em branco = {percent_white: .0f}%.\n')
