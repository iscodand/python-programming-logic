"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num1 = float(input('Insira um número: '))
num2 = float(input('Insira mais um número: '))

if num1 > num2:
    print('O número maior é', num1)
elif num1 < num2:
    print('O número maior é', num2)
else:
    print('Os número são iguais.')
