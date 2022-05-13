"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser 
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""

print(
    'Agora você será interrogado devido a um crime cometido recentemente.\nResponda as perguntas apenas com [S] para SIM e [N] para NÃO.')
provas = 0

primeira = (
    input('\n1° Pergunta  : Você telefonou pra vítima no dia do crime? ----> '))
if primeira == "S" or primeira == "s":
    provas += 1
elif primeira == "N" or primeira == "n":
    provas = provas
else:
    print('Por favor, insira uma opção válida!\nVocê terá que refazer o teste.')
    quit()

segunda = (
    input('2° Pergunta  : Você esteve no local do crime no dia do crime? ----> '))
if segunda == "S" or segunda == "s":
    provas += 1
elif segunda == "N" or segunda == "n":
    provas = provas
else:
    print('Por favor, insira uma opção válida!\nVocê terá que refazer o teste.')
    quit()

terceira = (input('3° Pergunta  : Você mora perto da vítima? ----> '))
if terceira == "S" or terceira == "s":
    provas += 1
elif terceira == "N" or terceira == "n":
    provas = provas
else:
    print('Por favor, insira uma opção válida!\nVocê terá que refazer o teste.')
    quit()

quarta = (input('4° Pergunta  : Você devia algo a vítima? ----> '))
if quarta == "S" or quarta == "s":
    provas += 1
elif quarta == "N" or quarta == "n":
    provas = provas
else:
    print('Por favor, insira uma opção válida!\nVocê terá que refazer o teste.')
    quit()

quinta = (input('5° Pergunta  : Você já trabalhou com a vítima? ----> '))
if quinta == "S" or quinta == "s":
    provas += 1
elif quinta == "N" or quinta == "n":
    provas = provas
else:
    print('Por favor, insira uma opção válida!\nVocê terá que refazer o teste.')
    quit()

if provas < 2:
    print('\nVocê é Inocente.')
elif provas == 2:
    print('\nVocê é Suspeito.')
elif provas < 5:
    print('\nVocê é Cúmplice.')
else:
    print('\nVocê é o Assassino.')
