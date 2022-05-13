"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um 
valor válido.
"""

while nota > 10 or nota < 1:
    nota = int(input('Insira uma nota válida: '))

print('Você inseriu uma nota válida.')
