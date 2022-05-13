"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

# ----> Cardápio
print('\nEspecificação ----- Código ------ Preço')
print('Cachorro Quente ---  100   ----- R$ 1,20')
print('Bauru Simples -----  101   ----- R$ 1,30')
print('Bauru com ovo -----  102   ----- R$ 1,50')
print('Hambúrguer --------  103   ----- R$ 1,20')
print('Cheeseburguuer ----  104   ----- R$ 1,30')
print('Refrigerante ------  105   ----- R$ 1,00\n')

final_value = 0
total_value = 0

while True:
    order = int(input('\nInsira o código do pedido ----> '))
    if order == 100:
        value = 1.20
    elif order == 101:
        value = 1.30
    elif order == 102:
        value = 1.50
    elif order == 103:
        value = 1.20
    elif order == 104:
        value = 1.30
    elif order == 105:
        value = 1.0
    else:
        print('Esse código é inválido.')
        order = int(input('\nInsira o código do pedido ----> '))

    quantity = int(input('Insira a quantidade desejada ---->'))

    total_value += value # ----> Calcular o valor total de todos os lanches
    final_value = total_value * quantity # ----> Vem depois do valor total, para a divisão ficar coerente

    end = str(input('Você deseja mais algo? [S/N] ----> ')).upper()   
    if end != "S":
        break

print(f'\nO valor total do pedido foi de ----> R$ {final_value:.2f}.\n')
