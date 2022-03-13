"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""

salary = float(input('\nEstamos em 1995.\nInsira seu salário: R$'))
initial_year = 1995
year = int(input('Insira o ano desejado: '))
increase = 1.5 / 100

for i in range(initial_year, year + 1):
    salary *= 1 + increase
    increase *= 2

print(f'\nSeu salário no ano de {i} é de: R$ {salary:.2f}\n')
