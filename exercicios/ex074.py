"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

quantity_cds = int(input('Insira a quantidade de CDs que você possui ----> '))
media = 0
total = 0

for i in range(1, quantity_cds + 1):
    value = float(input(f'Insira o valor do {i}° CD ----> '))
    total += value
    media = quantity_cds / value

print(f'Você gastou, em média, {media:.2f} reais por CD.')
