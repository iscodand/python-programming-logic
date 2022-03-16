"""
Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Fahrenheit.
"""

celsius = float(input('Insira a temperatura em graus Celsius: '))

temperatura = (celsius * 1.8) + 32

print('A temperatura inserida em graus Celsius equivale a',
      temperatura, 'graus Fahrenheit.')
