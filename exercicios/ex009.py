"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

fah = float(input('Insira a temperatura em graus Fahrenheit: '))

celsius = 5 * ((fah-32) / 9)

print('A temperatura inserida em graus Fahrenheit equivale a',
      celsius, 'graus Celsius')
