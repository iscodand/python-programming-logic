"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de 
um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
usando este link (em minutos).
"""

import math

arquivo = float(input('Insira o tamanho do arquivo em mb: '))
velocidade = float(input('Insira a velocidade da sua internet em mbps: '))

tempo = math.floor(arquivo / velocidade)

print('Seu arquivo irá demorar aproximadamente', tempo,
      'minutos para ter seu download concluído.')