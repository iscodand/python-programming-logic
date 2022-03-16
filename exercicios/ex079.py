"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que 
leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior 
temperaturas informadas, bem como a média das temperaturas.
"""

from cmath import inf

highest = -inf
lowest = inf
quantity = 0
total = 0
media = 0

while True:
    quantity += 1
    temperature = int(
        input(f'{quantity}° temperatura em Celsius (0 para encerrar) ----> '))
    total += temperature
    if temperature == 0:
        break

    if temperature > highest:
        highest = temperature
    if temperature < lowest:
        lowest = temperature

media = total / quantity

print(f'\nMédia das Temperaturas ----> {media} C°')
print(f'Menor temperatura ----> {lowest} C°')
print(f'Maior temperatura ----> {highest} C°')
