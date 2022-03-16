"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

term = int(input('Insira a quantidade de termos que você deseja ----> '))
t1 = 1
t2 = 1
t3 = t1 + t2

print(f'{t1} -> {t2} -> ', end='')

for i in range(2, term):
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(f'{t3} -> ', end='')

print('FIM')
