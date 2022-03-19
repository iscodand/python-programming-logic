"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a 
pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve 
fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição 
acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas 
restantes). As notas não são informados ordenadas. Um exemplo de saída do programa 
deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

notelist = []
high_note = 0

while True:
    athlete = str(input('\nNome do Atleta: '))
    for i in range(1, 8):
        note = float(input('Nota: '))
        notelist.append(note)
    notelist.sort()

    print('\n')
    print('-='*30)
    print(f'Resultado Final:')
    print(f'Atleta: {athlete}')
    print(f'Melhor nota: {max(notelist)}')
    print(f'Pior nota: {min(notelist)}')

    notelist.pop(6)
    notelist.pop(0)
    media_note = sum(notelist) / len(notelist)
    print(f'Média: {media_note:.2f}')
    print('-='*30)
