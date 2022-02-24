"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

a = int(input('Insira o tamanho do primeiro lado ---> '))
b = int(input('Insira o tamanho do segundo lado ----> '))
c = int(input('Insira o tamanho do terceiro lado ---> '))

if a == b and a == c:
    print('Esse é um Triângulo Equilátero.')
elif a == b and a != c or a == c and a != b or c == b and c != a:
    print('Esse é um Triângulo Isóceles.')
else:
    print('Esse é um Triângulo Escaleno.')