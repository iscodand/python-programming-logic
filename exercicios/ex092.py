"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um 
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
e depois informe a média dos saltos conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da 
execução, portanto não são ordenados. O programa deve ser encerrado quando não for 
informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

from cmath import inf

heelslist = []
high_heels = -inf
athlete_high_heels = ""

while True:
    print('-'*40)
    athlete = str(input('\nNome do Atleta: '))
    if athlete == "":
        break
    for i in range(1, 6):
        heels = float(input(f'Insira o {i}° salto: '))
        heelslist.append(heels)
    print('-'*40)
    print(f'\nPrimeiro Salto: {heelslist[0]} m')
    print(f'Segundo Salto: {heelslist[1]} m')
    print(f'Terceiro Salto: {heelslist[2]} m')
    print(f'Quarto Salto: {heelslist[3]} m')
    print(f'Quinto Salto: {heelslist[4]} m')

    # Organizei a lista para tirar o melhor e o pior salto
    heelslist.sort()
    print(f'\nMelhor Salto: {max(heelslist)} m')
    print(f'Pior Salto: {min(heelslist)} m')

    # Dei um "pop" na lista, removendo o melhor e o pior salto, para assim conseguir tirar a média dos demais
    heelslist.pop(4)
    heelslist.pop(0)
    media_heels = sum(heelslist) / len(heelslist)
    print(f'Média dos demais saltos: {media_heels:.1f} m')

    print(f'\nResultado Final:\n{athlete}: {media_heels:.1f} ')
