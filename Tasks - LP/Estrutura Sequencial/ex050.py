"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 
1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população
 do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
 """

population_1 = 80000
population_2 = 200000
years = 0

while population_1 <= population_2:
    years += 1
    population_1 += (population_1 * 3 / 100)
    population_2 += (population_2 * 1.5 / 100)

print(
    f'\nSerão necessários {years} anos para a PRIMEIRA POPULAÇÃO alcançar a SEGUNDA POPULAÇÃO.')
print(f'\nA PRIMEIRA POPULAÇÃO terá {population_1:.0f} habitantes.')
print(f'A SEGUNDA POPULAÇÃO terá {population_2:.0f} habitantes.\n')
