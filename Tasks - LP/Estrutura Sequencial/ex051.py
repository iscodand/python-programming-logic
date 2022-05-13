"""
Altere o programa anterior permitindo ao usuário informar as populações e as 
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""

population_1 = float(
    input('Insira a quantidade de habitantes da PRIMEIRA POPULAÇÃO ----> '))
population_2 = float(
    input('Insira a quantidade de habitantes da SEGUNDA POPULAÇÃO -----> '))
increase_1 = float(
    input('\nPorcentagem de aumento anual da PRIMEIRA POPULAÇÃO ----> '))
increase_2 = float(
    input('Porcentagem de aumento anual da SEGUNDA POPULAÇÃO -----> '))
years = 0

while population_1 <= population_2:
    years += 1
    population_1 += (population_1 * increase_1 / 100)
    population_2 += (population_2 * increase_2 / 100)

print(
    f'\nSerão necessários {years} anos para a PRIMEIRA POPULAÇÃO alcançar a SEGUNDA POPULAÇÃO.')
print(f'\nA PRIMEIRA POPULAÇÃO terá {population_1:.0f} habitantes.')
print(f'A SEGUNDA POPULAÇÃO terá {population_2:.0f} habitantes.\n')
