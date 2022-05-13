"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

dia = int(input('Para saber o dia da semana, insira um número de 1 a 7 ----> '))

if dia == 1:
    print('O dia da semana é domingo.')
elif dia == 2:
    print('O dia da semana é segunda.')
elif dia == 3:
    print('O dia da semana é terça.')
elif dia == 4:
    print('O dia da semana é quarta.')
elif dia == 5:
    print('O dia da semana é quinta.')
elif dia == 6:
    print('O dia da semana é sexta.')
elif dia == 7:
    print('O dia da semana é sábado.')
else:
    print('Só são aceitos números de 1 a 7.')
