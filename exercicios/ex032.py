"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:"""

nota_1 = float(input('Insira a primeira nota ----> '))
nota_2 = float(input('Insira a segunda nota -----> '))
media = (nota_1 + nota_2) / 2

if media >= 9:
    atribuicao = "A"
elif media >= 7.5:
    atribuicao = "B"
elif media >= 6:
    atribuicao = "C"
elif media >= 4:
    atribuicao = "D"
else:
    atribuicao = "E"

if atribuicao == "A" or atribuicao == "B" or atribuicao == "C":
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print('Sua média foi ------>', media)
print('Seu conceito é ----->', atribuicao)
print('Sua situação é de -->', situacao)
