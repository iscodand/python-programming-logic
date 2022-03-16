"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da 
digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos 
clientes
"""

from cmath import inf

# ----> Declaração de MUITAS variáveis
count = 1
total_height = 0
total_weight = 0

high_height = -inf
low_height = inf
high_weight = -inf
low_weight = inf

code_hight_height = 0
code_low_height = 0
code_high_weight = 0
code_low_weight = 0

medium_height = 0
medium_weight = 0

# ----> Aqui o usuário insere suas informações

while True:
    code = int(input(f'\nCódigo do Cliente {count}: '))
    if code == 0:
        break
    height = float(input(f'Altura do Cliente (cm) {count}: '))
    weight = float(input(f'Peso do Cliente (kg) {count}: '))
    count += 1
    total_height += height
    total_weight += weight

    # ----> Verificação de maior e menor pesos e alturas, juntamente com o código do respectivo cliente
    if height > high_height:
        high_height = height
        code_high_height = code
    if height < low_height:
        low_height = height
        code_low_height = code
    if weight > high_weight:
        high_weight = weight
        code_high_weight = code
    if weight < low_weight:
        low_weight = weight
        code_low_weight = code

medium_height = total_height / count - 1
medium_weight = total_weight / count - 1

print(
    f'\nMaior Altura: {high_height} cm. - Código do Cliente: {code_high_height}')
print(f'Menor Altura: {low_height} cm. - Código do Cliente: {code_low_height}')
print(
    f'\nMaior Peso: {high_weight} kg. - Código do Cliente: {code_high_weight}')
print(f'Menor Peso: {low_weight} kg. - Código do Cliente: {code_low_weight}')

print(f'\nAltura Média: {medium_height:.0f} cm.')
print(f'Peso Médio: {medium_weight:.0f} kg.\n')
