"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notes = []

for i in range(1, 5):
    notes.append(float(input(f'Insira a {i}° nota: ')))

media = sum(notes) / len(notes)
print(f'Média: {media:.2f}\n')
