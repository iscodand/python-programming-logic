"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule 
seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

sexo = int(input(
    'Vamos calcular seu peso ideal. Insira [1] se você for homem e [2] se você for mulher. '))

if sexo == 1:
    alturah = float(input('Insira sua altura em metros, homem: '))
    pesoh = (72.7*alturah) - 58
    print('Seu peso ideal é igual a', pesoh, 'quilogramas.')

elif sexo == 2:
    alturam = float(input('Insira sua altura em metros, mulher: '))
    pesom = (62.1*alturam) - 44.7
    print('Seu peso ideal é igual a', pesom, 'quilogramas.')

else:
    print('Você inseriu um valor inválido, por favor, faça novamente.')
