"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

from cmath import sqrt

a = float(input('Insira o primeiro valor ---> '))
if a == 0:
    print('A equação não é do segundo grau.')
    quit()

b = float(input('Insira o segundo valor ----> '))
c = float(input('Insira o terceiro valor ---> '))
delta = (b ** 2) + (-4 * a * c)

if delta < 0:
    print('O valor de delta é negativo, a equação não possui raizes reais.')
    quit()
elif delta == 0:
    equacao = sqrt(delta) + (- b) / 2 * a
    print('A equação só possui uma raiz real --->', equacao)
else:
    equacao = sqrt(delta) + (- b) / 2 * a
    equacao2 = sqrt(delta) + (b) / 2 * a
    print('A equação possui duas raízes, sendo uma',
          equacao, 'e a outra', equacao2)
