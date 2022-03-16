"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da 
promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no 
cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e 
gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipo_carne = (input(
    'Bem Vindo! Você deseja qual tipo de carne?\nPara FILÉ DUPLO insira ---> [F]\nPara ALCATRA insira ------> [A]\nPara PICANHA insira ------> [P]\n------> '))
quantidade = float(
    input('\nAgora insira a quantidade desejada (em KG) ----> '))

carne = 0

if tipo_carne == "F" or tipo_carne == "f":
    carne = "FILÉ DUPLO"
    if quantidade < 5:
        valor = (4.9 * quantidade)
    else:
        valor = (5.8 * quantidade)
elif tipo_carne == "A" or tipo_carne == "a":
    carne = "ALCATRA"
    if quantidade < 5:
        valor = (5.9 * quantidade)
    else:
        valor = (6.8 * quantidade)
elif tipo_carne == "P" or tipo_carne == "p":
    carne = "PICANHA"
    if quantidade < 5:
        valor = (6.9 * quantidade)
    else:
        valor = (7.8 * quantidade)
else:
    print('Por favor, insira uma opção válida.')
    quit()

print(
    f'\nTipo e Quantidade ---> {quantidade} Kg de {carne}\nValor Total ---> R$ {valor}')

pagamento = (input(
    '\nVocê deseja pagar com o CARTÃO TABAJARA? [S] para SIM ou [N] para NÃO ----> '))

if pagamento == "S" or pagamento == "s":
    desconto = (valor * 0.05)
elif pagamento == "N" or pagamento == "n":
    desconto = 0
else:
    print('Por favor, insira uma opção válida.')
    quit()

print(f'\nO valor a ser pago pelo cliente é R$ {valor - desconto}.')
