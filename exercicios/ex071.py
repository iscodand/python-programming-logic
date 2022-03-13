"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada."""

quantity = int(input('Insira a quantidade de pessoas ----> '))
total = 0
media = 0

for i in range(1, quantity + 1):
    age = int(input(f'Insira a idade da {i}° pessoa: '))
    total += age
    media = (total) / quantity
if media < 25:
    print(f'A turma é jovem, sua média de idade é de {media:.0f} anos.')
elif media < 60:
    print(f'A turma é adulta, sua média de idade é de {media:.0f} anos.')
else:
    print(f'A turma é idosa, sua média de idade é de {media:.0f} anos.')
