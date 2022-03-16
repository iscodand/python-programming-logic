"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias 
vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""

while True:
    num = int(input('\nInsira um valor ----> '))
    if not 0 < num < 16:
        print('Insira um valor válido.')
        continue
    fact = 1

    for i in range(num, 1, -1):
        fact *= i
    print(f'O fatorial do número {num} é {fact}.')
    
    if str(input('\nVocê deseja continuar [S/N]? ')).upper() != "S":
        print('\nFIM DO PROGRAMA.\n')
        break
