"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou 
V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
"Valor Inválido!", conforme o caso.
"""

turno = (input(
    '[M] Matutino\n[V] Vespertino\n[N] Noturno\nInsira o turno que você estuda: '))

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Opção Inválida.')
