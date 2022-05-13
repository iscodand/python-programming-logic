"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 
6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em 
galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math

metros = float(input('Insira o valor em m² da área a ser pintada: '))

metros_com_dez = (metros * 1.0)

latas = math.ceil(metros / 108)
galoes = math.ceil(metros / 21.6)

valor_latas = (latas * 80)
valor_galoes = (galoes * 25)

latas_2 = math.floor(metros_com_dez / 108)
galoes_2 = math.ceil((metros_com_dez % 108) / (21.6))

valor_latas_galoes = (latas_2 * 80) + (galoes_2 * 25)

print('Caso você compre somente latas de 18 litros, você terá que pegar',
      latas, 'latas e pagará um total de', valor_latas, 'reais.')
print('Caso você compre somente galões de 3,6 litros, você terá que pegar',
      galoes, 'galões e pagará um total de', valor_galoes, 'reais.')
print('Caso você queira comprar latas e galões, você terá que pegar', latas_2,
      'latas e', galoes_2, 'galoes e pagará um total de', valor_latas_galoes, 'reais.')