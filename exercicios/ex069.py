"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""

limit = int(input('\nAté qual número você deseja verificar? ----> '))
lista = []
count = 0

for i in range(limit + 1):
    if i % 2 == 1 and i != 2:
        count += 1
        lista.append(i)

print(
    f'\nEntre 1 e {limit} foram encontrados os seguintes números primos ----> {lista}.\n')
print(f'Para encontrar esses números, foram necessárias {count} divisões.\n')
