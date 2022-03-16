"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular 
a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print('Você foi aprovado com média:', media)

elif media < 7:
    print('Você foi reprovado com média:', media)

else:
    print('Você foi aprovado com distinção com média:', media)
