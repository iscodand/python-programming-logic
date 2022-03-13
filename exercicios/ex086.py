"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""

from cmath import inf

# ----> Declaração de variáveis
count_city = 1
total_vehicles = 0
total_accidents = 0
count_accidents = 0

high_accidents = -inf
low_accidents = inf
code_high_accidents = 0
code_low_accidents = 0

medium_vehicles = 0
medium_accidents = 0

# ----> Usuário insere as informações solicitadas
for i in range(1, 6):
    city_code = int(input(f'\nInsira o Código da Cidade {count_city}: '))
    qtd_vehicles = int(
        input(f'Insira a Quantidade de Veículos da Cidade {count_city}: '))
    qtd_accidents = int(
        input(f'Insira a Quantidade de Acidentes da Cidade {count_city}: '))
    count_city += 1
    total_vehicles += qtd_vehicles
    if qtd_vehicles < 2000:
        total_accidents += qtd_accidents
        count_accidents += 1

    # ----> Identificar qual cidade tem mais e qual tem menos acidentes, além da identificação dos seus códigos
    if qtd_accidents > high_accidents:
        high_accidents = qtd_accidents
        code_high_accidents = city_code
    if qtd_accidents < low_accidents:
        low_accidents = qtd_accidents
        code_low_accidents = city_code

medium_vehicles = total_vehicles / i
medium_accidents = total_accidents / count_accidents

print(
    f'\nCódigo da Cidade com maior Índices de Acidentes:{code_high_accidents}.')
print(f'Número de Acidentes: {high_accidents}.')
print(
    f'\nCódigo da Cidade com menor Índices de Acidentes: {code_low_accidents}.')
print(f'Número de Acidentes: {low_accidents}.')
print(f'\nMédia de Veículos das {i} Cidades: {medium_vehicles:.0f}.')
print(
    f'\nMédia de Acidentes em Cidades com menos de 2000 Veículos: {medium_accidents:.0f}.\n')
