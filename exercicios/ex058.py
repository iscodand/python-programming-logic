"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro 
entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:
"""

num = int(input('Insira um número ----> '))
print(f'\nA tabuada de {num} é: ')
tabuada = 0

for i in range(1, 11):
    tabuada = num * i
    print(f'{num} x {i} = {tabuada}')
