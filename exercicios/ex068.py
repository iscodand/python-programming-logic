"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível."""

num = int(input('Insira um número ----> '))
count = 0
multi = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
        multi = i
        print(f'O número é divisível por ----> {multi}\n', end='')
if count == 2:
    print('\nO número é primo.\n')
else:
    print('\nO número não é primo.\n')
